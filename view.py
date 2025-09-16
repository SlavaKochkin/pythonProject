class View:
    def show_contacts(self, contacts):
        for contact in contacts:
            print(f'ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Комментарий: {contact.comment}')




