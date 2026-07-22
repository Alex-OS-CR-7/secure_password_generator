import random as r

digits = '0123456789'

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

punctuation = '!#$%&*+-=?@^_'

hard_chars = ['i', 'l', '1', 'L', 'o', '0', 'O']

def is_valid_answer(text):
    if text.lower() in ('да', 'yes'):
        return True
    else:
        return False

def is_valid_num(text):
    if text.isdigit():
        return True
    else:
        return False

print(
    'Добро пожаловать в программу "Генератор безопасных паролей"',
)
while True:
    chars = []
    while True:
        password_counter = input('Введите количество паролей, которые необходимо сгенерировать: ')
        if is_valid_num(password_counter) is False:
            print('Введите положительное целое число!')
            continue
        else:
            password_counter = int(password_counter)

        if password_counter == 0:
            print('Количество паролей не может быть равно нулю! Задайте число больше 0. ')
            continue
        else:
            break
    while True:
        password_length = input('Введите желаемую длинну пароля. Минимальная длинна пароля равна "8": ')
        if is_valid_num(password_length) is False:
                print('Введите положительное целое число!')
                continue
        else:
            password_length = int(password_length)
        
        if password_length < 8:
                print('Укажите длинну пароля не менее 8 символов! ')
                continue
        else:
            break
    while True:
        symbol_cnt_check = 0
        user_input = input('Пароль должен содержать цифры? Напишите "Да" или "Нет" ')
        if is_valid_answer(user_input):
            chars.extend(digits)
            symbol_cnt_check += 1
        user_input = input('Пароль должен содержать строчные буквы? Напишите "Да" или "Нет" ')
        if is_valid_answer(user_input):
            chars.extend(lowercase_letters)
            symbol_cnt_check += 1
        user_input = input('Пароль должен содержать прописные буквы? Напишите "Да" или "Нет" ')
        if is_valid_answer(user_input):
            chars.extend(uppercase_letters)
            symbol_cnt_check += 1
        user_input = input('Пароль должен содержать специальные символы? Напишите "Да" или "Нет" ')
        if is_valid_answer(user_input):
            chars.extend(punctuation)
            symbol_cnt_check += 1
        if symbol_cnt_check > 0:
            break
        else:
            print('Необходимо указать хотя бы один набор символов для генерации пароля. Попробуйте еще раз.')
            continue
    break
user_input = input('Нужно исключить неоднозначные символы "il1Lo0O"? ')
if is_valid_answer(user_input):
    for i in hard_chars:
        if i in chars:
            chars.remove(i)

def generate_password():
    password = []
    for i in range(password_length):
        password.append(r.choice(chars))
    return ''.join(password)

for i in range(password_counter):
    print(generate_password())
