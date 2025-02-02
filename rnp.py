class Stack:
    '''
    Класс для проведения операций над числами с использованием Обратной польской записи
    '''

    def __init__(self, *args):
        self.number = args
        self.number_list = []

    def formulas(self, a, b, operator):
        '''
        Устанавливает операцию, которую необходимо провести по выбранному оператору и возвращает результат
        :return: int | float: результат операции над числами
        '''

        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        else:
            return ValueError('Некорректный оператор')
        
    def check_is_number(self, i):
        '''
        Возвращает информацию о том, число ли это
        :return: bool: True если число, False если нет
        '''
        try:
            float(i)
        except ValueError:
            return False
        return True

    def operation_on_numbers(self):
        '''
        Возвращает результат после проведения операций по Обратной польской записи
        :return: int | float: Число - результат вычислений
        '''
        for arg in self.number:
            if self.check_is_number(arg):
                self.number_list.append(arg)
            elif arg in ['+' ,'-', '*', '/']:
                if len(self.number_list) > 1:
                    a = self.number_list.pop(-2)
                    b = self.number_list.pop(-1)
                    result = self.formulas(a, b, arg)
                    self.number_list.append(round(result, 2))
                else:
                    raise ValueError('Неверное количество значений')
            else:
                raise ValueError(f'Неверное значение: {arg}')
        return self.number_list

my = Stack(12, 54, 6, 8, 69, 7, 139, '*', '/', '+', '/', '-', '+')
print(my.operation_on_numbers())
