from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from pytube import YouTube
import os, fnmatch
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from django.conf import settings
from media_manager.utils import custom_exceptions as ce

from auth.helpers.query_helpers.login import (
    fetch_user_details_v1
)
from video.common import (
    messages as app_messages, constants as app_constants
)
from media_manager.common import (
    messages as glob_messages, constants as glob_constants
)

def export_document_v1(request):
    try:

        url = request.data.get('url')
        urltype = request.data.get('type')

        # Clearing Media Directory
        clear_media_dir()

        try:
            yt = YouTube(url)
        except:
            return Response({
                'success': True,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_messages.CONNECTION_ERROR,
                'data': None,
            }, status = status.HTTP_400_BAD_REQUEST)

        # Filtering out Files with mp4 Extension
        mp4files = yt.streams.filter(progressive = True,file_extension='mp4').first()

        try:
            # Downloading the Video
            mp4files.download(
                output_path = glob_constants.VIDEO_PATH, 
                filename=app_constants.VIDEO_TEMP
            )
        except:
            return Response({
                'success': True,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_messages.SOME_ERROR,
                'data': None,
            }, status = status.HTTP_400_BAD_REQUEST)
        
        # Loading the Downloaded Video File
        result, filepath = find(app_constants.VIDEO_TEMP, glob_constants.VIDEO_PATH)
        if not result:
            return Response({
                'success': True,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': app_messages.SOME_ERROR,
                'data': None,
            }, status = status.HTTP_400_BAD_REQUEST)

        # Declaring Path for the Media Files
        AUDIO_FILE_PATH = os.path.join(
            glob_constants.AUDIO_PATH, app_constants.AUDIO_TEMP
        )
        DOC_FILE_PATH = os.path.join(
            glob_constants.DOC_PATH, app_constants.DOC_TEMP
        )
        AUDIO_CHUNK_PATH = os.path.join(
            glob_constants.AUDIO_PATH, app_constants.AUDIO_CHUNK
        )

        # Converting from Video to Audio File
        clip = mp.VideoFileClip(filepath)
        clip.audio.write_audiofile(AUDIO_FILE_PATH)
        audio_file = AudioSegment.from_wav(AUDIO_FILE_PATH)

        # Removing the Video File
        rem_file(filepath)

        # Creating a blank Document
        document_file = open(DOC_FILE_PATH, "a+")

        # Chunk Audio Files Duration in Seconds
        duration = 10

        # Splitting the Audio Files into Chunks
        total_duration = len(audio_file)
        chunk_duration = duration*1000
        i=0
        t1 = 0
        t2 = chunk_duration

        while True:
            if t2 >= total_duration:
                break
            audio_chunk = audio_file[t1: t2]

            audio_chunk.export(AUDIO_CHUNK_PATH.format(i), bitrate ='192k', format ="wav")

            r = sr.Recognizer()
            with sr.AudioFile(AUDIO_CHUNK_PATH.format(i)) as source:
                audio_text = r.listen(source)
                try:
                    rec = r.recognize_google(audio_text)
                    document_file.write(rec+"\n")
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results. check your internet connection")
            
            # Removing the Chunk File
            rem_file(AUDIO_CHUNK_PATH.format(i))

            t1 = t2
            t2 += chunk_duration
            i += 1
        
        document_file.close()

        # Returning the Created Document File
        document_file = open(DOC_FILE_PATH, 'r')
        response = HttpResponse(
            document_file,
            content_type='text/plain')

        response['Content-Disposition'] = 'attachment; filename="'+app_constants.DOC_TEMP+'"'

        # Removing the Audio & Document File
        rem_file(AUDIO_FILE_PATH)

        return response

    except Exception as e:
        raise ce.InternalServerError

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return (True, os.path.join(root, name))
    return (False, '')

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def find_pattern(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def find_files(path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            result.append(os.path.join(root, name))
    return result

def rem_file(path):
    if os.path.exists(path):
        os.remove(path)

def clear_media_dir():
    try:
        files = find_files(glob_constants.MEDIA_DIR)
        for file in files:
            rem_file(file)
    except Exception as e:
        raise ce.InternalServerError