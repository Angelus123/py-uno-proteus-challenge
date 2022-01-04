from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector
import cv2
import serial
import datetime

datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
print(datetime.datetime.now())
import time

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
global cap
cap = cv2.VideoCapture(0)

def popupmsg():

    msg="Pictures of gesture to commmunicate"
    global ws
    ws.quit()
    print("Hello")
    ws.destroy()
    global popup
    popup = Tk()
    #Create a canvas
    
    popup.geometry('700x500')
    popup.wm_title("!")
    label = Label(popup, text=msg, font="bold, 18", pady=20, anchor="center")
    label.pack(pady=10)
    can= Canvas(popup, width= 500, height= 300)
    can.pack()


    img2= ImageTk.PhotoImage(Image.open("gesture_one.png"))
    #Add image to the Canvas Items
    can.create_image(30,30,anchor=NW,image=img2)
 
    B1 = Button(popup, text="NEXT", bg="green", pady=5, width=8, command = continue_with)
    B1.pack()
    popup.mainloop(

    )
def stop_cam():
    print('exit')
    cap.release() 
    plt.show()
   
def continue_with():
    popup.quit()
    popup.destroy()
    root = Tk()
    root.geometry("0x0")
    canva= Canvas(root, width= 0, height= 0)
    canva.pack()

    #Load an image in the script
    img= ImageTk.PhotoImage(Image.open("gesture.jpg"))

    #Add image to the Canvas Items
    canva.create_image(10,10,anchor=NW,image=img)
    
    w = Label(root, text ='A mute smart Ward', font = "50") 
    w.pack()
    messagebox.showinfo(title="showinfo", message="Wow Now u are good to go, camera will stay turn on to easy")
    arduino = serial.Serial('COM4', 9600)
    time.sleep(2)

    

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
                messagebox.showinfo(title="showinfo", message="Message sent to doctor")
            if fingers1 == [0,1,1,0,0] and faceScore[0]>0.50 : 
                arduino.write(b'c')
                print(f'Cleaner')
                time.sleep(5) # Sleep for 5 seconds
                messagebox.showinfo(title="showinfo", message="Message sent to Cleaner")
            if fingers1 == [1,1,1,0,0]and faceScore[0]>0.57 :
                print(f'Restaurent') 
                arduino.write(b'r')
                time.sleep(5) # Sleep for 5 seconds
                messagebox.showinfo(title="showinfo", message="Message sent to Restaurent")

        cv2.imshow("Image", img)
        cv2.waitKey(1)
    
#create window object
ws = Tk()
ws.title('A mute Smart Ward')
ws.geometry('750x600')

#Create a canvas
canvas= Canvas(ws, width= 471, height= 300)
canvas.pack()
#Load an image in the script
img= ImageTk.PhotoImage(Image.open("gesture_two.jpg"))
#Add image to the Canvas Items
canvas.create_image(10,10,anchor=NW,image=img)
canvas.grid(row=0,column=0,sticky="NW")

ws.config(height=700, width=700)
welcome_label=Label(ws, text="Welcome to smart ward", font="bold, 36", pady=50, padx=20)
welcome_label.grid(row=2,column=5)
f = Frame(ws,bg="green",width=50,height=50)
canvas.grid(row=0,column=5,sticky="NW")
f.grid_propagate(0)
f.update()
l = Label(f,text="123",bg="gray")
l.place(x=25, y=25, anchor="center")
add_btn=Button(ws, text="NEXT", bg="green", command=popupmsg, pady=5, width=8)
add_btn.grid(row=3, column=4, padx=30, pady=10)
ws.mainloop()



