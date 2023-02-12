class Mammal:
    """
            Документация на класс.
            Класс описывает модель млекопитающего.

            :param name: Имя млекопитающего.
            :param gender: Пол млекопитающего. 0 - мужской, 1 - женский.
            :param age: Возраст млекопитающего.

            Пример:
            >>> mammal = Mammal("Маркиз", 0, 4)  # инициализация экземпляра класса
            >>> print(mammal)
            A mammal Маркиз. Age 4. Gender is male.
            >>> repr(mammal)
            "Mammal(name='Маркиз', gender=0, age=4)"
        """

    def __init__(self, name: str, gender: int, age: int):
        self.name = name

        if not isinstance(gender, int):
            TypeError("gender must be an Integer.")
        if gender:
            ValueError("gender must be either 0 or 1.")

        self._gender = gender

        if not isinstance(age, int):
            TypeError("age must be an Integer.")
        self.age = age

    def __str__(self):
        return f"A mammal {self.name}. Age {self.age}. Gender is {'male' if self._gender == 0 else 'female'}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, gender={self._gender!r}, age={self.age!r})"

    @property
    def Gender(self) -> int:
        """
        Геттер для name. Protected метод - пол млекопитающего изменить нельзя.
        Примеры:
            >>> mammal = Mammal("Маркиз", 0, 4)  # инициализация экземпляра класса
            >>> mammal.Gender
            0
        """
        return self._gender

    @property
    def Name(self) -> str:
        """
        Геттер для name. Публичный метод - возможно переименовать млекопитающее.
        Примеры:
            >>> mammal = Mammal("Маркиз", 0, 4)  # инициализация экземпляра класса
            >>> mammal.Name
            'Маркиз'
        """
        return self.name

    @Name.setter
    def Name(self, name: str) -> None:
        """
        Сеттер для name.
        Примеры:
            >>> mammal = Mammal("Маркиз", 0, 4)  # инициализация экземпляра класса
            >>> mammal.Name = "Шаман"
            >>> mammal.Name
            'Шаман'
        """
        self.Name = name

    def noise(self) -> str:
        """ Метод, заставляющий млекопитающее говорить.

        Примеры:
            >>> mammal = Mammal("Маркиз", 0, 4)  # инициализация экземпляра класса
            >>> mammal.noise()
            'A mammal named Маркиз is making a noise.'
        """
        return f"A mammal named {self.name} is making a noise."

    def moving(self) -> str:
        """ Метод, заставляющий млекопитающее передвигаться.

                Примеры:
                    >>> mammal = Mammal("Маркиз", 0, 4)  # инициализация экземпляра класса
                    >>> mammal.moving()
                    'Маркиз is moving.'
                """
        return f"{self.name} is moving."

class Cat(Mammal):
    """
            Документация на класс.
            Класс описывает модель кота, унаследованный от класса Mammal.

            :param name: Имя кота
            :param gender: Пол кота. 0 - мужской, 1 - женский.
            :param age: Возраст кота.
            :param hair: Наличие шерсти у кота

            Пример:
                >>> cat = Cat("Маркиз", 0, 4, True)  # инициализация экземпляра класса
                >>> print(cat)
                A cat Маркиз. Age 4. Gender is male. Has hair.
                >>> repr(cat)
                "Cat(name='Маркиз', gender=0, age=4, hair=True)"
        """

    def __init__(self, name: str, gender: int, age: int, hair: bool):
        """ Инициализация экземпляра класса. """
        self.hair = hair
        super().__init__(name, gender, age)

    def __str__(self) -> str:
        return f"A cat {self.name}. Age {self.age}. Gender is {'male' if self._gender == 0 else 'female'}. {'Has hair' if self.hair else 'No hair'}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, gender={self._gender!r}, age={self.age!r}, hair={self.hair!r})"

    def noise(self) -> str:
        """ Метод, заставляющий кота мяукать.
        Примеры:
            >>> cat = Cat("Маркиз", 0, 4, True)  # инициализация экземпляра класса
            >>> cat.noise()
            'A cat named Маркиз is meowing.'
        """
        return f"A cat named {self.name} is meowing."


if __name__ == "__main__":
    pass