

from abc import ABC, abstractmethod
class firstClass(ABC):
    def parent(self, x):
        print("Abstract Class: ", x)
    @abstractmethod
    def task(self):
        print('This string is inside the "firstClass" task')

class secondClass(firstClass):
    def task(self):
        print('This string is inside of the "secondClass" task')

class thirdClass(firstClass):
    def task(self):
        print('This string is inside of the "thirdClass" task')

#Object of secondClass
second_obj = secondClass()
second_obj.task()
second_obj.parent("Example 1")


#Object of thirdClass
third_obj = thirdClass()
third_obj.task()
third_obj.parent("Example 2")
