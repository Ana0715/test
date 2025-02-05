class TaskQueue:
    '''
    Класс для представления очереди задач
    '''
    def __init__(self):
        self.list = []

    def add_task(self, task):
        '''
        Добавляет задачу в список
        '''
        self.list.append(task)

    def get_next_task(self):
        '''
        Если список не пуст возвращает первую задачу, если пуст возвращает None
        :return: str | None: Первая задача в списке или None
        '''
        if not self.is_empty():
            return self.list.pop(0)
        else:
            return None

    def is_empty(self):
        '''
        Возвращает информацию о пустоте списка
        :return: bool: True если пуст, False если нет
        '''
        return not self.list
    

class Task:
    '''
    Класс для представления задачи
    '''
    def __init__(self, name):
        self.name = name


queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)

next_task1 = queue.get_next_task()
print(f"Следующая задача: {next_task1.name if next_task1 else 'Нет задач'}")  # Ожидаемый результат: "Задача 1"

print(f"Очередь пуста: {queue.is_empty()}")  # Ожидаемый результат: False

next_task2 = queue.get_next_task()
print(f"Следующая задача: {next_task2.name if next_task2 else 'Нет задач'}")  # Ожидаемый результат: "Задача 2"

next_task3 = queue.get_next_task()
print(f"Следующая задача: {next_task3.name if next_task3 else 'Нет задач'}")  # Ожидаемый результат: "Задача 3"

next_task4 = queue.get_next_task() # Извлечь следующую задачу.
print(next_task4) # Ожидаемый результат: None
print(f"Следующая задача: {next_task4.name if next_task4 else 'Нет задач'}")  # Ожидаемый результат: "Нет задач"


print(f"Очередь пуста: {queue.is_empty()}")  # Ожидаемый результат: True

