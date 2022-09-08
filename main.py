from os import path
from tkinter import * # Buradaki zaten bütün özellikleri eklemiyor muydu ? Neden aşşağıya ayrıca fieldialog kısmını ekledik.
from tkinter import filedialog # fieldialog dosyayı kaydetmemizi sağlar ve nereye kaydetmek istediğimizi vs tarzı özelliklere yardımcı olur.
from moviepy import  *
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import  YouTube

import shutil
""""Shutil dizinler üzerinde bulunan dosyaları kopyalama , taşıma , açma, okuma , yazma ve kapatma gibi işlemleri “OS” modülü ile beraber basitçe yapmamızı sağlayan bir Python modülüdür."""

#Functions

def select_path():
    #allows user to select a path from the explorer

    path= filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    #get user path

    get_link= link_field.get()

    #get selected path

    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video

    mp4_Video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_Video)
    vid_clip.close()

    #move file to selected directory
    shutil.move(mp4_Video,user_path)
    screen.title('Download Complete! Download another file...')




#Tk classını çağırıyoruz.
screen = Tk()


title= screen.title('Youtube Download')

#Canvas classını çağırıyoruz
canvas = Canvas(screen, width=500,height=500)
canvas.pack()

"""print(help(Canvas))"""


#link field
link_field= Entry(screen, width=50)
link_label= Label(screen, text="Enter download link here !", font=('Arial',15))

#Select Path for saving
path_label = Label(screen, text ="Selcet Path For Download", font=('Arial',15))
select_btn = Button(screen, text="Select", command= select_path)
"""command kısmı ile bu butona özellik getirdik. 
buraya istediğimiz fonksiyonu ekledik burada fonksiyonun parantezlerini koymadan yazdık koyunca otomatik çalışıyor.
"""

#Add to window
canvas.create_window(250,280, window=path_label)# yarattığımız label ve butonları canvasa ekliyoruz. window kelimesi ile.
canvas.create_window(250,330, window=select_btn)

#Add widget to window
canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=link_field)


#Download btns
download_btn= Button(screen, text="Download File",command=download_file)

#add to canvas
canvas.create_window(250, 390,window=download_btn)
screen.mainloop()