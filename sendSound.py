
import time
import serial


def sendSound(order , filePath=None):
	ser = serial.Serial ("/dev/ttyS0", 38400)    #Open port with baud rate'
	if filePath == None:
		BassTab = [1911,1702,1516,1431,1275,1136,1012]
   
	for i in BassTab:
		data = i.to_bytes(2, byteorder='big')
		ser.write(data)
		time.sleep(0.01)
		
	data = len(order).to_bytes(1, byteorder='big')
	ser.write(data)
	print(len(order))
	time.sleep(0.01)
	
	for i in order:	
		data = i.to_bytes(1, byteorder='big')
		ser.write(data)
		time.sleep(0.01)
		
	ser.close()
		
		
