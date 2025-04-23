from library import Library

def main():
    lib = Library()
    lib.load_from_file()
    menu = {
        "1": lambda: lib.add_book(input("Название: "), input("Автор: "), input("Год: "), input("Жанр: ")),
        "2": lambda: lib.remove_book(int(input("ID: "))),
        "3": lambda: lib.search_by_title(input("Название: ")),
        "4": lambda: lib.search_by_author(input("Автор: ")),
        "5": lib.show_all,
        "6": lambda: lib.give_book(int(input("ID: "))),
        "7": lambda: lib.return_book(int(input("ID: "))),
        "8": lib.save_to_file,
        "9": lib.show_taken,
    }

    while True:
        print("\n1. Добавить книгу\n2. Удалить книгу\n3. Поиск по названию книги\n4. Поиск по автору\n"
              "5. Показать все книги\n6. Выдать книгу\n7. Вернуть книгу\n8. Сохранить выбор\n9. Выданные книги\n0. Выход из программы")
        choice = input("Выбор: ")
        if choice == "0":
            print("До свидания!")
            break
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()
