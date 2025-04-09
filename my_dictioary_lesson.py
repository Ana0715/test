class MyDict():
    '''
    Класс для создания словаря
    '''
    def __init__(self, dictionary:dict=None) -> None:
        '''
        Создаёт словарь, если его не было
        Если он есть, используется указанный
        '''
        self.dictionary: dict = dictionary if dictionary else {}


    def __getitem__(self, key):
        '''
        Возвращает значение по ключу
        :return: Any: Значение, если ключ найден в словаре, иначе None
        '''
        return self.dictionary.get(key, None)


    def __setitem__(self, key, value) -> None:
        '''
        Добавляет в словарь пару {ключ : значение}
        '''
        self.dictionary[key] = value


    def __delitem__(self, key) -> None:
        '''
        Удаляет и возвращает значение по ключу
        '''
        if self.dictionary[key]:
            self.dictionary.pop(key)


    def __contains__(self, key) -> bool:
        '''
        Возвращает True или False
        :return: bool: True, если текущий ключ есть в списке, False, если его нет
        '''
        return key in self.dictionary


    def keys(self) -> list:
        '''
        Возвращает все ключи, находящиеся в словаре
        :return: list: Список ключей словаря
        '''
        return [key for key in self.dictionary.keys()]
        

    def values(self) -> list:
        '''
        Возвращает все значения, находящиеся в словаре
        :return: list: Список значений словаря
        '''
        return [value for value in self.dictionary.values()]
        

    def items(self) -> list[tuple]:
        '''
        Возвращает все ключи и значения, находящиеся в словаре
        :return: list[tuple]: Список кортежей ключей и значений словаря
        '''
        return [(key, value) for key, value in self.dictionary.items()]
        

    def __str__(self) -> str:
        return f'My dict: {self.dictionary}'
        



my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict)  # Вернет весь словарь
print(my_dict['name'])  # Вернет 'Alice'
print(my_dict.items()) # Вернет список с кортежами из ключей и их значений
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print('city' in my_dict)  # Вернет False
print('name' in my_dict)  # Вернет True




my_dict_2 = MyDict()
my_dict_2['name'] = 'Kate'
my_dict_2['age'] = 27
my_dict_2['city'] = 'Kaliningrad (Konigsberg)'
print(my_dict_2)  # Вернет весь словарь
print(my_dict_2['name'])  # Вернет 'Kate'
print(my_dict_2.items()) # Вернет список с кортежами из ключей и их значений
del my_dict_2['age']
print(my_dict_2.keys())  # Вернет ['name', 'city']
print(my_dict_2.values())  # Вернет ['Kate', 'Kaliningrad (Konigsberg)']
print('city' in my_dict_2)  # Вернет True
print('name' in my_dict_2)  # Вернет True

