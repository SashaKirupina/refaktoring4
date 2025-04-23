import json
from book import Book
from dataclasses import asdict

class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, title, author, year, genre):
        book = Book(title, author, year, genre, self.next_id)
        self.books.append(book)
        self.next_id += 1
        print(f"Книга '{title}' добавлена.")

    def remove_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                self.books.remove(b)
                print("Книга удалена.")
                return
        print("Книга не найдена.")

    def search_by_title(self, title):
        found = [b for b in self.books if title.lower() in b.title.lower()]
        if found:
            for b in found:
                print(f"{b.title} by {b.author} (ID: {b.id})")
        else:
            print("Книга не найдена.")

    def search_by_author(self, author):
        for b in self.books:
            if b.author.lower() == author.lower():
                print(f"{b.author}: {b.title}")

    def show_all(self):
        for b in self.books:
            print(f"{b.title} — {b.author} ({b.year}, {b.genre}) ID: {b.id}, Выдана: {b.taken}")

    def show_taken(self):
        for b in self.books:
            if b.taken:
                print(f"{b.title} (ID: {b.id}) — ВЫДАНА")

    def give_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                if b.taken:
                    print("Книга уже выдана.")
                else:
                    b.taken = True
                    print("Книга выдана.")
                return
        print("ID не найден.")

    def return_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                if not b.taken:
                    print("Книга не была выдана.")
                else:
                    b.taken = False
                    print("Книга возвращена.")
                return
        print("ID не найден.")

    def save_to_file(self, filename="library.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([asdict(b) for b in self.books], f, ensure_ascii=False, indent=2)
        print("Книги сохранены.")

    def load_from_file(self, filename="library.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self.books.append(Book(**item))
                    self.next_id = max(self.next_id, item['id'] + 1)
        except FileNotFoundError:
            print("Файл не найден. Начинаем с пустой библиотеки.")
