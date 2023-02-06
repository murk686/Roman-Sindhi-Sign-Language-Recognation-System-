from tkinter import*
from PIL import Image,ImageTk
from data_collection import Data_collection

class Dataset:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1390x768+0+0")

        self.root.title("Dataset")

        img = Image.open("images\img_4.png")
        img = img.resize((866, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image
        bg1 = Image.open("images/img_14.jpg")
        bg1 = bg1.resize((1366, 488), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=550)

        # title section
        title_lb1 = Label(bg_img, text="Dataset Collection Panel ", font=("verdana", 30, "bold"),
                          bg="black", fg="white")
        title_lb1.place(x=0, y=0, width=1366, height=50)

        # student button 1
        std_img_btn = Image.open("images/img_12.png")
        std_img_btn = std_img_btn.resize((250, 250), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img ,command=self.data_collection,image=self.std_img1, cursor="hand2")
        std_b1.place(x=440, y=180, width=280, height=220)

        std_b1_1 = Button(bg_img, command=self.data_collection,text="Create Dataset", cursor="hand2",
        font=("tahoma", 15, "bold"), bg="#ffcc44", fg="navyblue",bd=5, justify="left", padx=2, pady=2,relief="sunken")
        std_b1_1.place(x=440, y=370, width=280, height=55)

    def data_collection(self):
        self.new_window = Toplevel(self.root)
        self.app = Data_collection(self.new_window)

if __name__ == "__main__":
        root = Tk()
        obj = Dataset(root)
        root.mainloop()