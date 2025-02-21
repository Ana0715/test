class Selection:
    def __init__(self, check_list):
        self.check_list = check_list

    def selection_sort(self):
        n = len(self.check_list)
        for i in range(n):
            minimal = i
            for j in range(i+1, n):
                if self.check_list[j] < self.check_list[minimal]:
                    minimal = j
            self.check_list[i], self.check_list[minimal] = self.check_list[minimal], self.check_list[i]
        return self.check_list
                    
def checking():
    import random
    for _ in range(0, 1000):
        check_list = [random.randint(-100, 100) for _ in range(random.randint(0, 100))]
        sort = Selection(check_list)
        result = sort.selection_sort()
        assert result == sorted(check_list), f'{result} != {sorted(check_list)}'
    print('All tests passed successfully.')


my_list = [64, 34, 25, 12, 22, 11, 90]
list_n = Selection(my_list)
print("Отсортированный список:", list_n.selection_sort())
list_2 = Selection([1, 4, 3, 8, 6, 5, 15, 19, 13, 0, 94, 85, 1.5, -6, 1, 1])
print("Отсортированный список 2:", list_2.selection_sort())

checking()