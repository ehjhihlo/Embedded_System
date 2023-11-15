# HW-7: Mbed-DSP programming
### 執行步驟
1. 執行main_collect_data.cpp，蒐集stm32 xyz三軸加速度的資料，stm32開發版靜止以及移動兩種狀態各收集一次。
2. 將上述步驟收集到的加速度資料，丟入arm_fir_data.c的testInput_f32_1kHz_15kHz陣列
3. matlab執行firPlot.m，丟入步驟1蒐集到的加速度資料，過filter
4. 把matlab執行結果，丟入arm_fir_data.c的refOutput陣列
5. 把本repo的main.cpp取代原本的main.cpp
6. 執行main.cpp，將filter過後的testOutput資料畫圖
7. 算出snr，以比較在STM32上filter過後(testOutput)和在matlab上filter過後(refOutput)的相似程度
