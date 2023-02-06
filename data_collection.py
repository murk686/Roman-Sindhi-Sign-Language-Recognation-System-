from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time


class Data_collection:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1390x768+0+0")

        self.root.title("Data_collection")

        img = Image.open("images/img_4.png")
        img = img.resize((866, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image
        bg1 = Image.open("images/bg1.jpg")
        bg1 = bg1.resize((1366, 488), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=550)

        # title section
        title_lb1 = Label(bg_img, text="Sign language Recognition System ", font=("verdana", 30, "bold"),
                          bg="black", fg="white")
        title_lb1.place(x=0, y=0, width=1366, height=50)





        cap = cv2.VideoCapture(0)
        detector = HandDetector(maxHands=1)

        offset = 20
        imgSize = 300

        folder = "ssl dataset/daal"
        counter = 0

        while True:
            success, img = cap.read()
            hands, img = detector.findHands(img)
            if hands:
                hand = hands[0]
                x, y, w, h = hand['bbox']

                imgwhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

                imgCropShape = imgCrop.shape

                aspectRatio = h / w

                if aspectRatio > 1:
                    k = imgSize / h
                    wCal = math.ceil(k * w)
                    imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                    imgResizeShape = imgResize.shape
                    wGap = math.ceil((imgSize - wCal) / 2)
                    imgwhite[:, wGap:wCal + wGap] = imgResize

                else:
                    k = imgSize / w
                    hCal = math.ceil(k * h)
                    imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                    imgResizeShape = imgResize.shape
                    hGap = math.ceil((imgSize - hCal) / 2)
                    imgwhite[hGap:hCal + hGap, :] = imgResize

                cv2.imshow("ImageCrop", imgCrop)
                cv2.imshow("ImageWhite", imgwhite)

            cv2.imshow("Image", img)
            key = cv2.waitKey(1)
            if key == ord("s"):
                counter += 1
                cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgwhite)
                print(counter)


if __name__ == "__main__":
        root = Tk()
        obj = Data_collection(root)
        root.mainloop()