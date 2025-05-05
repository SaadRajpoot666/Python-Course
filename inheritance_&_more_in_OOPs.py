print("Chapter 11 inheritance and more in OOPs")

# what is inheritace? 
# # inheritance in Python is an object-oriented programming concept where one class (called a child or subclass) inherits the properties and behaviors (like methods and attributes) from another class (called a parent or superclass). 🧬

# 💡 Why use inheritance?
# Code reuse – don't repeat code.

# Extensibility – easily add or modify features.

# Organization – logical class hierarchies.


# Types of inhertitance
# -> Single Inheritace
# -> Multiple Inheritance
# -> Multilevel Inheritance



#Single Inheritance Example
# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create an object of Dog
dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()   # Own method



# ->Multiple Inheritance Example
# Parent class 1
class Father:
    def skills(self):
        print("Father: Knows gardening")

# Parent class 2
class Mother:
    def skills(self):
        print("Mother: Knows cooking")

# Child class inheriting from both
class Child(Father, Mother):
    def own_skill(self):
        print("Child: Knows coding")

# Create object of Child
child = Child()
child.skills()     # Which parent's method gets called?
child.own_skill()



# ->Multilevel Inheritance Example

# Grandparent class
class Grandfather:
    def house(self):
        print("Grandfather: Owns a big house 🏠")

# Parent class inherits from Grandfather
class Father(Grandfather):
    def car(self):
        print("Father: Owns a car 🚗")

# Child class inherits from Father
class Son(Father):
    def bike(self):
        print("Son: Owns a bike 🏍️")

# Create object of Son
s = Son()
s.house()  # From Grandfather
s.car()    # From Father
s.bike()   # From Son


# super keyword we use. when we want that whenever we run the child constructor the parent will run too 
class Father:
    def show(self):
        print("Father: I love gardening 🌱")

class Son(Father):
    def show(self):
        super().show()  # Calling the parent class method
        print("Son: I love coding 💻")

# Create object of Son
s = Son()
s.show()


class Employee:
    a = 1
    def show(self):
        print(f"the value of a is {self.a}")

o = Employee()
o.a = 45
o.show() # it will show 45 but what if we want the default value of a? know came classmethod below is it's example

class Employe:
    b = 1
    @classmethod
    def show(cls):
        print(f"the value of a is {cls.b}")

d = Employe()
d.b = 45
d.show()


#propery decorates
class Circle:
    def __init__(self, radius):
        # Private variable (by convention)
        self._radius = radius

    # Getter method to access area (like a read-only property)
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

    # Getter method for radius
    @property
    def radius(self):
        return self._radius

    # Setter method to set radius with validation
    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Radius can't be negative ❌")
        else:
            self._radius = value
            print(f"Radius updated to {value} ✅")

# Create object
c = Circle(5)

# Access area and radius
print("Area:", c.area)
print("Radius:", c.radius)

# Try to update radius
c.radius = 10     # Valid
print("Area after update:", c.area)

c.radius = -5     # Invalid

# operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def show(self):
        print(f"({self.x}, {self.y})")

# Create two points
p1 = Point(2, 3)
p2 = Point(4, 5)

# Add them using +
p3 = p1 + p2  # This calls p1.__add__(p2)
p3.show()     # Output: (6, 8)

