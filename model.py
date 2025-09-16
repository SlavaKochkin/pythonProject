

class Contact:

    def __init__(self, id, name, phone, comment):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment

class ContactBook:

    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def add_contact(self, name, phone, comment):
        if not self.contacts:
            print('Сначала загрузите контакты через load_contacts()')
            return
        new_id = str(len(self.contacts) + 1)
        contact = Contact(new_id, name, phone, comment)
        self.contacts.append(contact)

        with open('data.txt', 'a', encoding='utf=8') as file:
            file.write(f"{contact.id}|{contact.name},{contact.phone}, {contact.comment}\n")


    def load_contacts(self, filename='data.txt'):
        self.contacts = []
        for contact in self.contacts:
            print(f'{contact.id}, {contact.name}, {contact.phone}, {contact.comment}')
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|')
                while len(parts) < 4:
                    parts.append('')

                contact = Contact(parts[0], parts[1], parts[2], parts[3])
                self.contacts.append(contact)

