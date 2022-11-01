'''
Program to design a game to
guess a secret word within 7 chances
using do-while loop and else block.
'''

#Initializing variables
counter = 0
doWhileVariable = True
#The secret word
secret_word = "python"
#while loop
while counter < 7 or doWhileVariable:
    doWhileVariable = False
    word = input("Enter the secret word: ")
    counter = counter + 1
    if word == secret_word:
        print("You guessed it right")
        break
else:
    print("better luck next time")


