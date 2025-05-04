print("Chapter 09 file I/0 using With")


# we can do the same exact thing using with 
f = open("myfile.txt")
print(f.read())
f.close() # This is very Heavy Therefore we use with 

#Using the above thing using with

with open("myfile.txt") as f:
    print(f.read())

#This is very easy and can't be heavy!