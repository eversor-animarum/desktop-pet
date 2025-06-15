#making  a listbox dammit
#importing stuff
from tkinter import *
from PIL import Image, ImageTk
#okay so basially it's going to be a small menu made up of buttons to basically start, stop, chnage the pet and put both pets there
#making the window
root=Tk()
root.title('Mochii Pets')
root.geometry('300x230+900+550')
root.attributes('-topmost',True)
root.configure(bg='beige')
#making it not resizable
root.resizable(False,False)
#converting the image to a photoimage object
img2=Image.open('assets/sakura-tree.jpg')
bg_img=ImageTk.PhotoImage(img2.resize((300,230),Image.Resampling.NEAREST))
l1=Label(root,image=bg_img,bd=0).place(x=0,y=0)
#this is for the pet pic in the background
img1=Image.open('assets/mochii_bg.png')
img=ImageTk.PhotoImage(img1.resize((140,300),Image.Resampling.NEAREST))
l2=Label(root,image=img).place(x=170,y=-40)
#including a label so i can make a cute background
#I'll be making buttons now
b1=Button(root,text='Start',command=lambda:print('App has started'),bg='lightpink',fg='black',font=('Arial',11))
b2=Button(root,text='Stop',command=lambda:print('quitting'),bg='lightpink',fg='black',font=('Arial',11))
b3=Button(root,text='Peach',command=lambda:print('Peachis activated'),bg='lightpink',fg='black',font=('Arial',11))
b4=Button(root,text='Goma',command=lambda:print('Goma is activated'),bg='lightpink',fg='black',font=('Arial',11))
b5=Button(root,text='Both',command=lambda:print('Both are active'),bg='lightpink',fg='black',font=('Arial',11))
#I put the butoons in a tuple
Buttons=[b1,b2,b3,b4,b5]
#placing them in the window using a for loop
for i,button in enumerate(Buttons):
    button.config(width=5,borderwidth=2,relief="ridge")  
   #how do I make these bouttons round and at the left side of the window?
   #putting the buttons in a vertical stack with a gap of 30 pixels between them
    button.place(x=10,y=10+i*40) 
#making the application run
#root.mainloop()

