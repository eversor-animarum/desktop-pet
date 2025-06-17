#making  a listbox dammit
#importing stuff
from tkinter import Button, Frame, Label, Tk
from PIL import Image, ImageTk
#okay so basially it's going to be a small menu made up of buttons to basically start, stop, chnage the pet and put both pets there
from main import launch_window
#making the pet_window a global variable
pet_window=None
#making the window
root=Tk()
root.title('Mochii Pets')
root.geometry('300x230+900+550')
root.attributes('-topmost',True)
root.configure(bg='beige')
#making it not resizable
root.resizable(False,False)
#adding the background image first so other widgets show above it
img2=Image.open('assets/sakura-tree.jpg')
bg_img=ImageTk.PhotoImage(img2.resize((300,230),Image.Resampling.NEAREST))
l1=Label(root,image=bg_img,bd=0)
l1.place(x=0,y=0)
#this is for the pet pic in the background
img1=Image.open('assets/mochii_bg.png')
img=ImageTk.PhotoImage(img1.resize((140,300),Image.Resampling.NEAREST))
l2=Label(root,image=img)  
l2.place(x=170,y=-40)
#this is a method to import the second window
    #I'll be making methods to activate the pets 
def activate_peach():
    global pet_window
    pet_window= launch_window(root)
def activate_goma():
    print('Goma is activated')
def activate_both():
    print('We are here')
    #this is a method to kill the pets window,but still maintain the main menu window
#this is a mthod to close the window
def unactivate_pet():
    global pet_window
    if pet_window:
        pet_window.destroy()
        pet_window = None
        print('Pets are unactivated')
    else:
        print('No pet window to close') 
#this is a method to kill the app
def stop_pets():
    print('Pets are stopped')
    root.destroy()
#I'll be using frames for the preview
#creating  a container for all preview panels
right_panel=Frame(root,bg='pink')
#creating a single frame for each pet
peach_frame=Frame(right_panel,bg='antiquewhite')
goma_frame=Frame(right_panel,bg='white')
both_frame=Frame(right_panel,bg='mistyrose')
#adding an image and buttons to each frame
peach_img=Image.open('assets/ppic.jpg')
peach_img=ImageTk.PhotoImage(peach_img.resize((260,200),Image.Resampling.NEAREST))
peach_label=Label(peach_frame,image=peach_img)
peach_label.pack()
goma_img=Image.open('assets/goma_pic.jpg')
goma_img=ImageTk.PhotoImage(goma_img.resize((260,200),Image.Resampling.NEAREST))
goma_label=Label(goma_frame,image=goma_img)
goma_label.pack()
both_img=Image.open('assets/sakura-bg.jpg')
both_img=ImageTk.PhotoImage(both_img.resize((220,200),Image.Resampling.NEAREST))
both_label=Label(both_frame,image=both_img)
both_label.pack()
        #adding the buttons I need for each tab, six buttons in total
bb1=Button(peach_frame,text='Start',command=activate_peach)
bb2=Button(peach_frame,text='Quit',command=unactivate_pet)
bb3=Button(goma_frame,text='Start',command=activate_goma)
bb4=Button(goma_frame,text='Quit',command=unactivate_pet)
bb5=Button(both_frame,text='Start',command=activate_both)
bb6=Button(both_frame,text='Quit',command=unactivate_pet)
#giving them the same features using a for loop
buttons=[bb1,bb2,bb3,bb4,bb5,bb6]
startbuttons=[bb1,bb3,bb5]
stopbuttons=[bb2,bb4,bb6]
for i,button in enumerate(buttons):
    button.config(width=6,height=8,bg='lightpink',fg='black',font=('Arial',11),borderwidth=2,relief="ridge")
    #placing them in the frames
    button.pack(padx=0,pady=3)
#placing the start buttons in the first row
for i,button in enumerate(startbuttons):
    button.pack(side='left',padx=15,pady=5 )
#placing the stop buttons in the second row
for i,button in enumerate(stopbuttons):
    button.pack(side= 'right',padx=20,pady=5)
#the function to display the selcected panel
def show_panel(panel):
    #code to show it when needed
    right_panel.place(x=100,y=0,width=200,height=230)
    #using a for loop to hide all until one is selected
    for f in (peach_frame,goma_frame,both_frame):
        f.place_forget()
        #display the selected panel
    panel.place(x=0,y=0,relwidth=1,relheight=1)
#I'll be making buttons now
b1=Button(root,text='Peach',command=lambda:show_panel(peach_frame),bg='lightpink',fg='black',font=('Arial',11))
b2=Button(root,text='Goma',command=lambda:show_panel(goma_frame),bg='lightpink',fg='black',font=('Arial',11))
b3=Button(root,text='Both',command=lambda:show_panel(both_frame),bg='lightpink',fg='black',font=('Arial',11))
b4=Button(root,text='Stop',bg='lightpink',command=root.destroy,fg='black',font=('Arial',11))
#I put the buttons in a tuple
Buttons=[b1,b2,b3,b4]
#placing them in the window using a for loop
for i,button in enumerate(Buttons):
    button.config(width=5,borderwidth=2,relief="ridge")  
   #how do I make these bouttons round and at the left side of the window?
   #putting the buttons in a vertical stack with a gap of 30 pixels between them
    button.place(x=10,y=10+i*40) 
#making the application run
root.mainloop()
