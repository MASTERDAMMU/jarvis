import cv2,os
import numpy as np
import image
import pickle
import sqlite3

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "C:/python-37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'dataSet'


def getProfile(id):
    conn=sqlite3.connect("FaceBase.db")
    con=conn.cursor()

    cmd="SELECT * FROM People WHERE ID="+str(id)
    con.execute(cmd)
    rows=con.fetchall()
    profile=None
    for row in rows:
        profile=row
        print(row)
    conn.close()
    return profile

cam = cv2.VideoCapture('http://25.89.171.185:8080/video')
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        id, conf=recognizer.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile != None):
            print(profile[1])
            cv2.putText(im,str(profile[1]), (x,y+h+30),font,0.55,(0,255,0),1)
            cv2.putText(im,str(profile[2]), (x,y+h+60),font,0.55,(0,255,0),1)
    cv2.imshow('im',im) 
    cv2.waitKey(10)
      