from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
from bluepy import btle

class NewDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, handle, data):
        print(f"Notification, handle: {handle}, data:{data}")


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

n=0
addr = []

for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    addr.append(dev.addr)
    n += 1
    for (adtype, desc, value) in dev.getScanData():
        print (" %s = %s" % (desc, value))



number = input('Enter your device number: ')
print ('Device', number)
num = int(number)
print (addr[num])
#

print ("Connecting...")
dev = Peripheral(addr[num], 'random')
#
print ("Services...")
for svc in dev.services:
    print (str(svc))
#

try:
    testService = dev.getServiceByUUID(UUID(0xfff0))
    #des = dev.getDescriptors()
    #print(des)
    for ch in testService.getCharacteristics():
        print (str(ch))



    characteristics = testService.getCharacteristics()
    notify_char = characteristics[0]
    hecg = notify_char.getHandle()

    for des in dev.getDescriptors(hecg, testService.hndEnd):
        if (des.uuid == 0x2902):
            print(f'Client Characteristic Configuration found at handle 0x{format(des.handle,"02X")}')
            hEcgCCC=des.handle

    dev.writeCharacteristic(hEcgCCC,bytes([1, 0]))


    for ch in dev.getCharacteristics(uuid=UUID(0xfff4)):
        # ch.write('52399254'.encode('utf-8'))
        dev.setDelegate(NewDelegate())

    print("writing done")
    while True:
        if dev.waitForNotifications(1.0):
            #ch.write('44444'.encode('utf-8'))
            # handleNotification() was called
            print("write notify")
            #ch = dev.getCharacteristics(uuid=UUID(0xfff4))[0]
            #if (ch.supportsRead()):
            #print(ch.read())
            continue
        print("waiting")

finally:
    dev.disconnect() 