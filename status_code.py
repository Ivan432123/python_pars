import requests
import time


# Функция поиска рабочего сайта со статус кодом 200
def status_code():
    # Цикл проходит по всем ссылкам и отправляет запрос на статус код 200
    for x in range(1, 501):
        response = requests.get(url=f'https://parsinger.ru/task/1/{x}.html')
        time.sleep(1)
        # Если стату код=200, цикл останавливается
        if response.status_code == 200:
            print("status_code = 200 link №", x)
            break
        # Иначе продолжает выводить статус коды
        else:
            print(response.status_code, "link №" + str(x))


status_code()
