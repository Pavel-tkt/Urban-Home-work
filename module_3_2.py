#Задача "Рассылка писем":
#Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и
# 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    end_variants =('.com', '.ru', '.net')
    if ("@" not in recipient or "@" not in sender):
        print('@ expected')
    elif recipient.endswith(end_variants) and sender.endswith(end_variants):
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        #else:
            #print(message)
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    
send_email('1Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('2Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('3Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('4Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')