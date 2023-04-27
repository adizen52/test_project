import json
import validators

def user_login(json_object):
    username = input('Введите ваш логин: ')
    flag = 0
    for i in json_object['users']:
        if username == i['name']:
            flag = 1
    if flag:
        print('Такой Логин уже существует.')
        user_login(json_object)
    else:
        return username


def user_email(json_object):
    email = input('Введите ваш email: ')
    flag = 0
    if validators.email(email, whitelist = None):
        for i in json_object['users']:
            if email == i['email']:
                flag = 1
        if flag:
            print('Такой EMAIL уже есть.')
            user_email(json_object)
        else:
            return email
    else:
        print('Неправильный формат EMAIL.')
        user_email(json_object)


def password_user():
    password = input('Введите ПАРОЛЬ >= 12 символов,'
                     'не менее 1 цифры, 1 большой буквы, 1 малой буквы: ')

    letters = set('qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю')
    numbers = set('1234567890')
    if len(password) < 12:
        print("Пароль должен быть 12 или более символов.")
        password_user()
    if len(letters.intersection(set(password))) == 0:
        print('Должно быть не менее одной малой буквы.')
        password_user()
    if len(numbers.intersection(set(password))) == 0:
        print('Должно быть не менее одной цифры.')
        password_user()
    if len(set(password).intersection(set(str(letters).upper()))) == 0:
        print('Должна быть хоть одна большая буква.')
        password_user()

    return password

def register_user(json_obj):
    login = user_login(json_obj)
    email = user_email(json_obj)
    password = password_user()
    user = {'name' : login,
            'email' : email,
            'password' : password}
    json_obj['users'].append(user)
    with open('data.json', 'w') as outfile:
        json.dump(json_obj, outfile, indent=2)

def login(json_obj):
    usname = input('Введите Ваш логин: ')
    for i in json_obj['users']:
        if i['name'] == usname:
            while True:
                password = input('Введите пароль: ')
                if i['password'] == password:
                    logout = True
                    return logout
                else:
                    print('Неверный пароль.')
                    continue
    else:
        print('Данного пользователя нет.')

def start():

    with open('data.json', 'r') as infile:
        json_obj = json.load(infile)

    vv = input("Если вы хотите зарегистрироваться - 'Y', \n"
               "Если зарегистрированы и хотите войти - 'N': " )
    if vv.lower() == 'y':
        register_user(json_obj)
    else:
        print(login(json_obj))

start()










# anton = {'name' : 'Anton',
#          'email' : 'adizen52@uandex,ru',
#          'password' : 'qwerty123'}
#
# data = {}
#
# data['users'] = []
#
# data['users'].append(anton)
#
# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile, indent=2)

