# %%
import pytube as yt
import httpx as hx
import asyncio as io
import datetime as dt
import os

# %%
class you_tube():
    def __init__ (self, url):
        self.url = url
        #yt.Playlist
        self.yt_list = yt.Playlist(self.url)
        self.url_jpg  = yt.YouTube(self.yt_list[0]).thumbnail_url
        self.title = self.yt_list.title

    def get_url_thumb(self, num_video = 0):
        self.url_jpg  = yt.YouTube(self.yt_list[num_video]).thumbnail_url


    def get_list(self):
        if self.list_type == True:
            return self.yt_list
        else:
            return 'not will informed a url list'


    def create_folder(self, folder_name = ''):
        if folder_name == '':
            folder_name = self.title

        try:
            os.makedirs(folder_name)
            self.folder = folder_name

        except OSError as err:
            if err.errno == 17:
                self.folder = folder_name

            print(err)

        
    def get_thumb(self, path = ''):
        if path == '':
            path = self.folder

        filename = 'Folder.jpg'
        
        response = hx.get(self.url_jpg)
        img = open(path + '/' + filename, 'wb').write(response.content)
            
    def get_video(self, folder_name = ''):
        if folder_name == '':
            folder_name = self.folder
            
        for video in self.yt_list.videos:
            video.streams.last().download(output_path = folder_name)
        

    def get_audio(self, folder_name = ''):
        if folder_name == '':
            folder_name = self.folder
            
        for video in self.yt_list.videos:
            video.streams.filter(only_audio = True).last().download(output_path = folder_name, filename = video.title + '.mka')


    def get_single_audio(url):
        video = yt.YouTube(url)

        video.streams.filter(only_audio = True).last().download(filename = video.title + '.mka')
        

# %%
list_txt = []
with open('yt_list.txt', 'r') as txt:
    list_txt = txt.readlines()

# %%
    
for item in list_txt:
    new_yt = you_tube(item)
    new_yt.title    
    new_yt.create_folder()
    #new_yt.get_url_thumb(num_video = 13)
    new_yt.get_thumb()
    new_yt.get_audio()



