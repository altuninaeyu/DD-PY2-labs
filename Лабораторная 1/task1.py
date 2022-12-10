import doctest


class Cat:
    """
        Документация на класс.
        Класс описывает модель кота.

        :param Name: Имя кота
        :param has_hair: Наличие шерсти у кота
        :param Hungry: Голодный ли кот

        Пример:
        >>> cat = Cat("Маркиз", True)  # инициализация экземпляра класса
    """
    def __init__(self, name: str, has_hair: bool):
        """ Инициализация экземпляра класса. """

        if not isinstance(name, str):
            raise TypeError
        self.Name = name

        if not isinstance(has_hair, bool):
            raise TypeError
        self.has_hair = has_hair

        self.Hungry = True

    def meow(self):
        """ Метод, заставляющий кота мяукать.

            Примеры:
            >>> cat = Cat("Маркиз", True)  # инициализация экземпляра класса
            >>> cat.meow()
            Meow!
        """

        print("Meow!")

    def eat(self):
        """ Метод, кормящий кота.

            Примеры:
            >>> cat = Cat("Маркиз", True)  # инициализация экземпляра класса
            >>> cat.eat()
            Маркиз удачно покормлен!
        """

        self.Hungry = False
        print(f"{self.Name} удачно покормлен!")

    def shave(self):
        """ Метод, бреющий кота.

            Примеры:
            >>> cat = Cat("Маркиз", True)  # инициализация экземпляра класса
            >>> cat.shave()
            Маркиз удачно побрит!
        """

        if self.has_hair:
            self.has_hair = False
            print(f"{self.Name} удачно побрит!")
        else:
            print(f"{self.Name} уже лысый!")



class Student:
    """
        Документация на класс.
        Класс описывает модель студента.

        :param student_id: номер студента
        :param course_id: номер курса
        :param marks: Список оценок студента
        :param Average: Среднее всех оценок

        :raise ValueError: Оценка не может быть отрицательной или выше 5.

        Примеры:
        >>> student = Student(134, 453, [1, 4, 5, 3])  # инициализация экземпляра класса
        >>> print(student.Average)
        3.25
    """
    def __init__(self, student_id: int, course_id: int, marks):
        """ Инициализация экземпляра класса. """

        if not isinstance(student_id, int):
            raise TypeError
        self.student_id = student_id

        if not isinstance(course_id, int):
            raise TypeError
        self.course_id = course_id

        if not all([isinstance(i, int) for i in marks]):
            raise TypeError
        if not all([i>0 and i<=5 for i in marks]):
            raise ValueError("Оценка не может быть отрицательной или выше 5.")
        self.marks = marks

        self.Average = round(sum(self.marks)/len(self.marks), 2)

    def rewrite_marks(self, marks: [int]):
        """ Метод, изменяющий оценки студента.

        :param marks:
        :raise ValueError: Оценка не может быть отрицательной или выше 5.

        Примеры:
        >>> student = Student(134, 453, [1, 4, 5, 3])  # инициализация экземпляра класса
        >>> student.rewrite_marks([5, 4, 2, 5, 2])
        >>> print(student.Average)
        3.6
        """

        if not all([isinstance(i, int) for i in marks]):
            raise TypeError
        if not all([i > 0 and i <= 5 for i in marks]):
            raise ValueError("Оценка не может быть отрицательной или выше 5.")
        self.marks = marks

        self.Average = sum(self.marks) / len(self.marks)

    def Passed(self, passGrade) -> bool:
        """ Метод, проверяющий, сдал ли студент программу.

        :param passGrade: оценка, необходимая для сдачи курса.
        :raise ValueError: оценка, необходимая для сдачи курса, отрицательна или выше 5.

        :return Passed: Сдал ли студент курс.

        Пример:
        >>> student = Student(134, 453, [1, 4, 5, 3])  # инициализация экземпляра класса
        >>> student.Passed(4)
        False
        """

        if passGrade<0 or passGrade>5:
            raise ValueError("Оценка, необходимая для сдачи курса, отрицательна или выше 5.")

        if self.Average >= passGrade:
            Passed = True
        else:
            Passed = False
        return Passed



class Kettle:
    """
        Документация на класс.
        Класс описывает модель студента.

        :param capacity: объем чайника, мл
        :param occupied_capacity: объем, заполненной жидкостью, мл
        :param temperature: температура воды в чайнике, градус Цельсия

        :raise ValueError: Слишком много воды в чайнике.
        :raise ValueError: Слишком высокая температура.

        Примеры:
        >>> kettle = Kettle(1000, 450, 25)  # инициализация экземпляра класса
    """
    def __init__(self, capacity: int, occupied_capacity: int, temperature: int):
        """ Инициализация экземпляра класса. """

        if not isinstance(capacity, int):
            raise TypeError
        self.capacity = capacity

        if not isinstance(occupied_capacity, int):
            raise TypeError
        if occupied_capacity > capacity:
            raise ValueError("Слишком много воды в чайнике.")
        self.occupied_capacity = occupied_capacity

        if not isinstance(temperature, int):
            raise TypeError
        if temperature > 200:
            raise ValueError("Слишком высокая температура.")
        self.temperature = temperature

    def boil(self):
        """ Метод, подогревающий чайник.

        Пример:
        >>> kettle = Kettle(1000, 450, 25)  # инициализация экземпляра класса
        >>> kettle.boil()
        Вода нагрета до 95 градусов Цельсия.
        >>> print(kettle.temperature)
        95
        """
        if self.temperature > 95:
            print("Вода уже нагрета до 95 градусов Цельсия или выше.")
        else:
            print("Вода нагрета до 95 градусов Цельсия.")
            self.temperature = 95

    def fill(self, volume):
        """ Метод, добавляющий воду в чайник.

        :param volume: Объем, добавляемый в чайник.

        Пример:
        >>> kettle = Kettle(1000, 450, 25)  # инициализация экземпляра класса
        >>> kettle.fill(400)
        Объем в чайнике - 850 мл.
        """
        if not isinstance(volume, int):
            raise TypeError

        if volume+self.occupied_capacity > self.capacity:
            self.occupied_capacity = self.capacity
        else:
            self.occupied_capacity=volume+self.occupied_capacity

        print(f"Объем в чайнике - {self.occupied_capacity} мл.")

if __name__ == "__main__":
    doctest.testmod()
