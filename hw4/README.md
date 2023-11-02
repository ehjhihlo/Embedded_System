# 執行步驟
1. 在Mbed Studio創建一個empty project，並刪掉原本的main.cpp
2. 下載ble程式 [https://github.com/ARMmbed/mbed-os-example-ble]，並將BLE_GattServer_AddService的資料夾放進去empty project裡面
3. 依照投影片修改mbed_add.json檔
4. 在樹莓派上下載本repo
5. 把本repo的main.cpp取代原本的main.cpp，並complie整個project
6. 把本repo的ble_scan_connect.py丟到樹莓派上面
7. 執行mbed studio，開始advertise
8. 執行ble_scan_connect.py，找到stm32的device(local name=EnJhih)，連上後即可接收從STM32傳來之magneto x, y, z的資料
