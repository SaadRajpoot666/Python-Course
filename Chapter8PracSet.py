print("Chapter number 8 practise set")

#Practise Number # 1
def greatest(a,b,c): #function definition
    if(a>b and a>c):
        print("The Greatest Number is : ",a)
    elif(b>a and b>c):
        print("The Greatest Number is : ",b)
    else:
        print("The Greatest Number is : ",c)
        
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c= int(input("Enter Third Number: "))
greatest(a,b,c)        # function calling or function call

#Practise number 2
def temprature_converter(farenheit):
    celsius = 5*(farenheit - 32)/9
    
    print(f"The Temprature in Celsius is: {int(celsius)}")
    
d = int(input("Enter the temprature in fahrenheit: "))
temprature_converter(d)

#Practise Number 3
print("a")
print("b")
print("c",end="")
print("d",end="")

#Practise Number 4
def sum(n):
    if n==1:
        return 1
    return sum(n-1) + n

print(sum(4))

#Practise number 5
# ***
# **
# *
n=3
for i in range(n,0,-1):
    print("*"*i)

#Practise Numeber 6
e = float(input("Enter Inches: "))
def inches_to_cms(e):
    cms = e *2.54
    print(cms)

inches_to_cms(e)

#practise number 7
l = ["raza","saad","nabeel","and"]
def rem(l,word):
    n=[]  
    for i in l:
        if not(i == word):
            n.append(i.strip(word))
        return n

print(rem(l,"a"))

#Practise number 8
def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

multiply(3)