fs = 100;  %%取樣頻率
N = 480;  %%取樣點數量
n = 0: N-1;
t = n/fs;
f = n*fs/N;


format long
b = fir1(28, 6/24);
format long
y = filter(b,1,moveAccZ); %%匯入原始資料進行轉換 "moveAccZ"可替換成任N*1的array
plot (t,y)  %%畫原始資料經fir filter 的濾波結果

format long
fid = fopen('ref.txt','wt'); %%將通過filter的資料存到ref中，可以再拿去當作refdata計算snr
fprintf(fid,'%g,\n',y);
fclose(fid);
