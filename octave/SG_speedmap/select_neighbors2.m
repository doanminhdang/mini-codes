%function [X_vect, Y_vect] = select_neighbors2(Z, XI, YI, level)
% Author: Dang Doan
% Date: 2016.12.07-2016.12.12
% Find the NONZERO neighbors around the point (XI, YI) in matrix Z
% Top left of matrix has coordinate (1,1); XI = axis x, YI = axis y
% Optional parameter: level, it indicates the neighborhood's "radius"
%
% Return the arrays of x_i and y_i of the found NONZERO neighbors

function [X_vect, Y_vect] = select_neighbors2(Z, XI, YI, level)
  %narginchk (3, 4);
  %nargs = nargin;
  if nargin < 3 
    error('There must be at least 3 parameters: Z, XI, YI!');
  end
  
  if nargin == 3 
    level = 5; % default level to look out
  end
  
  X_vect = [];
  Y_vect = [];
  
  col_Z = size(Z,2); % in Octave: columns(Z), this function is not available in Matlab
  row_Z = size(Z,1); % in Octave: rows(Z), this function is not available in Matlab
  
  % for ii=1:level
    min_left = max(1, XI - level); max_right = min(col_Z, XI + level);
    min_top = max(1, YI - level); max_bottom = min(row_Z, YI + level);

    sub_matrix_i = Z(min_top:max_bottom, min_left:max_right);
    [Y_vect, X_vect] = find(sub_matrix_i);
    
    X_vect = X_vect + min_left - 1; % convert the position in sub_matrix_i
    Y_vect = Y_vect + min_top - 1; % to the position in original matrix Z
    % note: the commands above perform addition of a constant to EVERY item in an array 
  % end
end
