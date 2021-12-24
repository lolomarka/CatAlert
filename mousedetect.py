import mouse
import cv2
import datetime as dt
import os
import time
from pygame import mixer

#Возвращает платформанезависемый путь к файлу в папке проекта
def getPIPath(*args):
    root = os.getcwd()
    for string in args:
        root = os.path.join(root, string)
    #print(root) //debug
    return root

# Делает снимок с подключённой камеры
def getPhoto():
        # Включаем камеру
        cap = cv2.VideoCapture(0)
        # "Прогреваем" камеру, чтобы снимок не был тёмным
        for i in range(15):
            cap.read()
        # Делаем снимок    
        ret,frame = cap.read()
        # Отключаем камеру
        cap.release()
        return frame

# Анализирует фото на наличие кошки
def analysePhoto(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.01,minNeighbors=5)
    
    return faces,len(faces) > 0
    
def alert(frame,faces,now):
    mixer.init()
    mixer.music.load(getPIPath("alert.mp3"))
    mixer.music.play()
    catTracked = True
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Alert",frame)
    cv2.waitKey()
    pictureName = str(now) + ".png"
    cv2.imwrite(getPIPath("Archive","Alert",pictureName),frame) 

def restoreAfterFakeAlert(frame,now):
    mouseMoved = False
    pictureName = str(now) + ".png"
    cv2.imwrite(getPIPath("Archive","FakeAlert",pictureName),frame) 

#инициализация
face_cascade=cv2.CascadeClassifier(getPIPath("cat_face.xml"))
pos = mouse.get_position()
mouseMoved = False
#Основной цикл
while True:
    # Проверяем триггер на срабатывание
    while not mouseMoved:
        bufPos = mouse.get_position()
        if(bufPos != pos):
            mouseMoved = True
    # Дата+время
    now = dt.datetime.now()
    print(str(now) + " : триггер сработал. Проверяем...")
    
    frame = getPhoto()
    #Проверяем, сделан ли был снимок
    if(not frame.any()):
        print("Камера не обнаружена, программа прекращает работу.")
        break
    # Записываем в файл
    cv2.imwrite(getPIPath("LastPhoto.png"), frame)
    faces,catDetected = analysePhoto(frame)
    if(catDetected):
        print(str(now) + " : Кошачий обнаружен! Принимаются меры.")
        alert(frame,faces,now)
    else:
        print(str(now) + " : Ложное срабатывание.")
        restoreAfterFakeAlert(frame,now)
    print("Программа вернётся в исходное положение через 15 сек...")
    time.sleep(15)
    pos = mouse.get_position()
