def start():
    print(
        "\n   ***  Список работников  ***\n"
        + "------------------------------------------\n"
        + "Введите от1 до 5:\n"
        + " 1 Для показа работников\n"
        + " 2 Для добавления новых работников\n"
        + " 3 Для поиска работников\n"
        + " 4 Для удаление работников\n"
        + " 5 Для выхода\n------------------------------------------"
    )
    choice = input("Введите номер: ")
    return choice


def print_message(data):
    print(data)


def insert_data(message):
    return input(message)
