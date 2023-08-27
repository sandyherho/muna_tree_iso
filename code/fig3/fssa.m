function [e,ln,A,rc,check]=fssa(x,m); 
% function [e,l,A,rc,check]=fssa(x,m); 
% quick function to run ssa
% x=dataseries (NaNs ok)
% m=embedding dimension
% output
% 
% by MNE

i=find(~isnan(x));x(i)=x(i)-mean(x(i));
[nt ns]=size(x);
% x must be a row vector, otherwise, reorient
if nt>ns
  x=x';
[ns nt]=size(x);
end
% choose embedding dimension
% reasonable to choose m>2d+1
% with d=underlying dimension of dataset

% form trajectory matrix
X=zeros(m,nt-m+1);
for i=1:m
X(i,:)=x(i:nt-m+i);
end

% covariance of trajectory matrix
r=NaN.*zeros(m,m);
for i=1:m
  j=find(~isnan(X(i,:)));
  for k=i:m
    n=find(~isnan(X(k,:)));
    o=intersect(j,n);ol=length(o);Xm(k)=mean(X(k,o));
    r(i,k)=(X(i,o)-mean(X(i,o)))*(X(k,o)-mean(X(k,o)))'./(ol-m+1);
    r(k,i)=r(i,k); % symmetry
  end
end

% eofs of trajectory matrix
[e,l,e]=svd(r);
ln=diag(l)./trace(l);


% pcs of trajectory matrix
% for projection to get PCs, use X with zeros for NaNs 
% as in HW4
X0=X;
X0(find(isnan(X0)))=0;
A=e'*X0;

% RCs of the trajectory matrix

rc=zeros(m,length(A)+m-1);
for i=1:m
  rc(i,:)=conv(A(i,:),e(:,i));
end

% scaling as in Ghil et al. (2002)
for i=1:nt
  if i<=m-1,
    rc(:,i)=rc(:,i)./i;
  elseif i>=m && i<=nt-m+1,
    rc(:,i)=rc(:,i)./m;
  elseif i>=nt-m+2 && i<=nt,
    rc(:,i)=rc(:,i)./(nt-i+1);
  end
end

xc=sum(rc);
rc(find(rc==0.0000000))=NaN;
i=find(~isnan(x));
j=find(isnan(x));
check=sqrt(sum((x(i)-xc(i))*(x(i)-xc(i))'./nt));
%[check]
rc(:,j)=NaN;
return

