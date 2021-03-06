clear
clf

load("data/F02.mat");
load("data/F04.mat");
load("data/F06.mat");
load("data/F08.mat");
F02 = F02{:,:};
F04 = F04{:,:};
F06 = F06{:,:};
F08 = F08{:,:};


plot(F02(:,1), F02(:,2), '-'); 
hold on;
plot(F04(:,1), F04(:,2), '-'); 
plot(F06(:,1), F06(:,2), '-'); 
plot(F08(:,1), F08(:,2), '-'); 

title('Observed Electrometer Voltage vs. Input E3 Voltage for Franck & Hertz Experiment');
xlabel('Input E3 Voltage (V)');
ylabel('Observed Electrometer Voltage (V)');
legend('Trial 2','Trial 4', 'Trial 6', 'Trial 8', 'Location','Best');
hold off;