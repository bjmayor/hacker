from bluetooth import *
'''
can't run in mac os . connect throw exception: depythonifying 'pointer', got 'tuple'
'''
def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr,port))
        print('[+] RFCOMM Port ' + str(port) + ' open')
        sock.close()
    except Exception as e:
        print('[-] RFCOMM Port ' + str(port) + ' closed')

for port in range(1, 30):
    rfcommCon('80:EA:96:8E:69:A7', port)