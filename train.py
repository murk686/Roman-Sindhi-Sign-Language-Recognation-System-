from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

class train:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1390x768+0+0")

        self.root.title("Train")

        # This part is image labels setting start
        # first header image
        img = Image.open("images\img_2.png")
        img = img.resize((1066, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image
        bg1 = Image.open("images/bg.jpg")
        bg1 = bg1.resize((1366, 488), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=550)

        # title section
        title_lb1 = Label(bg_img, text="Sign Detection ", font=("verdana", 30, "bold"),
                          bg="black", fg="white")
        title_lb1.place(x=0, y=0, width=1366, height=50)



        cap = cv2.VideoCapture(0)
        detector = HandDetector(maxHands=1)
        classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

        offset = 20
        imgSize = 300

        folder = "ssl dataset/Alaf"
        counter = 0

        labels = ["Alaf", "Bae", "Jeem", "Swaad", "Tua", "Daal", "Laam", "Meem", "Gea", "Khe"]

        while True:
            success, img = cap.read()
            imgOutput = img.copy()
            hands, img = detector.findHands(img)
            if hands:
                hand = hands[0]
                x, y, w, h = hand['bbox']

                imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

                imgCropShape = imgCrop.shape

                aspectRatio = h / w

                if aspectRatio > 1:
                    k = imgSize / h
                    wCal = math.ceil(k * w)
                    imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                    imgResizeShape = imgResize.shape
                    wGap = math.ceil((imgSize - wCal) / 2)
                    imgWhite[:, wGap:wCal + wGap] = imgResize
                    prediction, index = classifier.getPrediction(imgWhite, draw=False)
                    print(prediction, index)

                else:
                    k = imgSize / w
                    hCal = math.ceil(k * h)
                    imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                    imgResizeShape = imgResize.shape
                    hGap = math.ceil((imgSize - hCal) / 2)
                    imgWhite[hGap:hCal + hGap, :] = imgResize
                    prediction, index = classifier.getPrediction(imgWhite, draw=False)

                cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                              (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
                cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
                cv2.rectangle(imgOutput, (x - offset, y - offset),
                              (x + w + offset, y + h + offset), (255, 0, 255), 4)

                cv2.imshow("ImageCrop", imgCrop)
                cv2.imshow("ImageWhite", imgWhite)

            cv2.imshow("Image", imgOutput)
            cv2.waitKey(1)


if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()