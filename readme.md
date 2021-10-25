**Проект fastapi-audiototext3**

###### Функционал проекта:

1. Транскрибация аудио и видео файлов формата mp4, wav, mp3 в текст. 

2. Транскрибация с голоса (микрофона) в текст.

3. Формируется документ с текстом в формате docx.

4. Выделение аудио дорожки из видео формата mp4.

5. Создание специализированной библиотеки терминов.

Темы: управленческая, юридическая, экономическая, компьютерная, медицинская.

**Установить локально**.
Вводные данные ОС (ubuntu 20 focal)

1. Создать виртуальную среду python3 -m venv tutorial-env
2. Активировать виртуальную среду source tutorial-env/bin/activate
3. Сохранить репозиторий в вашу папку, команда: git clone https://github.com/JuBrandt/fastapi-audiototext3.git
4. Команда pip install -r requirements.txt
5. Команда uvicorn main:app --reload
6. В браузере 127.0.0.1:8000/index

**Установить локально с Docker.** Вводные данные ОС (windows, macos, linux)

1. Установить docker https://docs.docker.com/engine/install/
2. Установить docker-comlose https://docs.docker.com/compose/install/
3. Команда docker pull juliabrandt/fastapi-audiototext:v3 (последняя версия)
Репозиторий dockerhub https://hub.docker.com/r/juliabrandt/fastapi-audiototext/tags

4. C
5. Команда docker-compose up -d
6. В браузере 127.0.0.1:8000/index

**Документация api**

127.0.0.1:8000/docs




