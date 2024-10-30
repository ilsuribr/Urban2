def send_email(message: str, recipient: str, *, sender="university.help@gmail.com"):
    ends = ('.com', '.ru', '.net')
    if not ('@' in recipient and '@' in sender and
            any([recipient.endswith(end) for end in ends]) and
            any([sender.endswith(end) for end in ends])):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return None

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return None

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return None
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        return None


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
