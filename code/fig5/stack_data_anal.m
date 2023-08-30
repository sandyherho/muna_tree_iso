%{
stack_data_anal.m

SHSH <herho@terpmail.umd.edu>
08/27/23
calculate high-pass ts of PHYDA nino34 var

%}

clear all; close; clc

data = readtable("../../data/raw_data/PhydaNino34AnnualMean.csv");
t = data.year;
nino34 = data.nino3_4;

anom_nino34 = nino34 - mean(nino34);

[e,ln,A,rc,check] = fssa(nino34, 7);
clear e ln A check
hpf_ts = sum(rc(2:7,:),1);
hpf_ts = array2table([t hpf_ts']);
hpf_ts.Properties.VariableNames(1:2) = {'year','nino34'};
writetable(hpf_ts,'../../data/processed_data/PhydaNino34_high_pass.csv'); 