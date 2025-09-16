from model import ContactBook
from view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_contact_from_input(self):
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        comment = input("Введите комментарий: ")
        self.model.add_contact(name, phone, comment)
        print("Контакт добавлен!")

    def run(self):
        self.show_all_contacts()
        while True:
            print("Меню:")
            print("1 - Показать все контакты")
            print("2 - Добавить контакт")
            print("0 - Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.show_all_contacts()
            elif choice == "2":
                self.add_contact_from_input()
            elif choice == "0":
                print("Выход из программы.")
                break
            else:
                print("Неверный ввод, попробуйте снова.")

    def show_all_contacts(self):
        try:
            self.model.load_contacts()
            self.view.show_contacts(self.model.contacts)
        except Exception as e:
            print(f"Ошибка при загрузке или отображении контактов: {e}")
            pass
