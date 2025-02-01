class Stack:
    '''
    Класс для проверки правильности скобочной последовательности
    '''
    def __init__(self, line: str):
        self.line: str = line
        self.list_check: list = []

    def is_empty(self):
        '''
        Возвращает информацию о пустоте/наполненности списка
        :return: bool: True если список пуст, False eсли нет
        '''
        return len(self.list_check) == 0

    def check(self):
        '''
        Проверяет скобочную последовательность на правильность и возвращает соответствующую информацию
        :return: str: Информация о правильности скобочной последовательности
        
        '''
        for i in self.line:
            if i in ['(','[','{']:
                self.list_check.append(i)
            elif not self.is_empty():
                if self.list_check[-1] == '(' and i == ')':
                    self.list_check.pop()
                elif self.list_check[-1] == '[' and i == ']':
                    self.list_check.pop()
                elif self.list_check[-1] == '{' and i == '}':
                    self.list_check.pop()
                else:
                    self.list_check.append(i)
            else:
                self.list_check.append(i)
        if self.is_empty():
            return 'Последовательность правильная'
        elif not self.is_empty():
            return f'Неправильная последовательность, остались: {self.list_check}'
    


my = Stack(')))[[[]]]')
print(my.check())

my2 = Stack('((([[{{()}}]])))')
print(my2.check())