import codecs

""" ЧТЕНИЕ ФАЙЛА """


def read_file():
    f = codecs.open("1.csv", "r", "utf-8")

    q = f.readline().split(",")  # запись вопросов
    q[-1] = q[-1].replace("\r\n", "")

    s = []  # запись студентов
    for x in f.readlines():
        x = x.replace("\r\n", "")
        a = x.split(",")
        s.append(a)

    return q, s


""" ИГРА """


def game():
    # переменные
    questions, students = read_file()
    current_students = students.copy()
    current_students_copy = []
    answers = []

    # игра
    for i in range(1, len(questions)):
        print(questions[i])  # заданный вопрос

        while True:  # ответ от пользователя
            answer = input("Введите 'нет' или 'да': ")
            if answer == "нет" or answer == "да":
                answers.append(answer)
                break

        for j in range(len(current_students)):
            if current_students[j][i] == answer:
                current_students_copy.append(current_students[j])  # запись в отдельный список подходящих студентов
        current_students = current_students_copy.copy()  # запись подходящих студентов в основной список
        current_students_copy = []

        if len(current_students) == 1:  # если остался 1 студент, выдать ответ
            return f"Подходящий студент: {current_students[0][0]}!"
        if len(current_students) == 0:  # если не осталось подходящих студентов, прекратить игру (1)
            break

    if len(current_students) > 1:  # если у нескольких студентов оказались одни и те же характеристики
        for i in range(len(current_students)):
            print(f"Вы имели в виду студента {current_students[i][0]}?")
            while True:
                answer = input("введите 'нет' или 'да': ")
                if answer == "нет" or answer == "да":
                    break

            if answer == "да":
                return f"Подходящий студент: {current_students[i][0]}!"
            elif answer == "нет" and len(current_students)-i == 2:  # осталось 2 студента, но 1 не подходит - дать ответ
                return f"Подходящий студент: {current_students[-1][0]}!"

    return "Здесь нет таких студентов... Начните сначала!"  # в случае (1) или безуспешный конец последнего цикла


print(game())
