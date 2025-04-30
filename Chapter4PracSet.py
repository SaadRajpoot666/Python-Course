print("Chapter 4 List and Tuples Practise Set")

#Practise number 1
fr1 = input("Enter Fruit 1: ")
fr2 = input("Enter Fruit 2: ")
fr3 = input("Enter Fruit 3: ")
fr4 = input("Enter Fruit 4: ")
fr5 = input("Enter Fruit 5: ")
fr6 = input("Enter Fruit 6: ")
fr7 = input("Enter Fruit 7: ")

fruits = [fr1,fr2,fr3,fr4,fr5,fr6,fr7]

print(fruits) # -> Done

# -> Practise number 2
marks = []
st1 = input("Enter Marks : ")
marks.append(st1)
st2 = input("Enter Marks : ")
marks.append(st2)
st3 = input("Enter Marks : ")
marks.append(st3)
st4 = input("Enter Marks : ")
marks.append(st4)
marks.sort()

print(marks) # -> Dooe

# Practise number 3

tuple1 = 1,2,4,"Harry"

tuple1[2] = "Saad"

# -> Practise number 4 

l = [42309,45432,543,435]
# sum is the built in function in python which is  used for sum 
print(sum(l))

# -> Pracise number 5

a = 1,0,3,7,0,5,9,0,0,0,0,0

n=a.count(0)
print(n)        