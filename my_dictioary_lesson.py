class MyDict():
    '''
    Класс для создания словаря
    '''
    def __init__(self, dictionary=None) -> None:
        '''
        Создаёт список кортежей
        '''
        self.dictionary = dictionary if dictionary else []


    def __getitem__(self, wanted_key):
        '''
        Возвращает значение по ключу
        :return: Any: Значение, если ключ найден, иначе None
        '''
        for (key, value) in self.dictionary:
            return value if wanted_key == key else None


    def __setitem__(self, new_key, new_value) -> None:
        '''
        Добавляет в словарь пару {ключ : значение} или меняет текущее значение по ключу
        '''
        i = 0
        for (key, value) in self.dictionary:
            if new_key == key:
                self.dictionary[i] = (new_key, new_value)
                return self.dictionary
            i += 1
        self.dictionary.append((new_key, new_value))


    def __delitem__(self, del_key) -> None:
        '''
        Удаляет значение по ключу
        '''
        self.dictionary = [(key, value) for (key, value) in self.dictionary if key != del_key]


    def __contains__(self, found_key) -> bool:
        '''
        Возвращает True или False
        :return: bool: True, если текущий ключ есть в списке, False, если его нет
        '''
        return [found_key for (key, value) in self.dictionary if found_key == key]


    def keys(self) -> list:
        '''
        Возвращает все ключи, находящиеся в словаре
        :return: list: Список ключей словаря
        '''
        return [key for (key, value) in self.dictionary]
        

    def values(self) -> list:
        '''
        Возвращает все значения, находящиеся в словаре
        :return: list: Список значений словаря
        '''
        return [value for (key, value) in self.dictionary]
        

    def items(self) -> list[tuple]:
        '''
        Возвращает все ключи и значения, находящиеся в словаре
        :return: list[tuple]: Список кортежей ключей и значений словаря
        '''
        return [(key, value) for (key, value) in self.dictionary]
        

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
print('age' in my_dict_2)  # Вернет False

