import requests


# Функция загрузки видео с сайта
def download_video():
    url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
    response = requests.get(url=url, stream=True)
    with open('C:/Users/Ivan/Desktop/video/videoplayback.mp4', 'wb') as file:
        if file.write(response.content):
            print("ok")

download_video()
