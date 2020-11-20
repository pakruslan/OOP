# 1) Студент
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”


# class Student:
#     def __init__(self,name,lastname,department,year_of_entrance):
#         self.name =  name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance
#         pass
#     def get_student_info(self):
#         print(f'{self.name} {self.lastname} postupil v {self.year_of_entrance} g. na facultet: {self.department}')
  

# Vasya = Student(name = 'Vasya',lastname = 'Petrov',department = 'Programming',year_of_entrance = 2020)
# Student.get_student_info(Vasya)       


# 2) Банковский счет
# Создайте класс BankAccount, в конструкторе которого определена переменная экземпляра класса
# balance = 0. Определите метод withdraw с параметром amount, который будет отнимать сумму от
# баланса и возвращать текущий баланс. Также добавьте метод deposit, который также имеет параметр
# amount и соответственно добавляет сумму к балансу, возвращает баланс.
# Примечание: баланс не может быть отрицательным!

# class BankAccount:
#     balance = 20
#     def withdraw(self,amount):
#           BankAccount.balance -= amount
#           if BankAccount.balance < 0:
#             BankAccount.balance = 0  
#             print(f'Your balance:{BankAccount.balance}')
#     def deposit(self,amount):
#         BankAccount.balance += amount
#         if BankAccount.balance > 0:
#             print(f'Your balance: {BankAccount.balance}')

# BankAccount.withdraw(BankAccount,amount = 300)
# BankAccount.deposit(BankAccount,amount = 352)


# 3) Самолет
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекта:
# • make (марка)
# • model
# • year
# • max_speed
# • odometer
# • is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте все методы
# класса.


class Airplane:
    is_flying = False
    land = True
    odometer = 0

    def __init__(self,made,model,year,max_speed):
        self.made = made 
        self.model = model 
        self.year = year
        self.max_speed = max_speed

    def take_off(self):

        self.is_flying = True
        self.land = False


    def fly(self,distance):
        self.odometer += distance 


    def landing(self):
        self.is_flying = False
        self.land = True



falcon_900 = Airplane(made= 'Falcon',model='Dassault Falcon 900',year='2010',max_speed='1000' )
falcon_900.take_off()
falcon_900.fly(1200)
falcon_900.landing()