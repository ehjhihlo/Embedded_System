
%%利用這個來畫比較圖

subplot(3,2,1);
plot(dataaccintense(:,1))
title("x axis in static")
xlabel("samples")
ylabel("g")

subplot(3,2,3);
plot(dataaccintense(:,2))
title("y axis in static")
xlabel("samples")
ylabel("g")

subplot(3,2,5);
plot(dataaccintense(:,3))
title("z axis in static")
xlabel("samples")
ylabel("g")

subplot(3,2,2);
plot(stm32outputaccxmovefir(:,2))
title("x axis of stm32 fir result")
xlabel("samples")
ylabel("g")

subplot(3,2,4);
plot(stm32outputaccymovefir(:,2))
title("y axis of stm32 fir result")
xlabel("samples")
ylabel("g")

subplot(3,2,6);
plot(stm32outputacczmovefir(:,2))
title("z axis of stm32 fir result")
xlabel("samples")
ylabel("g")



