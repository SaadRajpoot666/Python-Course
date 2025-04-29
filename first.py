# # import pyjokes
# # print("Hello World!")

# # # making joke 
# # joke= pyjokes.get_joke()
# # print(joke)
# print('''twinkle twinkle little start
# how i wonder that you are 
# up above the wonder sky
# like a diamond in the sky''')

import pyttsx3
engine = pyttsx3.init()

a = input("Enter the message: ")


engine.say(a)
engine.runAndWait()
print(1 + 1)