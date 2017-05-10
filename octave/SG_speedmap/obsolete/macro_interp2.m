%function ZI = macro_interp2(Z, XI, YI, method)
% Dang Doan. 2016.12.07
% Interpolate the value ZI for the point (XI,YI) based on
% the data provided in:
% X_vect: array of x_i (X_vect=[x1, x2, ..., xN]
% Y_vect: array of y_i (Y_vect=[y1, y2, ..., yN]
% Z_vect: array of z_i (Z_vect=[z1, z2, ..., zN]
% with:
% f(x1,y1)=z1
% f(x2,y2)=z2
% ...
% f(xN,yN)=zN
% Compute: ZI=f(XI,YI)

function ZI = macro_interp2(Z, XI, YI, method)
  %narginchk (1, 6);
  %nargs = nargin;
  if nargin < 6 
    method = "linear";
  end
  
  % To do: check that length(X_vect)=length(Y_vect)=length(Z_vect)
  if (length(X_vect)~=length(Y_vect)) || (length(Y_vect)~=length(Z_vect))
  error('Must have length(X_vect)=length(Y_vect)=length(Z_vect)');
  
  point_Num = min(length(X_vect),length(Y_vect),length(Z_vect));
  
  di = zeros(point_Num,1); % initialize vector of distances from (x_i, y_i) to (XI, YI)
  
  dsum = 0;
  zdsum = 0;
  
    if (strcmp (method, "linear"))
      ## use (linear) weighted average
      for ii=1:point_Num 
      di(ii) = pair_distance(X_vect(ii), Y_vect(ii), XI, YI);
      dsum = dsum + di(ii);
      zdsum = zdsum + Z_vect(ii)*di(ii);
      end
      % to do: check the condition dsum!=0
      ZI = zdsum/dsum;
    end  
end