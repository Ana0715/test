class Queue:
    '''
    Класс для добавления и удаления значений в списке
    '''
    def __init__(self):
        self.list: list = []

    def enqueue(self, item):
        '''
        Добавляет значение в список        
        '''
        self.list.append(item)

    def is_empty(self):
        '''
        Возвращает значение bool - пустой ли список
        :return: bool: True если пуст, False если нет
        '''
        return len(self.list) == 0

    def dequeue(self):
        '''
        Убирает первое значение из списка, только если он не пуст
        '''
        if not self.is_empty():
            self.list.pop(0)
        else:
            raise IndexError('Очередь пуста')

    def size(self):
        '''
        Возвращает длину списка
        :return: int: Длина списка
        '''
        return len(self.list)
    

my = Queue()
my.enqueue(1)
my.enqueue(2)
my.enqueue(3)
my.enqueue(4)
my.dequeue()
print(my.is_empty())
print(my.size())
print(my.list)