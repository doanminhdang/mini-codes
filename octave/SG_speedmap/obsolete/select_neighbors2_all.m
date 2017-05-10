%function [X_vect, Y_vect] = select_neighbors2_all(Z, XI, YI, level)
% Dang Doan. 2016.12.12
% Find ALL the neighbors around the point (XI, YI) in matrix Z
% Top left of matrix has coordinate (1,1), XI = axis x, YI = axis y
%
% Return the arrays of x_i and y_i of the neighbors of (XI, YI)
% within the distance "level"
%
% Default value for "level": 3
%
% Dinh dung thuat toan tim neighbors DON GIAN, nhung gap cac van de:
% + Chay lau hon (do luc nao cung quet tat ca cac diem)
% + Khi tinh weighted average, thi cung can biet co bao nhieu gia tri zero
%   de loai bo, cho nen van khong the khong xac dinh so luong zero trong
%   neiborhood.
% De su dung trong code speedmap_fill:
% [X_vect, Y_vect] = select_neighbors2_all(Lack_v_data, col_Zero_v(ii), row_Zero_v(ii), Zone_effect);

function [X_vect, Y_vect] = select_neighbors2_all(Z, XI, YI, level)
  %narginchk (3, 4);
  %nargs = nargin;
  if nargin < 3 
    error('There must be at least 3 parameters!');
  end
  
  if nargin == 3 
    level = 5; % default level to look out
  end
  
  X_vect = [];
  Y_vect = [];
  
  col_Z = size(Z,2); % in Octave: columns(Z), this function is not available in Matlab
  row_Z = size(Z,1); % in Octave: rows(Z), this function is not available in Matlab
  
    min_left = max(1, XI - level); max_right = min(col_Z, XI + level);
    min_top = max(1, YI - level); max_bottom = min(row_Z, YI + level);
    for jj=min_top:max_bottom
      for kk=min_left:max_right
        Y_vect = [Y_vect; jj];
        X_vect = [X_vect; kk];
      end
    end

end