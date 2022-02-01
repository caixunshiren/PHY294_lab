from scipy.signal import find_peaks
import numpy as np
import pandas as pd

#  load data
F02, F04 = pd.read_csv('data/02.txt', delim_whitespace=True), pd.read_csv('data/04.txt', delim_whitespace=True)
F06, F08 = pd.read_csv('data/06.txt', delim_whitespace=True), pd.read_csv('data/08.txt', delim_whitespace=True)

# find peak
peaks_CH1 = []
peaks_CH2 = []
for F in [F02, F04, F06, F08]:
    peaks, _ = find_peaks(np.array(F['CH2(V)']), width=10)
    peaks_CH1.append(F['CH1(V)'][peaks].to_numpy())
    peaks_CH2.append(F['CH2(V)'][peaks].to_numpy())

# visualize
import matplotlib.pyplot as plt

for index, F in enumerate([F02, F04, F06, F08]):
    plt.plot(F['CH1(V)'], F['CH2(V)'], ls='-', color='blue')
    plt.scatter(peaks_CH1[index], peaks_CH2[index], color='red')
    plt.title("Trial 0" + str(index * 2 + 2))
    plt.show()

# drop F02's error
peaks_CH1[0], peaks_CH2[0] = np.delete(peaks_CH1[0], 1), np.delete(peaks_CH2[0], 1)

# drop close datapoint
max_gap = 0.2
for i, CH1 in enumerate(peaks_CH1):
    CH2 = peaks_CH2[i]
    diff = (CH1[1:] - CH1[0:-1]).tolist()
    new_CH1 = []
    new_CH2 = []
    flag = False
    for j, value in enumerate(diff):
        if flag:
            flag = False
            continue
        if value > max_gap:
            new_CH1.append(CH1[j])
            new_CH2.append(CH2[j])
        else:
            new_CH1.append((CH1[j] + CH1[j + 1]) / 2)
            new_CH2.append((CH2[j] + CH2[j + 1]) / 2)
            flag = True

    if diff[-1] > max_gap:
        new_CH1.append(CH1[-1])
        new_CH2.append(CH2[-1])
    peaks_CH1[i] = np.array(new_CH1)
    peaks_CH2[i] = np.array(new_CH2)

# visualize again
for index, F in enumerate([F02, F04, F06, F08]):
    plt.plot(F['CH1(V)'], F['CH2(V)'], ls='-', color='blue')
    plt.scatter(peaks_CH1[index], peaks_CH2[index], color='red')
    plt.title("Trial 0" + str(index * 2 + 2) + " Fixed")
    plt.show()

# calculate peak differences
peak_differences = []
for CH1 in peaks_CH1:
    peak_differences += (CH1[1:] - CH1[0:-1]).tolist()
print(peak_differences)

# save diff
df = pd.DataFrame(peak_differences)
# saving the dataframe
df.to_csv('peak_differences.csv')
