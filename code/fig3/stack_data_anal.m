%{
stack_data_anal.m

SHSH <herho@terpmail.umd.edu>
1/15/22
calculate high-pass stack ts of d18O var in Muna

%}

clear all; close; clc

%% read data
tg01c = readtable("../../data/raw_data/cleantg01c.csv");
tg11a = readtable("../../data/raw_data/cleantg11a.csv");
mun63 = readtable("../../data/raw_data/cleanmun63.csv");

%% set t vec
max_date = [max(floor(tg01c.date)), max(floor(tg11a.date)), max(floor(mun63.date))];
min_date = [min(floor(tg01c.date)), min(floor(tg11a.date)), min(floor(mun63.date))];

t = min(min_date):max(max_date);

%% calculate anom
anom_tg01c = anomal(tg01c, t);
anom_tg11a = anomal(tg11a, t);
anom_mun63 = anomal(mun63, t);


%% low_pass filt
high_pass_tg01c = highpassAnom(anom_tg01c, 2);
high_pass_tg11a = highpassAnom(anom_tg11a, 2);
high_pass_mun63 = highpassAnom(anom_mun63, 2);

% median & var of each
grand_med_tg01c = round(nanmedian(nanmedian(high_pass_tg01c, 2)), 2);
grand_med_tg11a = round(nanmedian(nanmedian(high_pass_tg11a, 2)), 2);
grand_med_mun63 = round(nanmedian(nanmedian(high_pass_mun63, 2)), 2);

ci_95_tg01c = round(prctile(nanmedian(anom_tg01c, 2), [2.5 97.5]), 2);
ci_95_tg11a = round(prctile(nanmedian(anom_tg11a, 2), [2.5 97.5]), 2);
ci_95_mun63 = round(prctile(nanmedian(anom_mun63, 2), [2.5 97.5]), 2);

hp = [high_pass_tg01c high_pass_tg11a high_pass_mun63];

%% entire percentile calc.
pc=[2.5 50 97.5];
ci95 = round(prctile(hp, pc, 2), 2);

%% save data
final_ts = array2table([t' ci95]);
final_ts.Properties.VariableNames(1:4) = {'year','lower','median', 'upper'};
writetable(final_ts,'../../data/processed_data/muna_high_pass_stack.csv');

