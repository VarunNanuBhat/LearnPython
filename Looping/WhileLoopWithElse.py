'''
Program to design a game to
guess a secret word within 7 chances
using while loop and else block.
'''

#Initializing variables
counter = 0
#The secret word
secret_word = "python"
#while loop
while counter < 7:
    doWhileVariable = False
    word = input("Enter the secret word: ")
    counter = counter + 1
    if word == secret_word:
        print("You guessed it right")
        break
else:
    print("better luck next time")


