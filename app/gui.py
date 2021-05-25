import tkinter
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import os
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import themed_tk as tk
import tkinter.font as font
import webbrowser

# create surface
from PIL import ImageTk

root = tk.ThemedTk()
root.title('FaceScan')
root.iconbitmap("pictures/hnet.com-image.ico")
root.configure(background='#464646')
root.resizable(False, False)
# put root in the middle of the screen
root_width = root.winfo_screenwidth() // 2
root_height = root.winfo_screenheight() // 2
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (root_width / 2))
y = int((screen_height / 2) - (root_height / 2))
root.geometry(f'{root_width}x{root_height}+{x}+{y}')
root.get_themes()
root.set_theme("equilux")
# font used for text in gui
font = font.Font(size=10, weight="bold")
# create frame for image
frametop = ttk.Frame(root)
frametop.pack()

# create label on top of frame with logo
img = PhotoImage(file="pictures/logo1.png")
labelbg = ttk.Label(frametop, image=img)
labelbg.pack(pady=10)

frameall = ttk.Frame(root)
frameall.pack()
# create Frame for Threshold
framethres = ttk.Frame(frameall)
framethres.pack()


# start program with selected source annd threshol
def setsource(args):
    os.system("python detect.py --source " + str(inputtext.get()) + " --weights best.pt --conf-thres " + setthreshold())


# clear entry text on click
def clearpath(event):
    event.widget.delete(0, 'end')
    return None


# get slider value
def setthreshold():
    sliderval = slider.get()
    formatted_sliderval = "{:.1f}".format(sliderval)
    return formatted_sliderval


# get slider value to put into label
def getvalue(val):
    formatted_val = "{:.1f}".format(float(val))
    threshinfo = ttk.Label(framethres, text=formatted_val)
    threshinfo.grid(row=1, column=3)


# function to select directory to use as path
def browsepath():
    # select directory
    filename = filedialog.askdirectory()
    input_path.delete(0, 'end')
    input_path.insert(0, filename)
    return filename


# set directory or file in entry as path, returns error if entry is empty
def setpath():
    if not input_path.get():
        messagebox.showwarning("Error", "Please insert Path!")
    if input_path.get() == 'Select or Paste Path':
        messagebox.showwarning("Error", "Please insert Path!")
    else:
        os.system("python detect.py --source " + input_path.get() + " --weights best.pt --conf-thres " + setthreshold())
        input_path.delete(0, 'end')


# function to select directory to use as stream
def browsestream():
    # select directory
    filename = filedialog.askdirectory()
    input_stream.delete(0, 'end')
    input_stream.insert(0, filename)
    return filename


# set directory or file in entry as stream, returns error if entry is empty
def setstream():
    if not input_stream.get():
        messagebox.showwarning("Error", "Please insert Stream!")
    if input_path.get() == 'Select or Paste Stream':
        messagebox.showwarning("Error", "Please insert Stream!")
    else:
        os.system(
            "python detect.py --source " + input_stream.get() + " --weights best.pt --conf-thres " + setthreshold())
        input_stream.delete(0, 'end')

def gotodashboard():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


label_thre = ttk.Label(framethres, text="Set Threshold: ")
label_thre.grid(row=1, column=1, padx=10, pady=10)
label_thre['font'] = font
slider = ttk.Scale(framethres, from_=0, to=1, orient=HORIZONTAL, length=450, command=getvalue)
slider.set(0.4)
slider.grid(row=1, column=2, padx=15)
threshinfo = ttk.Label(framethres)
threshinfo.grid(row=1, column=3, padx=5)
threshinfo['font'] = font

# create Frame to set source
framemiddle = ttk.Frame(frameall)
framemiddle.pack()
labelsource = ttk.Label(framemiddle, text="      Choose a Camera as Output")
labelsource.grid(row=2, column=1, padx=25, pady=18)
labelsource.config()
labelsource['font'] = font

inputtext = StringVar(value="0")
# radiobuttons to make camera selection
ttk.Radiobutton(framemiddle, text="Webcam", variable=inputtext, value=0).grid(row=2, column=3, padx=5)
ttk.Radiobutton(framemiddle, text="Camera 1", variable=inputtext, value=1).grid(row=2, column=4, padx=5)
ttk.Radiobutton(framemiddle, text="Camera 2", variable=inputtext, value=2).grid(row=2, column=5, padx=5)

button_source = ttk.Button(framemiddle, text="Set Source", command=lambda: setsource(inputtext.get()))
button_source.grid(row=2, column=7, padx=40)

# create Frame to set path to directory or file
framecenter = ttk.Frame(frameall)
framecenter.pack()
labelpath = ttk.Label(framecenter, text="Add Path:       ")
labelpath.grid(row=3, column=1, pady=10)
labelpath['font'] = font
cleartext = StringVar()
cleartext.set("Select of Paste Path")
input_path = ttk.Entry(framecenter, width=45, text=cleartext)
input_path.grid(row=3, column=2)
input_path.bind("<Button-1>", clearpath)

button_browse = ttk.Button(framecenter, text="Browse", command=lambda: browsepath()).grid(row=3, column=5)
button_source = ttk.Button(framecenter, text="Set Path", command=lambda: setpath())
button_source.grid(row=3, column=6, pady=12)

# create Frame to link to stream
framebottom = ttk.Frame(frameall)
framebottom.pack()

labelstream = ttk.Label(framebottom, text="Add Stream:    ")
labelstream.grid(row=4, column=2,pady = 12)
labelstream['font'] = font

cleartext2 = StringVar()
cleartext2.set("Select of Paste Stream")
input_stream = ttk.Entry(framebottom, width=45, text=cleartext2)
input_stream.grid(row=4, column=4)

input_stream.bind("<Button-1>", clearpath)
input_stream.bind("<Button-2>", clearpath)
button_browse2 = ttk.Button(framebottom, text="Browse", command=lambda: browsestream()).grid(row=4, column=5)

button_source = ttk.Button(framebottom, text="Set Stream", command=lambda: setstream())
button_source.grid(row=4, column=6)

dashboard = ttk.Button(framebottom,text="View Dashboard", command=lambda: gotodashboard())
dashboard.grid(row=5, columnspan=3)

credit = ttk.Label(root, text="Created by Daniel Lechner and Gabriel Fütterer")
credit.pack()

root.mainloop()
