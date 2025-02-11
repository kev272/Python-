#Built in functions/Standard library functions

y = max(67,34,22,24,22,11)
print("The maximum value is", y)

x = min(12,32,43,44,1,12)
print("The minimum value is", x)

#User-defined Function
def name():
    print("Kevin")

name() #Calling a function

def multiply():
    x = 10
    y = 2
    print(x * y)
multiply()

#Parameters/Variable and arguments/Value
def add(a,b):
    print(a + b)
add(6,4)

def employee(name,gender,salary,age):
    print(name,gender,salary,age)
employee("Mark","Male","100000","30")
employee("Mary","Female","70000","27")
employee("John","Male","80000","32")
employee("Alex","Female","90000","29")
employee("Jerry","Male","50000","34")

#A program that displays details of 5 students
#Use a user-defined function with the help of parameters and arguments
def student(fullname,gender,course,age):
    print(fullname,gender,course,age)
    
student("Jemmy Ross","Male","MIT","19")
student("Timmy Benny","Male","Datascience","18")
student("John Frank","Male","Cybersecurity","17")
student("Jane Cherry","Female","MIT","19")
student("Alice Wonder","Female","Cybersecurity","20")



