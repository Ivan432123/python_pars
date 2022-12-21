import requests
import time


# Функция загрузки картинок с сайта
def download_images():
    # Цикл проходит по всем urlam каждой картинки и загружает их поочереди в указанную папку
    for url_image in range(1, 161):
        response = requests.get(url=f'https://parsinger.ru/img_download/img/ready/{url_image}.png')
        time.sleep(0.00001)
        with open(f'C:/Users/Ivan/Desktop/image/{url_image}.png', 'wb') as file:
            file.write(response.content)
        print(url_image)


download_images()
