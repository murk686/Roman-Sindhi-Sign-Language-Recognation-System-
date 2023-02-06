import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start
        # first header image
        img=Image.open("images/img_30.png")
        img=img.resize((1166,110),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self. photoimg)
        f_lb1.place(x=0,y=0,width=1266,height=130)

        # backgorund image
        bg1=Image.open("images/bg1.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("verdana",30,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # developer button
        dev1_img_btn=Image.open("images\dev_suprvisor.png")
        dev1_img_btn=dev1_img_btn.resize((250,250),Image.ANTIALIAS)
        self.dev1_img1=ImageTk.PhotoImage(dev1_img_btn)

        dev1_b1 = Button(bg_img,image=self.dev1_img1,cursor="hand2")
        dev1_b1.place(x=80,y=150,width=260,height=250)

        dev1_b1_1 = Button(bg_img,text="Supervisor Sir M.Khalid Sheikh",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="navyblue")
        dev1_b1_1.place(x=80,y=380,width=260,height=50)



         # developer  button
        dev2_img_btn=Image.open("images\devv.jpg")
        dev2_img_btn=dev2_img_btn.resize((180,200),Image.ANTIALIAS)
        self.dev2_img1=ImageTk.PhotoImage(dev2_img_btn)

        dev2_b2 = Button(bg_img,image=self.dev2_img1,cursor="hand2",)
        dev2_b2.place(x=810,y=90,width=200,height=200)

        dev2_b2_1 = Button(bg_img,text="Murk Channa",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        dev2_b2_1.place(x=810,y=270,width=200,height=35)

        # Devloper  button
        dev3_img_btn = Image.open("images\devv2.jpg")
        dev3_img_btn = dev3_img_btn.resize((180, 200), Image.ANTIALIAS)
        self.dev3_img2 = ImageTk.PhotoImage(dev3_img_btn)

        dev3_b3 = Button(bg_img, image=self.dev3_img2, cursor="hand2", )
        dev3_b3.place(x=600, y=220, width=200, height=200)

        dev3_b3_1 = Button(bg_img, text="Seema Channa", cursor="hand2", font=("tahoma", 15, "bold"), bg="white",
                          fg="navyblue")
        dev3_b3_1.place(x=600, y=410, width=200, height=35)

        # Developer
        dev4_img_btn = Image.open("images\dev4.png")
        dev4_img_btn = dev4_img_btn.resize((180, 200), Image.ANTIALIAS)
        self.dev4_img1 = ImageTk.PhotoImage(dev4_img_btn)

        dev4_b1 = Button(bg_img, image=self.dev4_img1, cursor="hand2", )
        dev4_b1.place(x=1020, y=220, width=200, height=200)

        dev4_b1_1 = Button(bg_img, text="Manzar Hussain", cursor="hand2", font=("tahoma", 15, "bold"), bg="white",
                          fg="navyblue")
        dev4_b1_1.place(x=1020, y=410, width=200, height=35)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()