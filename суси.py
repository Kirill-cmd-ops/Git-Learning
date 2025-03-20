`class Person:
__name = ""
__age = 0
def init (self, name, age):
self.__name = name
self.__age = age
print("Создан человек с именем", self.__name)
def del (self):
print("Удален человек с именем", self.__name)
def display_info(self):
print(f"Имя: {self.__name} Возраст: {self.__age}")
def say(self, message):
print(message)
@Property
def name(self):
return self.__name
@name.setter
def name(self, name):
self.__name = name
@Property
def age(self):
return self.__age
@age.setter
def age(self, age):
self.__age = age

класс Сотрудник(Человек):
__company = ""
def init (я, имя, возраст, компания):
super(). init (имя, возраст)
self.__company = компания
print("Создан человек с именем", self.name)
def del (self):
print("Удален человек с именем", self.name)
def work(self):
print(f"{self.name} работает в {self.__company}")
@Property
def company(self):
return self.__company
@company.setter
def company(self, company):
self.__company = company

human = Person("Том", 40)
slay = Employee("Боб", 20, "Google")
human.display_info()
slay.work()
`