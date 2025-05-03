import requests
import random
import string

from src.constants import Url

context = {}

# метод регистрации нового пользователя возвращает список из емейла и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_email_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем емейл, пароль и имя пользователя
    email = f'{generate_random_string(8)}@gmail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{Url.BASE_URL}/auth/register', json=payload)

    global context
    context['email'] = email
    context['password'] = password
    context['name'] = name

    # если регистрация прошла успешно (код ответа 201), добавляем в список емейл и пароль пользователя
    if response.status_code == 201:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

    # возвращаем список
    return login_pass

# метод регистрации нового пользователя возвращает ответ запроса
def register_new_courier_and_return_response():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем емейл, пароль и имя пользователя
    email = f'{generate_random_string(8)}@gmail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию пользователя
    response = requests.post(f'{Url.BASE_URL}/auth/register', json=payload)
    print(response.json())

    if response.status_code == 200:
        context['email'] = email
        context['password'] = password
        context['name'] = name
    print(context)
    # возвращаем ответ
    return response
