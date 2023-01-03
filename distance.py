'''
UART communication on Raspberry Pi using Pyhton
https://www.qutaojiao.com
'''
import serial
import time
#from subprocess import run
import subprocess    
import threading
from sendSound import sendSound
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-ip" , dest="ip" , default="192.168.0.23")
parser.add_argument("-p" , dest="port" , default="3000")

HTTP_server_ip = parser.parse_args().ip
HTTP_server_port = parser.parse_args().port

ser = serial.Serial ("/dev/ttyS0", 38400)    #Open port with baud rate'




dis = 0;
HTTP_Request = None
person_name = ""


while True:
	received_data = ser.read()              #read serial port
	time.sleep(0.1)
	data_left = ser.inWaiting()             #check for remaining byte
	received_data += ser.read(data_left)

	if float(received_data.decode()) < 0:
		continue
		
	
	    
	if dis > 50 and float(received_data.decode()) < 50:
		#sound = threading.Thread(target =sendSound, args = (ser,))
		#sound.start()
		
		
		with open('face_record.txt') as f:
			person_name = f.readline()
		print(person_name)	
		if person_name != "other":
			HTTP_Request = subprocess.Popen(["python" , "HTTP_get.py" , "-ip" , HTTP_server_ip , "-p" , HTTP_server_port , "--N" , person_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    
	if HTTP_Request!= None and HTTP_Request.poll() != None:
		output, err = HTTP_Request.communicate()
		print("Send ACK: ",output.decode())
		print(err)
		
		if(output.decode() == "OK Yes"):
			sendSound([2,5,1,0,3])
		
		
		HTTP_Request = None
        
	dis = float(received_data.decode())
        
	print (received_data.decode())                   #print received data
		

