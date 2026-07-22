import random as r

digits = '0123456789'

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

punctuation = '!#$%&*+-=?@^_'

chars = []

def is_valid_answer(text):
    if text.lower() in ('да', 'yes'):
        return True
    else:
        return False

print(
    'Добро пожаловать в программу "Генератор безопасных паролей"',
)
while True:
    while True:
        password_counter = int(input('Введите количество паролей, которые необходимо сгенерировать: '))
        if password_counter == 0:
            print('Количество паролей не может быть равно нулю! Задайте число больше 0.')
            continue
        else:
            break
    while True:
        password_lenght = int(input('Введите желаемую длинну пароля. Минимальная длинна пароля равна "8": '))
        if password_lenght < 8:
                print('Укажите длинну пароля не менее 8 символов!')
                continue
        else:
            break
    user_input = input('Пароль должен содержать цифры? Напишите "Да" или "Нет"')
    if is_valid_answer(user_input):
        chars.extend(digits)
    user_input = input('Пароль должен содержать строчные буквы? Напишите "Да" или "Нет"')
    if is_valid_answer(user_input):
        chars.extend(lowercase_letters)
    user_input = input('Пароль должен содержать прописные буквы? Напишите "Да" или "Нет"')
    if is_valid_answer(user_input):
        chars.extend(uppercase_letters)
    user_input = input('Пароль должен содержать специальные символы? Напишите "Да" или "Нет"')
    if is_valid_answer(user_input):
        chars.extend(punctuation)