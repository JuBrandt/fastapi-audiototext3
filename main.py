import os
import shutil
import subprocess
import json
# import pyaudio
from moviepy.editor import *
import uvicorn
import aiofiles
import aiofiles.os
from fastapi import FastAPI, File, Form, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from uuid import uuid4


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

'''----------- СТАРТ Загрузка mp4'''
@app.post("/videototext", response_class=HTMLResponse)
async def upload_file_mp4(request: Request, title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):


    file_name = f'{uuid4()}_{file.filename}'
    if file.content_type == 'video/mp4':
        async with aiofiles.open(file_name, "wb") as buffer:
            for i in range(10):
                data = await file.read()
                await buffer.write(data)
            async with aiofiles.open(file_name, mode='r'):
                file_stat = await aiofiles.os.stat(file_name)
                if file_stat.st_size <= 314572800:
                    with open(f'{file_name}', 'rb'):
                        with open(f'{file_name}.docx', 'w'):
                            cmd = f"python3 test_ffmpeg_ru.py {file_name}"
                            p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True,
                                                  )
                            out = p1.communicate()
                            file_text = shutil.copy2(r'file_name.txt', f'{file_name}.docx')
                            print(out)
                            print(file_text)

                else:
                    await aiofiles.os.remove(file_name)
                    raise HTTPException(status_code=418,
                                        detail="Проверьте размер файла. Должен быть не больше 300 mb")
    return templates.TemplateResponse('download.html', {'request': request})



@app.get('/videototext', response_class=HTMLResponse)
def upload_file_mp4(request: Request):


    return templates.TemplateResponse('videototext.html', {'request': request})

'''-------- КОНЕЦ mp4'''

'''--------------Загрузка аудио файла- mp3'''

@app.post("/index", response_class=HTMLResponse)
async def upload_file_mp3(request: Request, title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    file_name = f'{uuid4()}_{file.filename}'
    if file.content_type == 'media/mp3':
        async with aiofiles.open(file_name, "wb") as buffer:
            for i in range(10):
                data = await file.read()
                await buffer.write(data)
            async with aiofiles.open(file_name, mode='r'):
                file_stat = await aiofiles.os.stat(file_name)
                if file_stat.st_size <= 314572800:
                    with open(f'{file_name}', 'rb'):
                        with open(f'{file_name}.docx', 'w'):
                            cmd = f"python3 test_ffmpeg_ru.py {file_name}"
                            p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True,
                                                  )
                            out = p1.communicate()
                            file_text = shutil.copy2(r'file_name.txt', f'{file_name}.docx')
                            print(out)
                            print(file_text)

                else:
                    await aiofiles.os.remove(file_name)
                    raise HTTPException(status_code=418,
                                        detail="Проверьте размер файла. Должен быть не больше 300 mb")
                return templates.TemplateResponse('download.html', {'request': request})



@app.get('/index', response_class=HTMLResponse)
def upload_file_mp3(request: Request):


    return templates.TemplateResponse('index_.html', {'request': request})

'''----- start TEMPLATES jinja'''

@app.get('/base_body_temp', response_class=HTMLResponse)
def base_body_temp(request: Request):


    return templates.TemplateResponse('base_body_temp.html', {'request': request})

@app.get('/base_body_temp2', response_class=HTMLResponse)
def base_body_temp2(request: Request):


    return templates.TemplateResponse('base_body_temp2.html', {'request': request})

@app.get('/header', response_class=HTMLResponse)
def header(request: Request):


    return templates.TemplateResponse('header.html', {'request': request})

@app.get('/base_footer', response_class=HTMLResponse)
def base_footer(request: Request):


    return templates.TemplateResponse('base_footer.html', {'request': request})

@app.get('/base_header', response_class=HTMLResponse)
def base_header(request: Request):


    return templates.TemplateResponse('base_header.html', {'request': request})

'''Добавить слова в библиотеку'''

@app.get('/add_words', response_class=HTMLResponse)
def get_add_words(request: Request):


    return templates.TemplateResponse('add_words.html', {'request': request})



'''Забрать аудио из видео файла'''

@app.post("/videotoaudio", response_class=HTMLResponse)
async def upload_videotoaudio(request: Request, file: UploadFile = File(...), title: str = Form(...), description: str = Form(...)):
    file_name = f'{uuid4()}_{file.filename}'
    if file.content_type == 'video/mp4':
        async with aiofiles.open(file_name, "wb") as buffer:
            for i in range(10):
                data = await file.read()
                await buffer.write(data)
            async with aiofiles.open(file_name, mode='r'):
                file_stat = await aiofiles.os.stat(file_name)

                if file_stat.st_size <= 314572800:
                    async with aiofiles.open(f'{file_name}.mp4', 'wb'):
                        audioclip = AudioFileClip(f'{file_name}')
                        file_audio_ext = audioclip.write_audiofile(f'{file_name}.wav', fps=44100, buffersize=50000,
                                                                   codec='mp3', write_logfile=True, logger='bar')
                        audioclip.close()
                        print(file_audio_ext)
                else:
                    await aiofiles.os.remove(file_name)
                    raise HTTPException(status_code=418,
                                        detail="Проверьте размер файла. Должен быть не больше 300 mb")
        return templates.TemplateResponse('download.html', {'request': request})



@app.get('/videotoaudio', response_class=HTMLResponse)
def upload_videotoaudio(request: Request):


    return templates.TemplateResponse('videotoaudio.html', {'request': request})

''' end templates jinja'''

'''-------Конец mp3'''



'''-----------------Загрузка wav'''

@app.post("/audiototext", response_class=HTMLResponse)
async def upload_file_wav(request: Request, title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    file_name = f'{uuid4()}_{file.filename}'
    if file.content_type == 'media/wav':
        async with aiofiles.open(file_name, "wb") as buffer:
            for i in range(10):
                data = await file.read()
                await buffer.write(data)
            async with aiofiles.open(file_name, mode='r'):
                file_stat = await aiofiles.os.stat(file_name)
                if file_stat.st_size <= 314572800:
                    with open(f'{file_name}', 'rb'):
                        with open(f'{file_name}.docx', 'w'):
                            cmd = f"python3 test_ffmpeg_ru.py {file_name}"
                            p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True,
                                                  )
                            out = p1.communicate()
                            file_text = shutil.copy2(r'file_name.txt', f'{file_name}.docx')
                            print(out)
                            print(file_text)
    return templates.TemplateResponse('download.html', context={'request': request})


@app.get('/audiototext', response_class=HTMLResponse)
def upload_file_wav(request: Request):


    return templates.TemplateResponse('audiototext.html', {'request': request})

'''------Конец wav'''

'''-------------Регистрация'''

@app.get('/registration', response_class=HTMLResponse)
def get_registration(request: Request):

    return templates.TemplateResponse('registration.html', {'request': request})

@app.get('/profile', response_class=HTMLResponse)
def get_profile(request: Request):


    return templates.TemplateResponse('profile.html', {'request': request})

'''-----------------
Микрофон'''

@app.get('/voicetotext', response_class=HTMLResponse)
def get_voicetotext(request: Request):


    return templates.TemplateResponse('voicetotext.html', {'request': request})

'''--------------------- Скачать файл'''

@app.get('/download', response_class=HTMLResponse)
def get_download(request: Request):


    return templates.TemplateResponse('download.html', {'request': request})

path = '/home/julia/dev/fastapi-audiototext/video/media/'


@app.get('/download_notfound')
async def download_txt():
    file_path = os.path.join(path, 'file_name.txt')
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {'error': 'File not found'}

@app.get('/download_1', responses={200: {'description': 'Файл успешно получен'}})
async def getfiletext():
    file_path = os.path.join(path, 'file_name.txt')
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='multipart/form-data', filename='file_name.txt')
    return {'error': 'File not found'}



if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)