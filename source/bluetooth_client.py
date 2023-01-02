from bluedot.btcomm import BluetoothClient
from signal import pause
from argparse import ArgumentParser
import time

parser = ArgumentParser()
parser.add_argument("-message" , "--M" , dest="msg" , default="test")


msg = parser.parse_args().msg

is_end = False

def data_recv(data):
    print(data)
    global is_end 
    is_end  = True
    

c = BluetoothClient("E4:5F:01:A4:31:44", data_recv)
c.send(msg)

#pause()

while not is_end:
    #print(is_end)
    time.sleep(0.1)
    


