def PhoneMesage():

    let_and_num = {'1' : '.,?!:;1',
                   '2' : 'абвг2',
                   '3' : 'дежз3',
                   '4' : 'ийкл4',
                   '5' : 'мноп5',
                   '6' : 'рсту6',
                   '7' : 'фхцч7',
                   '8' : 'шщъы8',
                   '9' : 'ьэюя9',
                   '0' : ' 0 0 '}

    number_text = input('Введите последовательность: ').split()

    letters = []

    for num in number_text:
        symbol = num[0]
        pos = len(num)
        count = 1
        for i in num:
            if i == symbol and count == pos:
                if symbol == '1':
                    letters.append(let_and_num[symbol][count % 7 - 1])
                else:
                    letters.append(let_and_num[symbol][count % 5 - 1])
            elif i == symbol:
                count += 1
                continue
            else:
                print('Вы вводите не правильное значение.')
                return None

    print(''.join(letters))