import tkinter
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import os
import tkinter as tk

# create surface
from PIL import ImageTk
root = Tk()
root.title('FaceScan')
root.iconbitmap("pictures/hnet.com-image.ico")
root.configure(background='#5F6368')
root.resizable(False,False)
# put root in the middle of the screen
root_width = root.winfo_screenwidth()//2
root_height = root.winfo_screenheight()//2
screen_width =root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (root_width/2))
y = int((screen_height/2) - (root_height/2))
root.geometry(f'{root_width}x{root_height}+{x}+{y}')

# create frame for image
frametop = Frame(root, padx=10, pady=10, bg='#5F6368')
frametop.pack()

# create label on top of frame with logo
img = PhotoImage(file="pictures/logo1.png")
labelbg = Label(frametop, image=img, bg='#5F6368')
labelbg.pack()

frameall = Frame(root,bg = '#5F6368',highlightbackground = 'black' , highlightthickness=1)
frameall.pack()
# create Frame for Threshold
framethres = Frame(frameall,padx=20,pady = 10, bg = '#5F6368',highlightbackground = 'black' , highlightthickness=1)
framethres.pack()


def setthreshold() :
    sliderval = slider.get()
    formatted_sliderval = "{:.1f}".format(sliderval)
    return formatted_sliderval

slider = Scale(framethres, from_= 0, to = 1, resolution = 0.1, orient=HORIZONTAL,bg = '#5F6368',length=450, bd = 0, fg = 'white',activebackground = '#464B51')
slider.set(0.4)
slider.grid(row=1, column = 2, padx = 10)


label_thre = Label(framethres, text="Set Threshold: ",padx=30, pady=0 , bg= '#5F6368', fg='white')
label_thre.grid(row=1, column =1, padx = 2)

# create Frame to set source
framemiddle = Frame(frameall,padx=20,pady = 15, bg = '#5F6368',highlightbackground = 'black' , highlightthickness=1)
framemiddle.pack()
labelsource = Label(framemiddle, text="Choose a Camera as Output",bg = '#5F6368', fg='white')
labelsource.grid (row =2 , column =1, padx = 25)
labelsource.config()

inputtext = StringVar(value="0")
# radiobuttons to make camera selection
Radiobutton(framemiddle, text="Webcam", variable = inputtext, value = 0,bg = '#5F6368', fg='white',selectcolor = '#5F6368',activebackground = '#464B51').grid(row=2 , column = 3)
Radiobutton(framemiddle, text="Camera 1", variable = inputtext, value = 1,bg = '#5F6368', fg='white',selectcolor = '#5F6368',activebackground = '#464B51').grid(row=2 , column = 4)
Radiobutton(framemiddle, text="Camera 2", variable = inputtext, value = 2,bg = '#5F6368', fg='white',selectcolor = '#5F6368',activebackground = '#464B51').grid(row=2 , column = 5)



def setsource(args):
           os.system("python detect.py --source " + str(inputtext.get()) + " --weights best.pt --conf-thres " + setthreshold())


button_source = Button(framemiddle, text="Set Source",padx=30, pady=0, command=lambda : setsource(inputtext.get()),bg = '#5F6368', fg='white',activebackground = '#464B51')
button_source.grid(row=2, column =7, padx = 30)


# create Frame to set path to directory or file
framecenter = Frame(frameall,padx=10,pady = 15, bg = '#5F6368',highlightbackground = 'black' , highlightthickness=1)
framecenter.pack()
labelpath = Label(framecenter, text="Add Path:",bg = '#5F6368', fg='white', padx= 16)
labelpath.grid (row =3 , column =1)
input_path = Entry(framecenter, width = 58, borderwidth= 3, fg='#8F9193')
input_path.grid(row=3, column=2)
input_path.insert(0, "Select or Paste Path")


# function to get directory
def browse():
    # select directory
    input_path.config(fg='black')
    filename = filedialog.askdirectory()
    input_path.delete(0, 'end')
    input_path.insert(0,filename)
    return filename

button_browse = Button(framecenter, text="Browse",padx=21,pady=0, command = lambda: browse(),bg = '#5F6368', fg='white',activebackground = '#464B51').grid(row=3, column = 5)

# function to set directory into command line
def setpath():
    if not input_path.get():
        messagebox.showwarning("Error", "Please insert Path!")
    if input_path.get() == 'Select or Paste Path':
        messagebox.showwarning("Error", "Please insert Path!")
    else:
        os.system("python detect.py --source " + input_path.get() + " --weights best.pt --conf-thres " + setthreshold())
        input_path.delete(0, 'end')

button_source = Button(framecenter, text="Set Path",padx=27, pady=0, command=lambda : setpath(),bg = '#5F6368', fg='white',activebackground = '#464B51')
button_source.grid(row=3, column =6)




# create Frame to link to stream
framebottom = Frame(frameall,padx=6,pady = 15, bg = '#5F6368',highlightbackground = 'black' , highlightthickness=1)
framebottom.pack()
labelstream = Label(framebottom, text="Add Stream:",bg = '#5F6368', fg='white',padx =16)
labelstream.grid (row =4 , column =1)



def browsestream():
    # select directory
    input_stream.config(fg='black')
    filename = filedialog.askdirectory()
    input_stream.delete(0, 'end')
    input_stream.insert(0,filename)
    return filename


input_stream = Entry(framebottom, width = 58, borderwidth= 3,fg='#8F9193')
input_stream.grid(row=4, column=2)
input_stream.insert(0, "Select or Paste Path")


button_browse2 = Button(framebottom, text="Browse",padx=21,pady=0, command = lambda: browsestream(),bg = '#5F6368', fg='white',activebackground = '#464B51').grid(row=4, column = 5)
def setstream():
    if not input_stream.get():
        messagebox.showwarning("Error", "Please insert Stream!")
    if input_path.get() == 'Select or Paste Stream':
        messagebox.showwarning("Error", "Please insert Path!")
    else:
        os.system("python detect.py --source " + input_stream.get() + " --weights best.pt --conf-thres " + setthreshold())
        input_stream.delete(0,'end')


button_source = Button(framebottom, text="Set Stream",padx=18, pady=0, command=lambda : setstream(),bg = '#5F6368', fg='white',activebackground = '#464B51')
button_source.grid(row=4, column =6)

root.mainloop()