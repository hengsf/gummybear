from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from imaging import *

HEIGHT = 30
WIDTH = 450
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users",
                                          title="Open file okay?",
                                          filetypes= (("img","*.img"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

def SelectedFolder():
    path = askdirectory(title='Select Folder')  # shows dialog box and return the path
    print(path)

def SelectedDDImage():
        # RUNNING THE DD SCRIPT.
        # Toplevel object which will
        # be treated as a new window
        #newWindow = Toplevel(window)

        # sets the title of the
        # Toplevel widget
        #newWindow.title("New Window")

        # sets the geometry of toplevel
       # newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        #Label(newWindow,
          #    text="Result").pack()

        no_image()

window = Tk()
window.title("Welcome GUMMY Forensic Tool")
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image = PhotoImage(file='./Forensic-Images.png')
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

entry = Entry(window, bg='white',width='70')
entry.pack()
entry.insert(END,'choose your drive...')
button = Button(text="Open",bg='grey',width='10',command=SelectedFolder)
button.pack(side=LEFT,pady=10,padx=20)
DDbutton = Button(text="DD",bg='grey',width='10',command=SelectedDDImage)
DDbutton.pack(side=LEFT,pady=10,padx=20)


window.mainloop()