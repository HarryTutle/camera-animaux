import numpy as np
import cv2
import tensorflow.lite as tflite
from picamera2 import Picamera2
from matplotlib import pyplot as plt
import time
import RPi.GPIO as GPIO
import os

chemin_usb='/media/harrytutle/PHILIPS UFD/photos/'
#numero_photo=0

""" BOUTON GPIO"""

GPIO.setmode(GPIO.BCM)
BUTTON_ALARM = 16
BUTTON_PIN = 22
GPIO.setup(BUTTON_ALARM, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


interpreter = tflite.Interpreter(model_path="/home/harrytutle/Desktop/ia_animaux/model_mobilenet_220625_2.tflite")
interpreter.allocate_tensors()
'''
debug=interpreter.get_input_details()
'''
picam2 = Picamera2()
picam2.preview_configuration.main.size=(640, 480)
picam2.preview_configuration.main.format='RGB888'
picam2.preview_configuration.controls.FrameDurationLimits=(1000000,1000000)
picam2.configure("preview")
picam2.start()
time.sleep(2)

while True:
    
    image = picam2.capture_array()
    frame=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    new_frame=cv2.resize(frame, (224,224))
    
    new_frame = new_frame.astype(np.float32) / 255.0
    input_data = np.expand_dims(new_frame, axis=0)
    #input_data = np.expand_dims(input_data, axis=-1)
    #print(input_data.shape)
    #print(np.mean(new_gray_frame))
    #print(np.std(new_gray_frame))
    #cv2.imshow("camcam", new_gray_frame)
    
    
    input_index = interpreter.get_input_details()[0]['index']
    output_index = interpreter.get_output_details()[0]['index']
    interpreter.set_tensor(input_index, input_data)
    interpreter.invoke()
    output = interpreter.get_tensor(output_index)
    
    timer=time.strftime("%Y-%m-%d-%H-%M-%S")
    print("Résultat de la prédiction :", output)
    print(timer)
    if output[0][1]>0.5:
        #numero_photo+=1
        cv2.imwrite(chemin_usb + timer + ".jpg" , frame)
        GPIO.output(BUTTON_ALARM, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(BUTTON_ALARM, GPIO.LOW)
        
    elif (output[0][2]>0.5) or (output[0][3]>0.5):
        #numero_photo+=1
        cv2.imwrite(chemin_usb + timer + ".jpg" , frame)
        time.sleep(3)
        
    else:
        pass
    
    
    if GPIO.input(BUTTON_PIN)==1:
        break




picam2.stop()
os.system("sudo shutdown now")