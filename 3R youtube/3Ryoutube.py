#Packages for GUI
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
#Package for download code
from pafy import new

def Next():
    global myCanvas, LocError, REntry, RChoices, EntryError, Choices
    myCanvas.delete('all')
    myCanvas.create_image(0,0,image= MyImage, anchor='nw')

    #3R Link Label
    myCanvas.create_text(200,40, text='Enter your link here:',fill='#5b6770', font=('jost', 14))

    #Entry Box
    REntryVar = StringVar()
    REntry = Entry(root, width=50,bg='#FBFBFB', textvariable= REntryVar)
    myCanvas.create_window(50,62, anchor='nw', window=REntry)

    #Error message
    EntryError = myCanvas.create_text(200,90, text='*You must enter a link',fill='#FFB185', font=('jost', 10))

    #Save Label
    SaveLabel = myCanvas.create_text(200,132, text='Choose a location',fill='#5b6770', font=('jost', 14))

    #Button for location
    SaveLoc = Button(root, width=15, bg='#F3C4B7',fg='white', text='Choose', command = openLocation)
    myCanvas.create_window(145,154, anchor='nw', window=SaveLoc)

    #Error message of locatino
    LocError = myCanvas.create_text(200,187, text='*You must select a location',fill='#FFB185', font=('jost', 10))

    #Video or Audio
    VorA = myCanvas.create_text(200,225, text='Select',fill='#5b6770', font=('jost', 14))

    #Combobox
    Choices = ['Video', 'Only Audio']
    RChoices = ttk.Combobox(root, values= Choices)
    myCanvas.create_window(130,242, anchor='nw', window=RChoices)

    #Download button
    Download = Button(root, width=10, bg='#F3C4B7',fg='white', text='Download', command= download)
    myCanvas.create_window(162,280, anchor='nw', window=Download)


#Download Function
def download():
    link = REntry.get()
    choice = RChoices.get()
    video = new(link)
    if(len(link)>1):
        myCanvas.itemconfig(EntryError,text='')
        if(choice == Choices[0]):
            select = video.getbest()
        elif(choice == Choices[1]):
            audio = video.audiostreams
            select = audio[0]
        else:
            myCanvas.itemconfig(EntryError,text='Try again',fill='#FFB185')
    select.download(Folder_Name)
    myCanvas.itemconfig(EntryError,text='')
    myLabel = myCanvas.create_text(200,320, text='Download Completed',fill='#95C674', font=(11) )

#File location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        myCanvas.itemconfig(LocError,text=Folder_Name, fill='#95C674')
    else:
        myCanvas.itemconfig(LocError,text='Please Choose Folder!!',fill='#FFB185')


#root
root = Tk()
root.title('3R')
root.geometry('400x400')
root.iconbitmap('iconP.ico')

#Images definition
MyImage = PhotoImage(file='222.png')
MyImage1 = PhotoImage(file='33.png')

#Canvas 
myCanvas = Canvas(root, width=350, height=300, bd=0, highlightthickness=0)
myCanvas.pack(fill='both', expand=True)
CanvasImage = myCanvas.create_image(0,0,image= MyImage1, anchor='nw')

#Start Window
#Start Button
Start = Button(root, width=10, bg='#F3C4B7',fg='white', text='Start', command= Next)
myCanvas.create_window(162,230, anchor='nw', window=Start)
#Start Texts 
myCanvas.create_text(200,150, text='Welcome To 3R',fill='#5b6770', font=('jost', 16))
myCanvas.create_text(200,170, text='For Downloading From YouTube',fill='#5b6770', font=('jost', 10))
myCanvas.create_text(100,390, text='By Rawabi, Raghad, and Rahaf',fill='#5b6770', font=('jost', 10))

root.mainloop()