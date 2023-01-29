class Book:
    """
    Базовый класс книги.
    """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError("Неверный тип данных для pages.")
        if pages < 0:
            raise ValueError("pages не может быть отрицательным.")

        self.pages = pages

    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}. Всего {self.pages} страниц."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        if not (isinstance(duration, float) or isinstance(duration, int)):
            raise TypeError("Неверный тип данных для duration.")
        if duration < 0:
            raise ValueError("duration не может быть отрицательным.")

        self.duration = duration

    def __str__(self):
        return f"Аудиокнига {self._name}. Автор {self._author}. Продолжительность {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"
