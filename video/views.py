from fileinput import filename
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
import magic
from pytube import YouTube


# Create your views here.

@api_view()
def video_download(request):
    try:

        url = request.query_params.get('url')

        SAVE_PATH = '/home/hariom/arka'

        try:
            # object creation using YouTube
            # which was imported in the beginning
            yt = YouTube(url)
        except:
            print("Connection Error")

        # filters out all the files with "mp4" extension
        mp4files = yt.streams.filter(progressive = True,file_extension='mp4').first()

        try:
            # downloading the video
            mp4files.download(output_path = SAVE_PATH, filename='Hariom Video')
        except:
            print("Some Error!")

    except Exception as e:
        print(e)

    return Response({
        'success': True,
        'status_code': status.HTTP_200_OK,
        'message': (
            'Yotube video downloader'
        ),
        'data': None,
    }, status = status.HTTP_200_OK)
