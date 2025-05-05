#Practise 1
class two_d_vector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
        
class three_d_vector(two_d_vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
        
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
        

a = two_d_vector(1,2)
b = three_d_vector(1,2,3)
a.show()
b.show()


#Practise 2
class Animals:
    pass

class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("BOW BOW !")

c = Dog()
c.bark()


#Practise 3

class Employee:
    salary = 234
    increment = 20
    @property
    def salary_after_increment(self):
        return (self.salary + self.salary * (self.increment / 100))
    
    @salary_after_increment.setter
    def salary_after_increment(self,salary):
        self.increment = ((salary/self.salary) -1)*100
        

d = Employee()
d.salary_after_increment = 290
print(d.salary_after_increment)
print(d.increment)

#Practise #4

class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    
    def __add__(self,c2):
        return complex(self.r + c2.r,self.i + c2.i)
    
   
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = complex(1,2)
c2 = complex(3,4)
print(c1+c2)
 