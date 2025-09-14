def load_contacts():
    contacts = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        for r in file:
            r = r.strip()
            if not r:
                continue
            parts = r.split('|')

            while len(parts) < 4:
                parts.append('')

            if len(parts) >= 4:
                parts = parts[:4]
                contact = {
                    'id': parts[0],
                    'name': parts[1],
                    'phone': parts[2],
                    'comment': parts[3]
                }
                contacts.append(contact)
    return contacts

contacts = load_contacts()
for contact in contacts:
    print(f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact['comment']}")



def add_contact(id, name, phone, comment):
    with open('data.txt', 'a', encoding='utf-8') as file:
        line = f"{id}|{name}|{phone}|{comment}\n"
        file.write(line)



id = input("Введите ID: ")
name = input("Введите имя: ")
phone = input("Введите телефон:")
comment = input("Введите комментарий: ")

add_contact(id, name, phone, comment)


def show_menu():
    print("Выберите действие:")
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("0 - Выйти")

def load_contacts():
    contacts = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        for r in file:
            r = r.strip()
            parts = r.split('|')
            if len(parts) == 4:
                contact = {
                    'id': parts[0],
                    'name': parts[1],
                    'phone': parts[2],
                    'comment': parts[3]
                }
                contacts.append(contact)
    return contacts

def add_contact(id, name, phone, comment):
    with open('data.txt', 'a', encoding='utf-8') as file:
        line = f'{id}|{name}|{phone}|{comment}\n'
        file.write(line)

while True:
    show_menu()
    choice = input("Введите номер действия: ")

    if choice == '1':
        contacts = load_contacts()
        for contact in contacts:
            print(f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact['comment']}")
    elif choice == '2':
        id = input("Введите id: ")
        name = input("Введите имя: ")
        phone = input("Введите телефон:")
        comment = input("Введите комментарий: ")
        add_contact(id, name, phone, comment)
        print("Контакт добавлен!\n")
        contacts = load_contacts()
        for contact in contacts:
            print(f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact['comment']}")
    elif choice == "0":
        print("Выход из программы...")
        break
    else:
        print("Неверный выбор, попробуйте заново.")




