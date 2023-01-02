python distance.py &
python bluetooth_server.py &
cd FaceRecognize_yolov5_Facenet_svm
python ./yolov5/face_detect.py --source 1 --weights ./yolov5/best-int8_edgetpu.tflite --svc ./SVCmodel.pkl --imgsz 160 --data ./dataset.yaml --save ../face_record.txt &
