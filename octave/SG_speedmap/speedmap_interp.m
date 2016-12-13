% Bai toan noi suy giao thong o Sai Gon cho Doan Hiep
% Author: Dang Doan
% Date: 2016.12.05-2016.12.12
%-----

%% Overall problem parameters
ChieuRong=20; %km 
ChieuCao=15; %km
width_Cell=0.5; %km
height_Cell=0.5; %km
Sample=1000; %xe
Vmax=50; %kmph

%% Algorithm tuning parameters

% Danh cho viec generate ra du lieu
LamLoang = 2; % so lan lam loang du lieu
Out_ring = 3; % de lai 3 vong du lieu o phia ngoai

% Danh cho thuat toan xac dinh vung anh huong cua mot o
Level = 5;

%---

%% Generate data
Row_length=ChieuCao/height_Cell;
Col_length=ChieuRong/width_Cell;


x_Xe=zeros(1,Sample);
y_Xe=zeros(1,Sample);
v_Xe=zeros(1,Sample);

for i=1:Sample
x_Xe=ChieuRong*rand();
y_Xe=ChieuCao*rand();
v_Xe=Vmax*rand();
end;

%test:
% plot(x_Xe)
% plot(y_Xe)
% plot(v_Xe)

Combined_v=Vmax*rand(Row_length,Col_length);

%test:
%mesh(1:Col_length,1:Row_length,Combined_v);

% Tao ra cac o khong co du lieu
Lost_data=rand(Row_length,Col_length);
Lost_data_boolean=Lost_data>0.5;
Lack_v_data=Combined_v.*Lost_data_boolean;


for jj=1:LamLoang % lam them nhieu lan cho no mat di nhieu du lieu BEN TRONG
Lost_data_small=rand(Row_length-2*Out_ring,Col_length-2*Out_ring); 
Lost_data_small_boolean=Lost_data_small>0.5;
Lack_v_data(Out_ring+1:Row_length-Out_ring,Out_ring+1:Col_length-Out_ring)=Lack_v_data(Out_ring+1:Row_length-Out_ring,Out_ring+1:Col_length-Out_ring).*Lost_data_small_boolean;
end;

% Now find the cells that do not have data
[row_Zero_v,col_Zero_v]=find(not(Lack_v_data )); 
% moi gia tri tuong ung cua row va col se cho biet o do trong ma tran la zero

%% Load the sample data for testing
load Lack_data_LamLoang_2_Out_ring_3.mat

%test: 
disp('Tong so o: ');
Row_length*Col_length

disp('So o khong co du lieu luc dau: ');
length(row_Zero_v) %number of missing data cells
%mesh(1:Col_length,1:Row_length,Lack_v_data); %plot of the missing map

%% Noi suy cho tat ca cac o con chua co du lieu trong map
% Ghi chu: dau vao cua thuat toan nay la:
%   Ma tran chua thong tin Lack_v_data
%   Toa do cua cac o can phai dien them du lieu, trong hai arrays
%   col_Zero_v va row_Zero_v
tic

% Thuat toan chinh nam o day
Full_v_data = speedmap_fill(Lack_v_data, col_Zero_v, row_Zero_v, Level);

disp('Thoi gian chay thuat toan noi suy cho ca ban do: ')
toc

%test:
flat_Full_v_data=reshape(Full_v_data,1,Row_length*Col_length); % m(1,1) m(2,1)... m(N_row,1) m(1,2) m(2,2)...
[row_Zero_v_new,col_Zero_v_new]=find(not(flat_Full_v_data )); % hau nhu tat ca cac o deu phai khac Zero
disp('So o khong co du lieu SAU khi noi suy:');
length(row_Zero_v_new) %number of missing data cells
%figure; mesh(1:Col_length,1:Row_length,Full_v_data); %plot of the full map

% Compare the map before and after data filling

%figure;
%subplot(1,2,1); image([1,Col_length],[1,Row_length],Lack_v_data); title('Missing data'); colorbar;
%subplot(1,2,2); image([1,Col_length],[1,Row_length],Full_v_data); title('Filled data'); colorbar;

figure;
subplot(1,2,1); imagesc([1,Col_length],[1,Row_length],Lack_v_data); title('Missing data'); colorbar;
subplot(1,2,2); imagesc([1,Col_length],[1,Row_length],Full_v_data); title('Filled data'); colorbar;

% Plot the speed map with rescaled in 8 levels
Scale_v=Vmax*[1:8]/8;

Lack_Scale1 = Lack_v_data<Scale_v(1);
Lack_Scale2 = Lack_v_data>Scale_v(1) & Lack_v_data<Scale_v(2);
Lack_Scale3 = Lack_v_data>Scale_v(2) & Lack_v_data<Scale_v(3);
Lack_Scale4 = Lack_v_data>Scale_v(3) & Lack_v_data<Scale_v(4);
Lack_Scale5 = Lack_v_data>Scale_v(4) & Lack_v_data<Scale_v(5);
Lack_Scale6 = Lack_v_data>Scale_v(5) & Lack_v_data<Scale_v(6);
Lack_Scale7 = Lack_v_data>Scale_v(6) & Lack_v_data<Scale_v(7);
Lack_Scale8 = Lack_v_data>Scale_v(7) & Lack_v_data<Scale_v(8);
Rescale_Lack_v_data = Lack_Scale1*1 + Lack_Scale2*2 + Lack_Scale3*3 + Lack_Scale4*4 + Lack_Scale5*5 + Lack_Scale6*6 + Lack_Scale7*7 + Lack_Scale8*8;

Full_Scale1 = Full_v_data<Scale_v(1);
Full_Scale2 = Full_v_data>Scale_v(1) & Full_v_data<Scale_v(2);
Full_Scale3 = Full_v_data>Scale_v(2) & Full_v_data<Scale_v(3);
Full_Scale4 = Full_v_data>Scale_v(3) & Full_v_data<Scale_v(4);
Full_Scale5 = Full_v_data>Scale_v(4) & Full_v_data<Scale_v(5);
Full_Scale6 = Full_v_data>Scale_v(5) & Full_v_data<Scale_v(6);
Full_Scale7 = Full_v_data>Scale_v(6) & Full_v_data<Scale_v(7);
Full_Scale8 = Full_v_data>Scale_v(7) & Full_v_data<Scale_v(8);
Rescale_Full_v_data = Full_Scale1*1 + Full_Scale2*2 + Full_Scale3*3 + Full_Scale4*4 + Full_Scale5*5 + Full_Scale6*6 + Full_Scale7*7 + Full_Scale8*8;

figure;
subplot(1,2,1); imagesc([1,Col_length],[1,Row_length],Rescale_Lack_v_data); title('Rescaled missing data'); colorbar;
subplot(1,2,2); imagesc([1,Col_length],[1,Row_length],Rescale_Full_v_data); title('Rescaled filled data'); colorbar;
