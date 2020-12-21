

class Encapsulation:
    def __init__(self):
        self._protectedVar = 0 # Protected Variable
        self.__privateVar = 50 # Private Variable

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Encapsulation()
obj._protectedVar = 100
obj.getPrivate()
obj.setPrivate(150)
obj.getPrivate()
