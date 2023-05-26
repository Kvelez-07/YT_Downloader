import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        #Video Title
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download error!", text_color="red")

def on_progress(stream, chunk, bytes_remaning):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaning
    completion_percentange = bytes_downloaded / total_size * 100
    print(completion_percentange)
    per = str(int(completion_percentange))
    progress_percentage.configure(text=per + "%")
    progress_percentage.update()

    #Update progress bar
    progressBar.set(float(completion_percentange) / 100)

#System setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

#UI elements
title = customtkinter.CTkLabel(app, text="Inser a YT link: ")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finished download
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress percentage
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()