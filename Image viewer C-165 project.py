from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer")
root.geometry("600x600")
root.configure(background="black")

img_path=""


def Open():
    
    global img_path
    img_path=filedialog.askopenfilename(title = "Select Image File", filetypes= [("Image Files", "*.jpg *.gif *.png *.jpeg")])
    print(img_path)
    img=ImageTk.PhotoImage(Image.open(img_path))
    label_image.configure(image=img)
    label_image.image=img
    
def rotate():
    
    print("Rotate 180")
    print(img_path)
    im=Image.open(img_path)
    rotated_img=im.rotate(180)
    img=ImageTk.PhotoImage(rotated_img)
    label_image.configure(image=img)
    label_image.image=img

def rotateg():
    
    print("Rotate 360")
    print(img_path)
    im=Image.open(img_path)
    rotated_img=im.rotate(360)
    img=ImageTk.PhotoImage(rotated_img)
    label_image.configure(image=img)
    label_image.image=img
    
btn_open=Button(root,text="Open Image",command=Open,relief="flat",font=("Times New Roman0",15),bg="#808080",fg="white")
btn_open.place(relx=0.5,rely=0.08,anchor=CENTER)

btn_rotate=Button(root,text="Rotate Image",command=rotate,relief="flat",font=("Times New Roman0",15),bg="#808080",fg="white")
btn_rotate.place(relx=0.25,rely=0.8,anchor=CENTER)

btn_rotateagain=Button(root,text="Rotate Image Again",command=rotateg,relief="flat",font=("Times New Roman0",15),bg="#808080",fg="white")
btn_rotateagain.place(relx=0.75,rely=0.8,anchor=CENTER)

label_image=Label(root,bg="black",fg="black")
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()