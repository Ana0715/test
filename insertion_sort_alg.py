class Insertion:
    def __init__(self, check_list):
        self.check_list = check_list

    def check(self, n):
        for x in range(0, n):
            if self.check_list[x] > self.check_list[n]:
                self.check_list.insert(x, self.check_list.pop(n))

    def insertion_sort(self):
        n = 1
        for _ in self.check_list:
            if n < len(self.check_list):
                self.check(n)
                n+=1
        return self.check_list
                    
my_list = [64, 34, 25, 12, 22, 11, 90]
list_n = Insertion(my_list)
print("Отсортированный список:", list_n.insertion_sort())
