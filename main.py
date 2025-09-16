from controller import Controller
from model import ContactBook
from view import View

def main():
    model = ContactBook()
    view = View()
    controller = Controller(model, view)

    controller.show_all_contacts()
    controller.run()

if __name__ == "__main__":
    main()




