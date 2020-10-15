import cv2
import sqlite3
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('C:/python-37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
def insertOrUpdate(Id,Name,Mood):

    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET NAME="+str(Name)+"WHERE ID="+str(Id)
        cmd="UPDATE People SET Mood="+str(Mood)+"WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO People(ID,Name,Mood) Values("+str(Id)+","+str(Name)+","+str(Mood)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id=input('enter your id')
name=input('enter name')
mood=input('enter mood')
insertOrUpdate(id,name,mood)

sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
        print(sampleNum)
        
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>300:
        break
cam.release()
cv2.destroyAllWindows()