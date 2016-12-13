%function Full_v_data = speedmap_fill(Lack_v_data, col_Zero_v, row_Zero_v, Zone_effect)
% Author: Dang Doan
% Date: 2016.12.12
% Day la thuat toan chinh de dien cac du lieu vao o trong 
% trong ma tran chua van toc trung binh cua xe
%
% Parameters:
%   Lack_v_data: ma tran chua du lieu ban dau, co the co nhung o trong
%   col_Zero_v: hoanh do (vi tri tren truc x) cua cac o trong 
%   row_Zero_v: tung do (vi tri tren truc y) cua cac o trong 
%     Hai array row_Zero_v va col_Zero_v phai co cung chieu dai,
%     chung cho biet toa do tuong ung (x,y) cua cac o can noi suy du lieu.
%   Zone_effect: kich thuoc cua vung anh huong den tung o khi noi suy.

function Full_v_data = speedmap_fill(Lack_v_data, col_Zero_v, row_Zero_v, Zone_effect)

% Set default options
  if nargin < 5
    smooth_coeff = 1;
  end

  if nargin < 4
    Zone_effect = 5;
  end

Full_v_data = Lack_v_data; % initialize the full matrix, to be filled

for ii=1:length(row_Zero_v)
% Note: interp2 is NOT the correct function to use 
% Old command: Full_v_data(row_Zero_v(i),col_Zero_v(i))=interp2(1:Col_length,1:Row_length,Full_v_data, col_Zero_v(i), row_Zero_v(i));

% Chon cac neighbors co gia tri du lieu (o vi du nay, do la cac o non-zero)
[X_vect, Y_vect] = select_neighbors2(Lack_v_data, col_Zero_v(ii), row_Zero_v(ii), Zone_effect);

% Lap vector chua cac gia tri van toc cua cac neighbors co du lieu
Z_vect=zeros(size(X_vect));
  for jj=1:length(X_vect)
    Z_vect(jj) = Lack_v_data(Y_vect(jj), X_vect(jj)); %Y: row, X: column
  end

% Noi suy cho du lieu theo cac neighbors cua no
Full_v_data(row_Zero_v(ii),col_Zero_v(ii)) = multi_interp2(X_vect, Y_vect, Z_vect, col_Zero_v(ii), row_Zero_v(ii));
end;
