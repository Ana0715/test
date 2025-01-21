from enum import Enum

class Engine:
    '''
    Класс, представляющий двигатель машины
    '''
    def __init__(self, horsepower: int , fuel_type: str) -> None:
        '''
        Создание экземпляра класса Engine(Двигатель)
        :param horsepower: int: Мощность двигателя в лошадиных силах
        :param fuel_type: str: Тип топлива
        '''
        self.horsepower: int = horsepower
        self.fuel_type: str = fuel_type

    def display_engine_info(self) -> str:
        '''
        Возвращает информацию об экземпляре класса Engine(Двигатель)
        :return: str: Информация о мощности двигателя и типе топлива
        '''
        return f'Horsepower: {self.horsepower}, Fuel: {self.fuel_type}'


class CarBody:
    '''
    Класс, представляющий кузов машины
    '''
    def __init__(self, type_body: str, doors: int) -> None:
        '''
        Создание экземпляра класса CarBody(Кузов)
        :param type_body: str: Тип кузова
        :param doors: int: Количество дверей
        '''
        self.type_body: str = type_body
        self.doors: int = doors

    def display_carbody_info(self) -> str:
        '''
        Возвращает информацию об экземпляре класса CarBody(Кузов)
        :return: str: Информация о типе кузова и количестве дверей
        '''
        return f'Type body: {self.type_body}, Doors: {self.doors}'

class WheelRubber(Enum):
    '''
    Класс, представляющий типы резины колёс
    '''
    SUMMER = 'Летняя'
    UNIVERSAL = 'Универсальная'
    MUD_TERRAIN = 'Для бездорожья'

class Wheel:
    '''
    Класс, представляющий колесо автомобиля
    '''
    def __init__(self, diameter: float, rubber: WheelRubber) -> None:
        '''
        Создание экземпляра класса Wheel(Колесо)
        :param diameter: float: Диаметр колеса
        :param rubber: WheelRubber: Тип резины
        '''
        self.diameter: float = diameter
        self.rubber: WheelRubber = rubber

    def change_wheel_rubber(self, new_wheel_rubber: WheelRubber) -> str:
        '''
        Меняет тип резины колёс
        :param new_wheel_rubber: str: Новый тип резины колёс
        :return: str: Изменённый тип резины колёс
        :raises ValueError: Eсли текущий тип резины колёс Универсальный
        >>> wheel_1 = Wheel(diameter=15.5, rubber=WheelRubber.SUMMER)
        >>> wheel_1.change_wheel_rubber(new_wheel_rubber=WheelRubber.MUD_TERRAIN)
        <WheelRubber.MUD_TERRAIN: 'Для бездорожья'>
        >>> wheel_2 = Wheel(diameter=25.6, rubber=WheelRubber.UNIVERSAL)
        >>> wheel_2.change_wheel_rubber(new_wheel_rubber=WheelRubber.MUD_TERRAIN)
        Traceback (most recent call last):
        ...
        ValueError: Нельзя менять универсальный тип резины
        '''
        if self.rubber == WheelRubber.UNIVERSAL:
            raise ValueError('Нельзя менять универсальный тип резины')
        self.rubber = new_wheel_rubber
        return self.rubber

    def display_wheel_info(self) -> str:
        '''
        Возвращает информацию об экземпляре класса Wheel(Колесо)
        :return: str: Информация о диаметре колеса и типе резины
        '''
        return f'Diameter: {self.diameter}, Rubber: {self.rubber.value}'


class Car:
    '''
    Класс, представляющий автомобиль
    '''
    def __init__(self, horsepower: int, fuel_type: str, type_body: str, doors: int, diameter: float, rubber: WheelRubber) -> None:
        '''
        Создание экземпляра класса Car(Автомобиль)
        :param: horsepower: int: Мощность двигателя в лошадиных силах
        :param fuel_type: str: Тип топлива
        :param type_body: str: Тип кузова
        :param doors: int: Количество дверей
        :param diameter: float: Диаметр колеса
        :param rubber: WheelRubber: Тип резины
        '''
        self.engine = Engine(horsepower, fuel_type)
        self.carbody = CarBody(type_body, doors)
        self.wheel = Wheel(diameter, rubber)

    def display_engine_info(self) -> str:
        '''
        Возвращает информацию об экземпляре класса Engine(Двигатель)
        :return: str: Информация о мощности двигателя и типе топлива
        '''
        return self.engine.display_engine_info()

    def display_carbody_info(self) -> str:
        '''
        Возвращает информацию об экземпляре класса CarBody(Кузов)
        :return: str: Информация о типе кузова и количестве дверей
        '''
        return self.carbody.display_carbody_info()

    def display_wheel_info(self) -> str:
        '''
        Возвращает информацию об экземпляре класса Wheel(Колесо)
        :return: str: Информация о диаметре колеса и типе резины
        '''
        return self.wheel.display_wheel_info()

    def display_all_info(self) -> str:
        '''
        Возвращает информацию об экземпляре класса Car(Автомобиль)
        :return: str: Информация о мощности двигателя и типе топлива, о типе кузова и количестве дверей, о диаметре колеса и типе резины
        '''
        return f'All info: {self.display_engine_info()}, {self.display_carbody_info()}, {self.display_wheel_info()}'


car1 = Car(170, 'diesel', 'sedan', 4, 50.8, WheelRubber.SUMMER)
car2 = Car(120, 'petrol', 'hetchback', 2, 64.8, WheelRubber.UNIVERSAL)
car3 = Car(240, 'petrol', 'SUV', 4, 81.45, WheelRubber.MUD_TERRAIN)

print(car1.display_all_info())
print(car2.display_all_info())
print(car3.display_all_info())

print(car1.display_engine_info())
print(car1.display_carbody_info())
print(car1.display_wheel_info())

if __name__ == '__main__':
    import doctest
    doctest.testmod()