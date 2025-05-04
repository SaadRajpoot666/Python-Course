'''
1 for snake 
-1 for water
0 for gun
'''
computer = -1
youstr = input("Enter Your Choice: ")
youDict = {"s":1,"w":-1,"g":0} 
reverseDict = {1:"Snake",-1:"Water",0:"gun"}
you = youDict[youstr]

invertDict =   {"s":"Snake","w":"Water","g":"Gun"}

print(f"You Chose {invertDict[youstr]} and Computer Choose {reverseDict[computer]}")

if(computer == you):
    print("Draw")
elif(computer == -1 and you == 1):
    print("You Win!")
elif(computer == -1 and you == 0):
    print("You Loose!")
elif(computer == 1 and you == -1):
    print("You loose!")
elif(computer == 1 and you == 0 ):
    print("You win!")
elif(computer == 0 and you == -1):
    print("You win!")
elif(computer ==0 and you == 1):
    print("You Loose!")
else:
    print("Something went wrong")
