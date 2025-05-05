print("Chapter 10 Practise Set")
from random import randint
#Problem 1
class Programmer:
    company = "Microsoft"

    def __init__(self,name, salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(f"This Name is {name} and salary is {salary} and the pincode is {pin}")
        
saad = Programmer("Saad",1200000,45726)

#Problem 2
class calculator:
    def __init__(self,n):
        self.n = n
  
    @staticmethod
    def greet():
        print("Hello")
    def square(self):
        print(f"The square is {self.n*self.n}")
    def square_root(self):
        print(f"The square root is {self.n**1/2}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

calculate  = calculator(4)
calculate.square()
calculate.square_root()
calculate.cube()
calculate.greet()


#Problem 3
#it is in problem 2 greeting function

#Problem 4

class Train:
    def __init__(self,train_no):
        self.train_no = train_no
    def book(self,fro,to):
        print(f"Ticket is Booked in train no {self.train_no} from {fro} to {to}")
    def get_status(self):
        print(f"Train number {self.train_no} is running and is on time")
    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.train_no} from {fro} to {to} is {randint(222,5555)}")

t = Train(12399)
t.book("Lahore","islamabad")