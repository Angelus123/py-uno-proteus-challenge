from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector
import cv2
import serial
import datetime
datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
print(datetime.datetime.now())
import time

arduino = serial.Serial('COM4', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon =0.8, maxHands=1)
faceDetector = FaceDetector()
while True:
    # Get image frame
    success, img = cap.read()

    # Find hand and its
    hands, image =detector.findHands(img)

    img, bboxs = faceDetector.findFaces(img)
    # hands = detector.findHands(img, draw =True)  # without draw
    if hands and bboxs:

    # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right
        fingers1 = detector.fingersUp(hand1)


        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        print(f'{bboxs[0]["score"]}') 
        cv2.circle(img, center, 5, ( 255, 0, 255), cv2.FILLED )
        faceScore =  bboxs[0]["score"]

        print(f'Finger Array {fingers1}, Face Score {faceScore[0]}') 
        if fingers1 == [0,1,0,0,0] and faceScore[0]>0.50 :
            arduino.write(b'd')
            print(f'Doctor') 
            time.sleep(5) # Sleep for 5 seconds
        if fingers1 == [0,1,1,0,0] and faceScore[0]>0.50 : 
            arduino.write(b'c')
            print(f'Cleaner')
            time.sleep(2) # Sleep for 5 seconds
            time.sleep(5) # Sleep for 5 seconds
        if fingers1 == [1,1,1,0,0]and faceScore[0]>0.57 :
            print(f'Restaurent') 
            arduino.write(b'r')
            time.sleep(2) # Sleep for 5 seconds

    cv2.imshow("Image", img)
    cv2.waitKey(1)