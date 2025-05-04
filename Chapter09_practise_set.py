import random
print("Chapter 09 Practise Set")


# Practise 1
f = open("poem.txt")
content = f.read()
if "TWINKLE" in content:
    print("Twinkle is Present in This Content")
else:
    print("Twinkle isn't in the content")

# Pracitse 2

def game():
    print("You are playing the game...")
    score = random.randint(1,50)
    #fetching high score 
    with open("hi_score.txt") as f:
        hi_score = f.read()
        if(hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0

    print(f"Your score is {score}")
    if(score>hi_score):
        #write the high score
        with open("hi_score.txt","w") as f:
            f.write(str(score))

    return score

game()


# Pracise 3
def generate_table(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"table/table_{n}.txt","w") as f:
            f.write(table)

for i in range(2,21):
    generate_table(i)


# Practise 4

word = "Donkey"
with open("myfile.txt") as f:
    content = f.read()

content_new = content.replace(word,"######")

with open("myfile.txt","w") as f:
        f.write(content_new)

# Practies 5
word = ["Donkey","bad","nice"]
with open("myfile.txt") as f:
    content = f.read()

content = content.replace(word,"#" * len(word))

with open("myfile.txt","w") as f:
        f.write(content)


# Pracise 6
with open("log.txt") as f:
    content = f.read()
    if("python" in content):
        print("Python is present in log file") 

#Pracise 7
lineno=1
with open("log.txt") as f:
    lines = f.readline()
    for line in lines:
        if("python" in lines):
            print(f"Python is present in line {line}")
            break 
        lineno += 1
    else:
            print("Python isn't present in the line")

#Pracise 8
with open("log.txt")as f:
    content = f.read()

with open("log-copy.txt","w") as f:
    f.write(content)