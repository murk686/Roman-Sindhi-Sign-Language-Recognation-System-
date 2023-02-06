import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from classifier import Classifier
from dataset import Dataset

class Execution:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1390x768+0+0")

        self.root.title("Sign_Recogonition_System")

        # This part is image labels setting start
        # first header image
        img = Image.open("images\img_2.png")
        img = img.resize((1066, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1466, height=150)

        # img
        logo_btn = Image.open("images\img_26.png")
        logo_btn = logo_btn.resize((194, 120), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(logo_btn)
        logo_b1 = Button(f_lb1, image=self.photoimg1, cursor="hand2", )
        logo_b1.place(x=10, y=5, width=191, height=120)

        # backgorund image
        bg1 = Image.open("images/bg1.jpg")
        bg1 = bg1.resize((1366, 488), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=550)

        # title section
        title_lb1 = Label(bg_img, text="DASHBOARD ", font=("Century", 30, "bold"),
                          bg="sandybrown", fg="black")
        title_lb1.place(x=0, y=0, width=1366, height=50)

        7  # ------------classifier  button
        classifier_img_btn = Image.open("images/img_5.png")
        classifier_img_btn = classifier_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.classifier_img1 = ImageTk.PhotoImage(classifier_img_btn)

        classifier_b1 = Button(bg_img, command=self.classifier, image=self.classifier_img1, cursor="hand2", )
        classifier_b1.place(x=740, y=90, width=220, height=200)

        classifier_b1_1 = Button(bg_img, command=self.classifier, text="Classifier", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="#ffcc44", fg="navyblue",bd=5, justify="left", padx=2, pady=2,relief="sunken")
        classifier_b1_1.place(x=740, y=292, width=220, height=53)

    #----------------dataset button -----------------
        dataset_img_btn = Image.open("images\img_8.png")
        dataset_img_btn = dataset_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.dataset_img1 = ImageTk.PhotoImage(dataset_img_btn)

        dataset_b1 = Button(bg_img, command=self.dataset, image=self.dataset_img1, cursor="hand2", )
        dataset_b1.place(x=410, y=90, width=220, height=200)

        dataset_b1_1 = Button(bg_img, command=self.dataset, text="Dataset", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="#ffcc44", fg="navyblue",bd=5, justify="left", padx=2, pady=2,relief="sunken")
        dataset_b1_1.place(x=410, y=292, width=220, height=53)
    def classifier(self):
        self.new_window = Toplevel(self.root)
        self.app = Classifier(self.new_window)

    def dataset(self):
        self.new_window = Toplevel(self.root)
        self.app =Dataset(self.new_window)

if __name__ == "__main__":
        root = Tk()
        obj = Execution(root)
        root.mainloop()