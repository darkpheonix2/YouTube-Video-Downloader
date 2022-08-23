from tkinter import *
from tkinter import filedialog,messagebox
from pytube import YouTube,Playlist

# To automatically open the downloaded folder
import os

# Functionality Part
def download():
    path=filedialog.askdirectory()
    # print(path)
    link_url=text.get()
    # print(link_url)
    
    if(chk.get()==1):
        yt=YouTube(link_url)
        yt.streams.get_highest_resolution().download(path)
        messagebox.showinfo('Success','Downloading is successful')
        os.startfile(path)

    if chk.get()==2:
        yt_p=Playlist(link_url)
        for videos in yt_p.videos:
            videos.streams.get_hightest_resolution().download(path)
        messagebox.showinfo("Complete playlist downloaded")
        os.startfile(path) 




# Gui Part

screen = Tk()

# Frames are only visible when we add height and width to it or some text to them
screen.title("Youtube video downloader")
screen.config(bg='red4')

# Making a frame inside the window
outerframe = Frame(screen)
# Grid method helps to display
outerframe.grid(row=0, column=0, pady=30, padx=30)

logoimg = PhotoImage(file='4.png')
logolabel = Label(outerframe, image=logoimg)
logolabel.grid(row=0, column=0, padx=20, pady=20)

innerframe = LabelFrame(outerframe,
                        text='DOWNLOAD',
                        font=('arial', 14, 'bold'))
innerframe.grid(row=1, column=0, pady=30)

# chk will have one value depending upon the users choice 
chk=IntVar()
radioImage = PhotoImage(file='4.png')
videobtn = Radiobutton(innerframe,
                       image=radioImage,
                       text='Single Video',
                       compound=BOTTOM,
                       font=('arial', 12, 'bold'),
                       relief='solid',variable=chk,value=1)
videobtn.grid(row=0, column=0, padx=20, pady=20)

playlistradioImage = PhotoImage(file='4.png')
playlistvideobtn = Radiobutton(innerframe,
                               image=radioImage,
                               text='PLAYLIST',
                               compound=TOP,
                               font=('arial', 12, 'bold'),
                               relief='solid',variable=chk,value=2)
playlistvideobtn.grid(row=0, column=1, padx=20, pady=20)

# fg stand for foreground , i.e., text color
text = StringVar()
url_entry = Entry(outerframe,
                  width=60,
                  font=('arial', 14, 'bold'),
                  justify='center',
                  textvariable=text,
                  fg='gray')
url_entry.grid(row=2, column=0, padx=20, pady=30)
text.set('Enter URL')


def click(event):
    url_entry.delete(0, END)
    # But other color should be black when entered
    url_entry.config(fg='black')


url_entry.bind('<Button-1>', click)

downloadButton = Button(outerframe, text='Download', bg='red4',command=download)
downloadButton.grid(row=3, column=0, pady=20)

# This helps to play the screen
screen.mainloop()
