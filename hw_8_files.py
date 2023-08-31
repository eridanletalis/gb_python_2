"""
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определённой записи
4. Программа должна быть реализована с использованием функций

Меню:
1. Добавить контакт
2. Сохранить файл
3. Вывести все контакты
4. Поиск по имени/фамилии
5. Загрузить из файла
6. Изменить контакт
7. Удалить контакт
0. Выйти

"""


def print_div_string():

    print('\n', '*'*80, '\n')


def contact_on_screen(phonebook:list, list_number:int):
    contact = phonebook[list_number]
    print(f"{contact['last_name']} {contact['first_name']} {contact['middle_name']}: {contact['phone_number']}")


def get_contact_dict():
    last_name = input('Фамилия: ')
    first_name = input('Имя: ')
    middle_name = input('Отчество: ')
    phone_number = input('Номер телефона: ')

    return {'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'phone_number': phone_number}


def add_contact(phonebook: list,
                contact: dict):

    phonebook.append(contact)
    print('Контакт добавлен')


def save_to_file(phonebook, filename='data.txt'):
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(f"{contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, "
                       f"{contact['phone_number']} \n")
    print('Данные сохранены в файл ', filename)



def list_all_contacts(phonebook):
    if len(phonebook) == 0:
        print('Записей не содержится')
    else:
        for idx in range(len(phonebook)):
            contact_on_screen(phonebook, idx)


def search_contact(phonebook:list, pattern:str):
    not_found_flag = True
    pattern = pattern.lower()
    for idx, contact in enumerate(phonebook):
        if pattern in contact['last_name'].lower() or \
           pattern in contact['first_name'].lower() or \
           pattern in contact['middle_name'].lower():
            not_found_flag = False
            print(f'Номер вхождения: {idx}')
            contact_on_screen(phonebook, idx)

    if not_found_flag:
        print('Ничего не найдено')


def load_from_file(filename='data.txt'):
    phonebook = []
    with open(filename, 'r') as file:
        for contact in file:
            try:
                last_name, first_name, middle_name, phone_number = contact.split(',')
                phonebook.append({'last_name': last_name,
                                    'first_name': first_name,
                                    'middle_name': middle_name,
                                    'phone_number': phone_number})
            except Exception as e:
                pass
    return phonebook


def change_contact(phonebook):
    print_div_string()
    print('Известен ли номер вхождения в словарь или требуется произвести поиск?')
    print('1. Известен номер вхождения')
    print('2. Требуется произвести сначала поиск')
    print_div_string()
    change_choice = input("Выш выбор (для выхода ввести отличное от 1 и 2: ")

    if change_choice == '1':

        return changer(phonebook)

    if change_choice == '2':
        search_contact(phonebook, input('Введите ключ для поиска: '))
        return changer(phonebook)


def changer(phonebook):
    idx = int(input('Введите номер вхождения (для выхода без изменений -1): '))
    if idx < 0:
        return phonebook
    print('Необходимо ввести полные данные контакта с изменённой информацией')
    print('Меняется контакт ')
    contact_on_screen(phonebook, idx)

    phonebook[idx] = get_contact_dict()
    return phonebook


def delete_contact(phonebook:list):
    print_div_string()
    print('Известен ли номер вхождения в словарь или требуется произвести поиск?')
    print('1. Известен номер вхождения')
    print('2. Требуется произвести сначала поиск')
    print_div_string()
    change_choice = input("Выш выбор (для выхода ввести отличное от 1 и 2: )")

    if change_choice == '1':

        return deleter(phonebook)

    if change_choice == '2':
        search_contact(phonebook, input('Введите ключ для поиска: '))
        return deleter(phonebook)


def deleter(phonebook: list, idx:int):
    idx = int(input('Введите номер вхождения (для выхода без изменений -1): '))
    if idx < 0:
        return phonebook
    print('Удаляется контакт. ')
    contact_on_screen(phonebook, idx)
    if input('Подтвердить (1)? Отменить (2)') == '1':
        del phonebook[idx]
    return phonebook

def main():
    phonebook = []

    while True:
        print_div_string()
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")
        print("4. Поиск по имени/фамилии")
        print("5. Загрузить из файла")
        print("6. Изменить контакт")
        print("7. Удалить контакт")
        print("0. Выйти")
        print_div_string()

        choice = int(input('Выберете действие: '))

        if choice == 0:
            break

        if choice == 1:
            contact_dict = get_contact_dict()
            add_contact(phonebook, contact_dict)
        if choice == 2:
            save_to_file(phonebook)

        if choice == 3:
            list_all_contacts(phonebook)

        if choice == 4:
            search_contact(phonebook, input('Введите ключ для поиска: '))

        if choice == 5:
            phonebook = load_from_file()

        if choice == 6:
            phonebook = change_contact(phonebook)

        if choice == 7:
            phonebook = delete_contact(phonebook)


if __name__ == '__main__':
    main()


