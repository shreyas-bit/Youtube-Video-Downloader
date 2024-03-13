from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream=streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("video download complete")
        
    except Exception as e:
        print(e)

def open_file_dialog():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Select a folder:{folder}")
    return folder


if __name__ == "__main__": #directly executing anything that happens under this
    root= tk.Tk()
    root.withdraw()
    
    video_url=input("Please enter the Youtube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("started download")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
