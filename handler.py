from datetime import datetime


def hello():
    print('Здравствуйте')
    print('Введите дату в виде гггг.мм.дд, либо введите "сегодня" для получения информации о текущем дне, и я скажу расписание')


def handle_message():
    date = input()
    if len(date) == 10:
        t = datetime.strptime(date, "%d.%m.%Y")
        t.isoweekday()
        day = (t.isoweekday())
    else:
        return 'Введите дату в корректном формате'
    lessons = [
        [
            {"subject": "Литература", "teacher": "Угрехелидзе В. Г."},
            {"subject": "Литература", "teacher": "Угрехелидзе В. Г."},
            {"subject": "", "teacher": ""},
            {"subject": "Французский язык", "teacher": "Архипова Д. В."},
            {"subject": "", "teacher": ""},
            {"subject": "Химия", "teacher": "Малютина Е. М."},
            {"subject": "История", "teacher": "Авдеев А. Г."},
            {"subject": "История", "teacher": "Авдеев А. Г."},
            {"subject": "История", "teacher": "Авдеев А. Г."},
            {"subject": "", "teacher": ""}
        ],
        [
            {"subject": "", "teacher": ""},
            {"subject": "Французский язык", "teacher": "Архипова Д. В."},
            {"subject": "", "teacher": ""},
            {"subject": "Алгебра", "teacher": ""},
            {"subject": "Алгебра", "teacher": ""},
            {"subject": "Биология", "teacher": "Черткова Е. Р."},
            {"subject": "Биология", "teacher": "Черткова Е. Р."},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""}
        ],
        [
            {"subject": "Русский язык", "teacher": "Угрехелидзе В. Г."},
            {"subject": "Русский язык", "teacher": "Угрехелидзе В. Г."},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "Геометрия", "teacher": "Назарова К. А."},
            {"subject": "Геометрия", "teacher": "Назарова К. А."},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""}
        ],
        [
            {"subject": "", "teacher": ""},
            {"subject": "Французский язык", "teacher": "Архипова Д. В."},
            {"subject": "Химия", "teacher": "Малютина Е. М."},
            {"subject": "Химия", "teacher": "Малютина Е. М."},
            {"subject": "Алгебра", "teacher": ""},
            {"subject": "Алгебра", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""}
        ],
        [
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "", "teacher": ""},
            {"subject": "История", "teacher": "Авдеев А. Г."},
            {"subject": "Литература", "teacher": "Угрехелидзе В. Г."},
            {"subject": "Русский язык", "teacher": "Угрехелидзе В. Г."},
            {"subject": "Биология", "teacher": "Черткова Е. Р."},
            {"subject": "Биология", "teacher": "Черткова Е. Р."}
        ],
        ["Выходной"],
        ["Выходной"]
    ]
    return lessons[day]
