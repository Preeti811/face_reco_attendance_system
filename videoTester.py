import os
import cv2
import numpy as np
import faceRecognition as fr

#This module captures images via webcamera and performs face recognition
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:\\Users\\PREETI\\Desktop\\faceimage_database\\trainingData.yml')#Load saved training data

#open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, test_img=cap.read()# captures frame and returns boolean value and captured image
    faces_detected, gray_img = fr.faceDetection(test_img)

    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w, x:x+h]
        #perform face recognition
        label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
        print("confidence:",confidence)
        print("label:",label)
        #draw rectangle around the detected face
        fr.draw_rect(test_img,face)
        predicted_name=str(label)
        if confidence <70:#If confidence less than 37 then don't print predicted face text on screen
           fr.put_text(test_img,predicted_name,x,y)


    resized_img = cv2.resize(test_img, (1000, 600))
    cv2.imshow('face recognition tutorial ',resized_img)
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break

#releases camera
cap.release()
cv2.destroyAllWindows #properly close OpenCV windows

