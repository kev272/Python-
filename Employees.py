


class Employee:
    def __init__(self, name, salary,position):
        self.name = name
        self.salary = salary
        self.position = position

    def details(self):
        print(self. name,"is the",self.position)



employee1 = Employee("John",350000,"CEO")
print(employee1.name,employee1.salary,employee1.position)

employee2 = Employee("Ross",80000,"Manager")
print(employee2.name,employee2.salary,employee2.position)

employee3 = Employee("Johnny",60000,"Administrator")
print(employee3.name,employee3.salary,employee3.position)

employee4 = Employee("Jane",50000,"Accountant")
print(employee1.name,employee4.salary,employee4.position)




