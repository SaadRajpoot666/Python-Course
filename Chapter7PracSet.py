print("Chapter 7 Practise Set")

#Practise number 1 
# n = int(input("Enter the number : "))

# for i in range(0,10):
#     print(f"{i*n}")


#Practise number 2

# l = ["harry","sachin","soham","rahul"]

# for name in l:
#     if(name.startswith("s")):
#         print(f"hello {name}")


#Practise number 3

# i = 1
# e = int(input("Enter the Number : "))
# while(i<11):
#     print(f"{i*e}")
#     i+=1

#Practise number 4

# q = int(input("Enter the Number : "))

# for j in range(2,q):
#     if(q%j == 0 ):
#         print("Number isn't Prime")
#         break
# else:
#     print("Number is Prime")
    
#Practise number 5

# w = int(input("Enter the Number"))
# k=0
# sum = 0
# while(k<=w):
#     sum += k
#     k += 1

# print(sum)

# Practise number 6
# r = int(input("Enter the number : "))
# product  = 1
# for u in range(1,r+1):
#     product = product * u

# print(f"The factorial of {r} is {product}")

# Pracise number 7
# In this program we create the following pattern
#   *
#  ***
# *****
# p = int(input("Enter the number : "))
# for t in range(1,p+1):
#     print(" "* (p-t),end="")
#     print("*"* (2*t-1),end="")
#     print("\n")

# Pracise number 8
# In this program we create the following pattern
#*
#***
#*****

# a =int(input("Enter the Number : "))
# for s in range(1,a+1):
#     print("*"*s,end="")
#     print("\n")

# Pracise number 9
# In this program we create the following pattern
#***
#* *
#***
# n = int(input("Enter the Number: "))
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("*" * n)  # Top and bottom rows
#     else:
#         print("*" + " " * (n - 2) + "*")  # Middle rows with spaces


n = int(input("Enter the number : "))
for i in range(10,0,-1):
    print((n*i))   