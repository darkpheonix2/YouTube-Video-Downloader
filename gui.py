from tkinter import *
from tkinter import filedialog

# Function to select path
def select_path():
    # allows to select the path from file explorer
    path = filedialog.askdirectory() 
    path_label.config(text=path)

# To move file to selected directory
import shutil

# Funtion to download the video
from moviepy import * 
from moviepy.editor import VideoFileClip
from pytube import YouTube as YT
def download_file():
    # get user path
    get_link=link_field.get()
    # get seleced path
    user_path = path_label.cget("text")
    screen.title("Downloading ......")
    # Download video
    video = YT(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(video)
    vid_clip.close()
    # Moving to directory
    shutil.move(video,user_path)
    screen.title("Download complete! Download more!!")




screen = Tk()
title = screen.title("Youtube Download")
canvas = Canvas(screen,width=500,height=500)
canvas.pack()

# Adding image and inputs
logo_img = PhotoImage(file="C:\\Users\\nakul\\OneDrive\\Desktop\\coding\\Projects\\Youtube Downloader\\download.png")
# Resizing the image
# logo_img = logo_img.subsample(2,2)
 
canvas.create_image(250,80,image=logo_img)
#  x position=250 , y position =80

# Link field
link_field=Entry(screen,width=50)
link_label = Label(screen,text="Enter the Download link: ",font=('Arial',15))

# Select path for saving file
path_label = Label(screen,text="Select path for download",font=('Arial',15))
select_btn = Button(screen,text="Select",command=select_path)

# Add to window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)

# Add widgets to window
canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=link_field)

# Download Button
dld_button = Button(screen,text="Download File",command=download_file)
# Adding to window
canvas.create_window(250,390,window=dld_button) 


screen.mainloop()