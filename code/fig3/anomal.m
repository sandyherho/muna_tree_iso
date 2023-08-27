function [anom] = anomal(sample, t)

%{
anomal.m

SHSH <herho@terpmail.umd.edu>
1/12/22
function to calculate anomaly from the entire ts sample

sample: 1D ts
t : time vector 
%}

rng(212) % fixed random num generator for reproducibility
    for it = 1:length(t)
        x = find(floor(sample.date) == t(it));
        if length(x) == 0
            random1(it,1:1000) = nan;
        else
            par1 = mle(sample.o18(x),'distribution','uniform');
            random1(it,:) = random('uniform',par1(1),par1(2),1,1000);
        end
        clear x par1
    end

    [nx,ny]=size(random1);
    clim = ones(nx,1)*(nanmean(random1,1)*ones());
    anom = random1-clim;
    clear random1 clim
end
