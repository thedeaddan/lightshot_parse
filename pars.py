import random
import string
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

# Функция для генерации случайной строки заданной длины
def generate_random_string(length):
    letters_and_digits = string.ascii_lowercase + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string

# Инициализация счетчика
i = 0

# Список для хранения сгенерированных строк
generated = []

# Бесконечный цикл
while True:
    i += 1
    # Генерируем случайную строку из букв и цифр
    gen_string = generate_random_string(6)

    # Проверяем, не была ли уже сгенерирована такая строка
    if gen_string not in generated:
        generated.append(gen_string)
        # Формируем URL для запроса
        url = 'https://prnt.sc/' + gen_string

        # Отправляем GET-запрос на сайт с поддельным User-Agent
        response = requests.get(url, headers={'User-Agent': UserAgent().chrome})

        # Создаем объект BeautifulSoup для парсинга HTML-кода
        soup = BeautifulSoup(response.text, 'lxml')

        try:
            # Пытаемся найти элементы <img> с классом 'no-click screenshot-image'
            quotes = str(soup.find_all('img', class_='no-click screenshot-image')[0])
        except:
            # Если элементы не найдены, присваиваем переменной quotes пустую строку
            quotes = str(soup.find_all('img', class_='no-click screenshot-image'))

        try:
            # Разбиваем строку quotes по пробелам и выбираем 9-ый элемент
            div = quotes.split(" ")[8]
        except:
            # Если не удается получить 9-ый элемент, выводим содержимое переменной quotes
            print(quotes)

        try:
            # Разбиваем строку div по двойным кавычкам и выбираем второй элемент
            url_pic = div.split('"')[1]
        except:
            # Если не удается получить второй элемент, выводим содержимое переменной div
            print(div)

        # Проверяем, что в строке quotes нет подстроки "eQqbGWo.jpg"
        if "eQqbGWo.jpg" not in quotes:
            if "//st.pr" in url_pic:
                # Если ссылка начинается с "//st.pr", добавляем "http:" в начало
                url_pic = "http:" + url_pic

            # Отправляем GET-запрос по полученной ссылке на изображение
            img_data = requests.get(url_pic, headers={'User-Agent': UserAgent().chrome}).content

            # Сохраняем изображение на диск
            with open('/home/thedeaddan/pics/' + gen_string + '.jpg', 'wb') as handler:
                handler.write(img_data)

            # Выводим ссылку на изображение и сообщение "saved"
            print(url_pic)
            print("saved")
