import cv2
import os
import time
import Hand_Tracking_Module as htm
import serial #Serial imported for Serial communication
import time #Required to use delay functions

ArduinoSerial = serial.Serial('com5',9600)
time.sleep(2)
# print(ArduinoSerial.readline())

def getNumber(ar):
    s=""
    for i in ar:
       s+=str(ar[i]);
    if(s=="00000"):
        print('0')
        ArduinoSerial.write(b'0') #sent 0
        return (0)
    elif(s=="01000"):
        print('1')
        ArduinoSerial.write(b'1') #sent 1
        return(1)
    elif(s=="01100"):
        ArduinoSerial.write(b'2') #sent 2
        print('2')
        return(2) 
    elif(s=="01110"):
        ArduinoSerial.write(b'3') #sent 3
        print('3')
        return(3)
    elif(s=="01111"):
        ArduinoSerial.write(b'4') #sent 4
        print('4')
        return(4)
    elif(s=="11111"):
        ArduinoSerial.write(b'5') #sent 5
        print('5')
        return(5)      
 
wcam,hcam=640,480
cap=cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
pTime=0
detector = htm.handDetector(detectionCon=0.75)

while True:
    success,img=cap.read()
    img = detector.findHands(img, draw=True )
    lmList, bbox = detector.findPosition(img, draw=False)
    #print(lmList)
    tipId=[4,8,12,16,20]
    if(len(lmList)!=0):
        fingers=[]
        #thumb
        if(lmList[tipId[0]][1]>lmList[tipId[0]-1][1]):
            fingers.append(1)
        else :
            fingers.append(0)
            #4 fingers
        for id in range(1,len(tipId)):   
            if(lmList[tipId[id]][2]<lmList[tipId[id]-2][2]):
                fingers.append(1)
            else :
                fingers.append(0)

        cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)   
        cv2.putText(img,str(getNumber(fingers)),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),20)  
        
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),3)
    cv2.imshow("image",img)
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break




































