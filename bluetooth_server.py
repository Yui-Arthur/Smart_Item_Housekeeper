from bluedot.btcomm import BluetoothServer
from signal import pause
import time
import subprocess    
import threading
import pickle
from sendSound import sendSound


def data_received(data):
    print(data)
    sendSound([6,0,6,0])
    subprocess.Popen(["python" , "./FaceRecognize_yolov5_Facenet_svm/logIn_usr.py" , "--root" , "./FaceRecognize_yolov5_Facenet_svm" , "--label" , data , "--num" , "4"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    

s = BluetoothServer(data_received)
sendSound([6,0,6,0])
with open("./FaceRecognize_yolov5_Facenet_svm/SVCmodel.pkl",'rb') as f:
        SVCmodel ,class_name = pickle.load(f)
        print(class_name)
    
pause()
