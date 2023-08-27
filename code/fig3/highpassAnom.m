function [filtered_anom] = highpassAnom(anom_data, m)

%{
highpassAnom.m
(req. anomal.m; fssa.m)

SHSH <herho@terpmail.umd.edu>
1/14/22
function to calculate low-pass filtered enso vars 

anom_data: sub-annual ts
%}

    for ii = 1:size(anom_data,2)
        [e,ln,A,rc,check] = fssa(anom_data(:,ii), 7);
        filtered_anom(:,ii) = sum(rc(m:7,:),1)';
        clear e ln A rc check
    end
end

% ganti m