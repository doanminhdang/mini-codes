%function d = pair_distance(x1,y1,x2,y2)
% Author: Dang Doan
% Date: 2016.12.07 
% Compute the distance between two points with Cartesian coordinates

function d = pair_distance(x1,y1,x2,y2)
  %narginchk (2, 4);
  %nargs = nargin;
  
  % Neu muon tranh dung ham sqrt, thi co the dung lookup table
  % Luu y la cac gia tri x, y deu la so nguyen, trong khoang 0-40
  d = sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
end
