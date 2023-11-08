#1
class Homosapiens:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} ")


#2
class Person:

    def __init__(self, name):
        self.__name = name  # имя работника

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} ")

    def work(self):
        print(f"{self.name} работает")

#3
class Human:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} ")


class Personage(Person):

    def work(self):
        print(f"{self.name} работает")


p1 = Personage("Кирилл")
print(p1.name)
p1.display_info()
p1.work()

#4

class Man:
    def work(self):
        print("Кирилл работает")



class Student:
    def study(self):
        print("Кирилл учится")


class WorkingStudent(Man, Student):
    pass



s1 = WorkingStudent()
s1.work()
s1.study()

#5

class Humanoid:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"{self.name} работает")


class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def study(self):
        print(f"{self.name} учится")


class WorkingStudent(Person, Student):
    pass


ws = WorkingStudent("Дима")
ws.work()
ws.study()
