%function ZI = multi_interp2(X_vect, Y_vect, Z_vect, XI, YI, method)
% Author: Dang Doan
% Date: 2016.12.07 
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
% Output: compute ZI=f(XI,YI)
% Currently, only 'linear' method is implemented (it is simple to use).

function ZI = multi_interp2(X_vect, Y_vect, Z_vect, XI, YI, method)
  %narginchk (1, 6);
  %nargs = nargin;
  if nargin < 6 
    method = 'linear';
  end
  
  % Check that length(X_vect)=length(Y_vect)=length(Z_vect)
  if (length(X_vect)~=length(Y_vect)) || (length(Y_vect)~=length(Z_vect))
  error('Must have length(X_vect)=length(Y_vect)=length(Z_vect)');
  end
  
  point_Num = length(X_vect);
  
  di = zeros(point_Num,1); % initialize vector of distances from (x_i, y_i) to (XI, YI)
  
  dsum = 0;
  zdsum = 0;
  
  %  if (strcmp (method, "linear"))
      % use (linear) weighted average
      for ii=1:point_Num 
        di(ii) = pair_distance(X_vect(ii), Y_vect(ii), XI, YI);
        dsum = dsum + di(ii); % adding to the total distance
        zdsum = zdsum + Z_vect(ii)*di(ii); % adding to the weighted sum
      end
      % TODO: check the condition dsum!=0
      % This issue may happen when the neighborhood is a singleton: (XI, YI)
      % or when X_vect or Y_vect contain some imaginary numbers (not used in this package)
      ZI = zdsum/dsum;
 %   end  
end
