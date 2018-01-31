from datetime import datetime

[y]

def hello():
    print('Здравствуйте')
    print('Введите дату в виде гггг-мм-дд, либо введите "сегодкя" для получения информации о текущем дне,  и я скажу расписание')

def handle_message():
    date = input()
    if len(date) == 10:
        t = datetime.strptime(date, "%Y-%m-%d")
        t.isoweekday()
        day = (t.isoweekday())

def send_message():
    if day == 1:
        print("Литература, 404")
        print("Литература, 404")
        print("Английский язык, 206")
        print("Французский язык, 310")
        print("Физкультура, спортзал")
        print("Химия, 407")
        print("История, 203")
        print("История, 203")
        print("История, 203")
    if day == 2:
        print("Английский язык, 531")
        print("Французский язык, 312")
        print("Алгебра, 305")
        print("Алгебра, 305")
        print("Биология, 204")
        print("Биология, 204")
        print("МХК, 402")
if day == 3:
        print("Русский язык, 203")
        print("Русский язык, 203")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
if day == 2:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    if day == 2:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    if day == 2:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

hello()
handle_message()
send_message()

