print("Functions and Recursions")

def avg(): #this whole part is called function definition means where we define the function that he has to do... 
    a = int(input("Enter the Number : "))
    b = int(input("Enter the Number : "))
    c = int(input("Enter the Number : "))
    sum = a + b + c
    average = sum / 3
    print(average)   

avg() # this part is called function call where we call the function and run the function

#Greeting function
nameInput = input("Enter Your Name : ")
def greet():
    print(f"Good Day {nameInput}")

if(not nameInput):
   print("Please first enter the name")
   nameInput = input("Enter Your Name : ")


else:
    greet()

def factorial(n):
    if(n==1 or n==0):
        return 1 
    return n * factorial(n-1)

n= int(input("Enter a Number : "))
print(f"The factorial of the given number is : {factorial(n)}")