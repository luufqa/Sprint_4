import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_without_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги без указания жанра
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две книги в
        # словарь books_genre, словарь имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_books_with_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги с указанием жанра
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        # проверяем, что две книги добавились в
        # словарь books_genre и у них указаны жанрыget_book_genre(self, name)
        assert collector.get_books_genre() == {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Комедии'
        }

    def test_get_book_genre_in_dict_books_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги с указанием жанра
        collector.add_new_book('Кафе на краю земли')
        collector.set_book_genre('Кафе на краю земли', 'Фантастика')

        # проверяем, что у добавленной книги
        # указан жанр
        assert collector.get_book_genre('Кафе на краю земли') == 'Фантастика'

    @pytest.mark.parametrize("genre, expected_book",
                             [('Ужасы', "Гордость и предубеждение и зомби"), ("Фантастика", "Кафе на краю земли")])
    def test_get_books_with_specific_genre_with_different_options(self, genre, expected_book):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Кафе на краю земли')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.set_book_genre('Кафе на краю земли', 'Фантастика')

        assert collector.get_books_with_specific_genre(genre)[0] == expected_book

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы', 'Мультфильмы'])
    def test_get_books_with_specific_genre_with_different_options_if_book_not_in_true(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Кафе на краю земли')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.set_book_genre('Кафе на краю земли', 'Фантастика')

        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_genre_with_books(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Кафе на краю земли')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.set_book_genre('Кафе на краю земли', 'Фантастика')

        assert collector.get_books_genre() == {'Что делать, если ваш кот хочет вас убить': 'Комедии',
                                               'Кафе на краю земли': 'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Приключения Том и Джерри')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.set_book_genre('Приключения Том и Джерри', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить',
                                                      'Приключения Том и Джерри']

    def test_add_book_in_favorites_book_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Том и Джерри')
        collector.add_book_in_favorites('Приключения Том и Джерри')
        book_in_favorit = collector.favorites[0]
        assert book_in_favorit == 'Приключения Том и Джерри'

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Приключения Том и Джерри')
        collector.add_new_book('Кафе на краю земли')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.set_book_genre('Приключения Том и Джерри', 'Мультфильмы')
        collector.set_book_genre('Кафе на краю земли', 'Фантастика')

        collector.add_book_in_favorites('Кафе на краю земли')
        collector.add_book_in_favorites('Приключения Том и Джерри')
        assert collector.get_list_of_favorites_books() == ['Кафе на краю земли', 'Приключения Том и Джерри']
