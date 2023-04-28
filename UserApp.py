import json
import validators

def user_login(json_object):
    while True:
        username = input('Введите ваш логин: ')
        flag = 0
        for i in json_object['users']:
            if username == i['name']:
                flag = 1
        if flag:
            print('Такой Логин уже существует.')
            continue
        else:
            break

    return username


def user_email(json_object):
    while True:
        email = input('Введите ваш email: ')
        flag = 0
        if validators.email(email, whitelist = None):
            for i in json_object['users']:
                if email == i['email']:
                    flag = 1
            if flag:
                print('Такой EMAIL уже есть.')
                continue
            else:
                break
        else:
            print('Неправильный формат EMAIL.')
            continue

    return email


def password_user():

    letters = set('qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю')
    numbers = set('1234567890')

    while True:
        password = input('Введите ПАРОЛЬ >= 12 символов,'
                         'не менее 1 цифры, 1 большой буквы, 1 малой буквы: ')
        if len(password) < 12:
            print("Пароль должен быть 12 или более символов.")
            continue
        if len(letters.intersection(set(password))) == 0:
            print('Должно быть не менее одной малой буквы.')
            continue
        if len(numbers.intersection(set(password))) == 0:
            print('Должно быть не менее одной цифры.')
            continue
        if len(set(password).intersection(set(str(letters).upper()))) == 0:
            print('Должна быть хоть одна большая буква.')
            continue
        break

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
    count = 0
    for i in json_obj['users']:
        if i['name'] == usname:
            while True:
                password = input('Введите пароль: ')
                if i['password'] == password:
                    logout = True
                    sp_inf = [logout, count]
                    return sp_inf
                else:
                    print('Неверный пароль.')
                    continue
        else:
            count += 1
    else:
        print('Данного пользователя нет.')
        logout = False
        sp_inf = [logout, None]
        return sp_inf

def start():

    with open('data.json', 'r') as infile:
        json_obj = json.load(infile)

    vv = input("Если вы хотите зарегистрироваться - 'Y', \n"
               "Если зарегистрированы и хотите войти - 'N': " )
    if vv.lower() == 'y':
        register_user(json_obj)
    elif vv.lower() == 'n':
        us_inf = login(json_obj)
        if us_inf[0] == True:
            qwest = input("Вы хотите удалить свою учетную запись? - 'y', \n"
                          "Вы хотите выйти из учетной записи? - 'n': ")
            if qwest.lower() == 'y':
                us_inf[0] = False
                json_obj['users'].pop(us_inf[1])
                with open('data.json', 'w') as outfile:
                    json.dump(json_obj, outfile, indent= 2)
                start()
            else:
                print('До новых встреч.')



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

