print("Chapter 6 Practise Set")

a1 = int(input("Enter the number :"))
a2 = int(input("Enter the number :"))
a3 = int(input("Enter the number :"))
a4 = int(input("Enter the number :"))

if(a1>a2 and a1 > a3 and a1> a4):
    print("Greater Number is a1:",a1)
    
elif(a2>a1 and a2 > a3 and a2> a4):
    print("Greater Number is a2:",a2)
    
elif(a3>a1 and a3 > a2 and a3> a4):
    print("Greater Number is a3:",a3)
    
elif(a4>a1 and a4 > a2 and a4> a3):
    print("Greater Number is a4:",a4)

total_percentage  = ((a1 + a2 +a3) / 300) * 100

if(total_percentage >= 40 and a1 >= 33 and a2 >= 33 and a3 >= 33):
    print("you are passed congrats!")
else:
    print("You are fail try your best in  next year")
input  = input("Enter the username: ")
if( len(input) <10):
    print("Your username is less than 10")
else:
    print("All is Well!")

name = input("Enter Your Name: ")
l = ["Saad","Nabeel","Raza"]

if(name in l ):
    print(" Your name is in the friendship list ")
else:
    print("Your are not friend")

marks = int(input("Enter the Marks: "))

if(marks >=90 and marks <=100):
    print("Ex")
elif(marks >=80 and marks <90):
    print("A")
elif(marks >=70 and marks <80):
    print("B")
elif(marks >=60 and marks <70):
    print("C")
elif(marks >=50 and marks <60):
    print("D")
else: print("fail")

postInput = input("Enter the Post : ")

if( "harry" in postInput or "Harry" in postInput):
    print("This is talking about harry")
