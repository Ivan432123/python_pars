import requests, time


def status_code():
    for x in range(1, 501):
        response = requests.get(url=f'https://parsinger.ru/task/1/{x}.html')
        time.sleep(0.0001)

        if response.status_code == 200:
            print("Status Code = 200", "на сайте № " + str(x), response.text)
            break
        else:
            print("Статус код =", response.status_code, "сайт № " + str(x))


status_code()
