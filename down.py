import pytube  
from pytube import YouTube 
import os 
os.system('pip3 install pytube')
ideo_url = input("Enter the link here : ")   
resolution = input("Enter the resolution : ")
youtube = pytube.YouTube(video_url)  
video = youtube.streams.filter(file_extension='mp4',res=resolution).first()
print("Starting the Downloads ...............")
video.download()  
print("Download Completed !!")
