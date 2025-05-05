print("Here we are learning OOPs")


# in oops we use objects and the objects are created by using class is same as class in js but syntax is different ok.
# It is the popular approach in programming

 

#first Class object
name = input("Enter Your Name: ")
age = int(input("Enter Your age: "))
Language = input("Enter Your Language: ")
class Employee:
    name = "Harry"
    age = 23
    language = "PYTHON"
 

 # any method starts from double underscore (__) is called dunder method and it doesn't require calling it automatically called
    def __init__(self , name, age): #now we don't need  data.name just pass aguments to employee
         self.age = age
         self.name = name 
         print("Hello it is dunder method ")




    def getinfo(self):
        print(f"The Name is {self.name} and the age is {self.age}")
    @staticmethod
    def greet(): #as here we don't need any element of class so we don't need self but without it it doesn't work. for this we use @statis method
            print("Good Morning")

data = Employee("Haris",34)
data.salary = 135000 # we can add data after too like this and is called instance attribute 
print(f'''
Name is : {data.name}
Age is : {data.age}
Language is : {data.language}
Salary is : {data.salary} 
# ''')
data.greet()
data.getinfo() 