import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from classifier import Classifier
from dataset import Dataset
from developer import Developer
from execute import Execution

import os

class Sign_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1390x768+0+0")

        self.root.title("Sign_Recogonition_System")

        # This part is image labels setting start

        # first header image
        img = Image.open("images\img_2.png")
        img = img.resize((1066, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        # set image as lablel
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1466, height=150)

        #img
        logo_btn = Image.open("images\img_26.png")
        logo_btn = logo_btn.resize((184, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(logo_btn)
        logo_b1 = Button(f_lb1, image=self.photoimg1, cursor="hand2", )
        logo_b1.place(x=10, y=5, width=191, height=120)

        # backgorund image
        bg1 = Image.open("images/bg2.jpg")
        bg1 = bg1.resize((1366, 508), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as labl
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=550)

        # title section
        title_lb1 = Label(bg_img, text="Roman Sindhi Sign language Recognition System ", font=("Century", 28, "bold"),
                          bg="sandybrown", fg="black")
        title_lb1.place(x=0, y=0, width=1366, height=44)

        # -----------------gif imaeg--------------

        gifImage = "images/handgesture13.gif"
        openImage = Image.open(gifImage)
       # gifImage = gifImage.resize((480, 420), Image.ANTIALIAS)


        frames = openImage.n_frames
        imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]

        count = 0

        showAnimation = None

        def animation(count):
            global showAnimation
            newImage = imageObject[count]

            gif_Label.configure(image=newImage)
            count += 1
            if count == frames:
                count = 0
            showAnimations = bg_img.after(190, lambda: animation(count))

        gif_Label = Label(bg_img, image="")
        gif_Label.place(x=40, y=55, width=430, height=450)

        animation(count)

        # Developers   button
        dev_img_btn = Image.open("images\img_9.png")
        dev_img_btn = dev_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img, command=self.developer, image=self.dev_img1, cursor="hand2", )
        dev_b1.place(x=710, y=200, width=180, height=180)

        dev_b1_1 = Button(bg_img, command=self.developer, text="Developers", cursor="hand2", font=("tahoma", 15, "bold"),
                          highlightbackground='red',highlightthickness='1',bg="#ffcc44", fg="navyblue",bd=5, justify="left", padx=2, pady=2,relief="sunken")
        dev_b1_1.place(x=710, y=383, width=180, height=45)

        # execution   button
        exi_img_btn = Image.open("images\img_27.png")
        exi_img_btn = exi_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.execute, image=self.exi_img1, cursor="hand2" )
        exi_b1.place(x=940, y=200, width=180, height=180)

        exi_b1_1 = Button(bg_img,command=self.execute, text="Execution", cursor="hand2", font=("tahoma", 15, "bold"),
                          highlightbackground='red',highlightthickness='1',bg="#ffcc44", fg="navyblue",bd=5, justify="left", padx=15, pady=15,relief="sunken")
        exi_b1_1.place(x=940, y=382, width=180, height=45)

        # ----------------------back button---------------------


    def execute(self):
        self.new_window = Toplevel(self.root)
        self.app =Execution(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)


if __name__ == "__main__":
        root = Tk()
        obj = Sign_Recognition_System(root)
        root.mainloop()
