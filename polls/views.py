from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
import pafy
import os
from tkinter import filedialog       
from tkinter import *



# Create your views here.
def home(request):
    if(request.POST.get('submit')):
        form(request.POST.get('name'),request.POST.get('path'))
    return render(request,'polls/home.html')
def form(data,path):
        video=pafy.new(data)
        audiostreams=video.audiostreams
        for i in audiostreams:
            print('bitrate: %s, ext: %s, size: %0.2fMb' % (i.bitrate, i.extension,i.get_filesize()/1024/1024))
                

        bestaudio=video.getbestaudio()
        bestaudio.download(filepath=path)



        old_extension = '.webm'
        old_extension2= '.m4a'
        new_extension = '.mp3'

        files_counter = 0

        with os.scandir(path) as files_and_folders:
            for element in files_and_folders:
                if element.is_file():
                    root, ext = os.path.splitext(element.path)
                    if ext == old_extension:
                        new_path = root + new_extension
                        os.rename(element.path, new_path)
                        files_counter += 1
        
        files_counter = 0

        with os.scandir(path) as files_and_folders:
            for element in files_and_folders:
                if element.is_file():
                    root, ext = os.path.splitext(element.path)
                    if ext == old_extension2:
                        new_path = root + new_extension
                        os.rename(element.path, new_path)
                        files_counter += 1


    