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
        assert len(collector.books_genre) == 2

    def test_add_new_book_add_two_books_with_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector2 = BooksCollector()

        # добавляем две книги с указанием жанра
        collector2.add_new_book('Гордость и предубеждение и зомби')
        collector2.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector2.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector2.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        # проверяем, что две книги добавились в
        # словарь books_genre и у них указаны жанры
        assert collector2.books_genre == {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Комедии'
        }

    def test_get_book_genre_in_dict_books_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector3 = BooksCollector()

        # добавляем две книги с указанием жанра
        collector3.add_new_book('Кафе на краю земли')
        collector3.set_book_genre('Кафе на краю земли', 'Фантастика')
        collector3.get_book_genre('Кафе на краю земли')

        # проверяем, что у добавленной книги
        # указан жанр
        assert collector3.books_genre.get('Кафе на краю земли') == 'Фантастика'

    @pytest.mark.parametrize("a, expected",
                             [('Ужасы', "Гордость и предубеждение и зомби"), ("Фантастика", "Кафе на краю земли")])
    def test_get_books_with_specific_genre_with_different_options(self, a, expected):
        collector4 = BooksCollector()
        collector4.add_new_book('Гордость и предубеждение и зомби')
        collector4.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector4.add_new_book('Кафе на краю земли')
        collector4.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector4.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector4.set_book_genre('Кафе на краю земли', 'Фантастика')

        assert collector4.get_books_with_specific_genre(a)[0] == expected

    @pytest.mark.parametrize('a', ['Ужасы', 'Детективы', 'Мультфильмы'])
    def test_get_books_with_specific_genre_with_different_options_if_book_not_in_true(self, a):
        collector5 = BooksCollector()
        collector5.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector5.add_new_book('Кафе на краю земли')
        collector5.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector5.set_book_genre('Кафе на краю земли', 'Фантастика')

        assert collector5.get_books_with_specific_genre(a) == []

    def test_get_books_genre_with_books(self):
        collector6 = BooksCollector()
        collector6.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector6.add_new_book('Кафе на краю земли')
        collector6.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector6.set_book_genre('Кафе на краю земли', 'Фантастика')

        assert collector6.get_books_genre() == {'Что делать, если ваш кот хочет вас убить': 'Комедии',
                                                'Кафе на краю земли': 'Фантастика'}

    def test_get_books_for_children(self):
        collector7 = BooksCollector()
        collector7.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector7.add_new_book('Приключения Том и Джерри')
        collector7.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector7.set_book_genre('Приключения Том и Джерри', 'Мультфильмы')

        assert collector7.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить',
                                                       'Приключения Том и Джерри']

    def test_add_book_in_favorites_book_in_list(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Приключения Том и Джерри')
        collector8.set_book_genre('Приключения Том и Джерри', 'Мультфильмы')
        collector8.add_book_in_favorites('Приключения Том и Джерри')
        assert collector8.favorites[0] == 'Приключения Том и Джерри'

    def test_delete_book_from_favorites(self):
        collector9 = BooksCollector()
        collector9.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector9.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector9.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector9.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector9.favorites == []

    def test_get_list_of_favorites_books(self):
        collector10 = BooksCollector()
        collector10.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector10.add_new_book('Приключения Том и Джерри')
        collector10.add_new_book('Кафе на краю земли')
        collector10.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector10.set_book_genre('Приключения Том и Джерри', 'Мультфильмы')
        collector10.set_book_genre('Кафе на краю земли', 'Фантастика')

        collector10.add_book_in_favorites('Кафе на краю земли')
        collector10.add_book_in_favorites('Приключения Том и Джерри')
        assert collector10.get_list_of_favorites_books() == ['Кафе на краю земли', 'Приключения Том и Джерри']
