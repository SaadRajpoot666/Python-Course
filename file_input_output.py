print("Chapter Number 09")


#This is how we can read the file

f = open("README.md")
data = f.read()
print(data)
f.close()


#This is how we can write the file . Create a new file and add the data in it
str = '''hello how are you it's saad a MERN STACK DEVELOPER and Full Stack Enthausiast eager to learn full stack '''

# #opeing a file
# f = open("myfile.txt","w")
# #writing data
# f.write(str)
# #closing
# f.close()

#Other functions
f = open("myfile.txt","a")

