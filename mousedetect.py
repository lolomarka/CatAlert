import time 
import mouse
import cv2
import shutil
import datetime as dt
import os 
import playsound
from pygame import mixer
mouseMoved = False
pos = mouse.get_position()
catTracked = False
while not catTracked:
    while not mouseMoved:
        bufPos = mouse.get_position()
        if(bufPos != pos):
            mouseMoved = True

    now = dt.datetime.now()
    print("Mouse was moved")
    # Включаем первую камеру
    cap = cv2.VideoCapture(0)

    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(30):
        cap.read()

    # Делаем снимок    
    ret, frame = cap.read()

    # Записываем в файл
    cv2.imwrite('photo.png', frame)   

    # Отключаем камеру
    cap.release()

    face_cascade=cv2.CascadeClassifier("cat_face.xml")

    img=cv2.imread("photo.png")

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.01,minNeighbors=5)
    if(len(faces) > 0):
        mixer.init()
        mixer.music.load('alert.mp3')
        mixer.music.play()
        catTracked = True
        for x,y,w,h in faces:
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #playsound.playsound('bkb.mp3')
        cv2.imshow("cat face",img)
        cv2.waitKey()
        srcfold = str(os.path.dirname(__file__))
        src = srcfold + '\\photo.png'
        dst = srcfold+'\\archive\\cat-alert'+str(now.hour)+'-'+str(now.minute) + "-" + str(now.second)+'.png'
        shutil.copy(src, dst) 
    else:
        srcfold = str(os.path.dirname(__file__))
        src = srcfold + '\\photo.png'
        dst = srcfold+'\\archive\\photo'+str(now.hour)+'-'+str(now.minute) + "-" + str(now.second)+'.png'
        shutil.copyfile(src, dst)       
        mouseMoved = False  
        pos = mouse.get_position()

    #print(type(faces))
    #print(faces)
    
    


print("Тебя заскамили, смотри ищи себя в прошмандовках и азербайджана")