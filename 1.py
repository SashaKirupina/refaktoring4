import json

books = [] #список всех книг
all_ids = [] #все ID книг
books_that_are_taken_now = [] #список ID выданных книг

def add_book(a, b, c, d): #добавляем книгу и ID
    iddd = len(all_ids) + 1
    book = {}
    book['title'] = a
    book['author'] = b
    book['year'] = c
    book['genre'] = d
    book['id'] = iddd
    book['taken'] = False
    books.append(book)
    all_ids.append(iddd)
    print("Книга с названием " + a + " добавлена")

def remove_the_book_by_id(the_id_thing): #удаления книги по ID
    for i in range(0, len(books)):
        if books[i]['id'] == the_id_thing:
            del books[i]
            print("Книга удалена")
            return
    print("Книга не найдена")

def find_book_with_title(tit): #поиск книги по названию
    found = []
    for i in range(0, len(books)):
        if tit.lower() in books[i]['title'].lower():
            found.append(books[i])
    if len(found) > 0:
        for x in found:
            print("Найденная книга:", x['title'], "by", x['author'], "(ID:", x['id'], ")")
    else:
        print("Книга не найдена")

def book_find_by_author_name(authorname): #поиск книги по автору
    for i in range(0, len(books)):
        if books[i]['author'].lower() == authorname.lower():
            print("Книга", authorname, ":", books[i]['title'])
            continue

def display_all_books_with_stupid_format(): #отображение всех книг
    print("------------")
    for i in range(0, len(books)):
        print("Книга:", books[i]['title'])
        print("Автор:", books[i]['author'])
        print("Год выпуска:", books[i]['year'])
        print("Жанр:", books[i]['genre'])
        print("ID:", books[i]['id'])
        print("Книга выдана?", books[i]['taken'])
        print("------------")

def give_book_to_person(book_id): #выдача книг по ID
    for i in range(0, len(books)):
        if books[i]['id'] == book_id:
            if books[i]['taken'] == True:
                print("Извините, эту книгу забрали")
                return
            books[i]['taken'] = True
            books_that_are_taken_now.append(book_id)
            print("Книга выдана")
            return
    print("ID не найден")

def bring_book_back_from_person(book_id): #возврат книги
    for i in range(0, len(books)):
        if books[i]['id'] == book_id:
            if books[i]['taken'] == False:
                print("Книгу не брали")
                return
            books[i]['taken'] = False
            if book_id in books_that_are_taken_now:
                books_that_are_taken_now.remove(book_id)
            print("Книга возвращена")
            return
    print("ID не найден")

def do_the_saving_to_file_thing(): #сохранение книг в файл
    with open("somebooksfile.json", "w") as f:
        json.dump(books, f)
    print("Книги сохранены")

def load_data_back_from_file_or_fail_gracefully_if_file_missing(): #загрузка книг из файла
    global books
    try:
        with open("somebooksfile.json", "r") as f:
            books = json.load(f)
            for i in books:
                all_ids.append(i['id'])
                if i['taken']:
                    books_that_are_taken_now.append(i['id'])
    except:
        print("Файл не найден, начинаю с пустого списка")

def show_only_taken_books(): #показ взятых книг
    for i in range(0, len(books)):
        if books[i]['taken'] == True:
            print("Взятые:", books[i]['title'], "by", books[i]['author'], "(ID:", books[i]['id'], ")")

def main_thing_function_loop_do_everything_here(): #основной цикл программы
    load_data_back_from_file_or_fail_gracefully_if_file_missing()
    while True:
        print("1: Добавить книги")
        print("2: Удалить книги")
        print("3: Поиск по названию книги")
        print("4: Поиск по автору")
        print("5: Показать все книги")
        print("6: Выдать книгу")
        print("7: Вернуть книгу")
        print("8: Сохранить выбор")
        print("9: Выданные книги")
        print("0: Выход из программы")
        x = input("Выбор: ")
        if x == "1":
            a = input("Название: ")
            b = input("Автор: ")
            c = input("Год: ")
            d = input("Жанр: ")
            add_book(a, b, c, d)
        elif x == "2":
            theid = int(input("Enter book ID: "))
            remove_the_book_by_id(theid)
        elif x == "3":
            title = input("Enter title: ")
            find_book_with_title(title)
        elif x == "4":
            auth = input("Author name: ")
            book_find_by_author_name(auth)
        elif x == "5":
            display_all_books_with_stupid_format()
        elif x == "6":
            idd = int(input("Book ID to give: "))
            give_book_to_person(idd)
        elif x == "7":
            idd = int(input("Book ID to return: "))
            bring_book_back_from_person(idd)
        elif x == "8":
            do_the_saving_to_file_thing()
        elif x == "9":
            show_only_taken_books()
        elif x == "0":
            print("Bye.")
            break
        else:
            print("What even is that command?")

main_thing_function_loop_do_everything_here()