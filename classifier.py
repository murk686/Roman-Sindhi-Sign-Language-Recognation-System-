from tkinter import*
from PIL import Image,ImageTk
from train import train

class Classifier:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1390x768+0+0")

        self.root.title("classifier")

        img = Image.open("images\img_4.png")
        img = img.resize((866, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image
        bg1 = Image.open("images/img_15.jpg")
        bg1 = bg1.resize((1366, 488), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=550)

        # title section
        title_lb1 = Label(bg_img, text="Sign Detection Panel ", font=("Century", 30, "bold"),
                          bg="black", fg="white")
        title_lb1.place(x=0, y=0, width=1366, height=50)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # character button 1
        char_img_btn = Image.open("images/img_5.png")
        char_img_btn = char_img_btn.resize((250, 180), Image.ANTIALIAS)
        self.char_img1 = ImageTk.PhotoImage(char_img_btn)

        char_b1 = Button(bg_img,command=self.train, image=self.char_img1, cursor="hand2")
        char_b1.place(x=250, y=100, width=250, height=180)

        char_b1_1 = Button(bg_img,command=self.train, text="character", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="#ffcc44", fg="navyblue",bd=5, justify="left", padx=2, pady=2,relief="sunken")
        char_b1_1.place(x=250, y=280, width=250, height=45)

        # Word button 2
        word_img_btn = Image.open("images\img_5.png")
        word_img_btn = word_img_btn.resize((250, 180), Image.ANTIALIAS)
        self.word_img1 = ImageTk.PhotoImage(word_img_btn)

        word_b1 = Button(bg_img,  image=self.word_img1, cursor="hand2", )
        word_b1.place(x=510, y=100, width=250, height=180)

        word_b1_1 = Button(bg_img, text="word", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="#ffcc44", fg="navyblue",bd=5, justify="left", padx=2, pady=2,relief="sunken")
        word_b1_1.place(x=510, y=280, width=250, height=45)

          # sentence System  button 3
        sen_img_btn = Image.open("images\img_5.png")
        sen_img_btn = sen_img_btn.resize((250, 180), Image.ANTIALIAS)
        self.sen_img1 = ImageTk.PhotoImage(sen_img_btn)

        sen_b1 = Button(bg_img,  image=self.sen_img1, cursor="hand2", )
        sen_b1.place(x=780, y=100, width=250, height=180)

        sen_b1_1 = Button(bg_img,  text="Sentence", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="#ffcc44", fg="navyblue",bd=5, justify="left", padx=2, pady=2,relief="sunken")
        sen_b1_1.place(x=780, y=280, width=250, height=45)



    def train(self):
            self.new_window = Toplevel(self.root)
            self.app = train(self.new_window)



if __name__ == "__main__":
        root = Tk()
        obj = Classifier(root)
        root.mainloop()