class Bubble:
    def __init__(self, check_list: list):
        self.check_list = check_list

    def bubble_sort(self):
        n = 0
        for _ in self.check_list:
            try:
                if self.check_list[n] <= self.check_list[n+1]:
                    n += 1
                else:
                    self.check_list[n], self.check_list[n+1] = self.check_list[n+1], self.check_list[n]
                    self.bubble_sort()
                
            except:
                break


        return self.check_list




test_bubble_1 = Bubble([1, 4, 3, 8, 6, 5, 15, 19, 13, 0, 94, 85, 1, 1.5])
print('Отсортированный список:', test_bubble_1.bubble_sort())

my_list = [64, 34, 25, 12, 22, 11, 90]
test_bubble_2 = Bubble(my_list)
print('Отсортированный список:', test_bubble_2.bubble_sort())

