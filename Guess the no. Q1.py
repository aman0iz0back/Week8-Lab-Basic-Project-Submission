import random

def fun(y):
    x = random.randint(1, 10)
    for i in range(5):
        ch = int(input("\t\tEnter a number between 1 and 10: "))
        if ch != x:
            print("\n\t\t\tWrong! Try again...\n")
            y -= 50
        else:
            print("\n\t\tCongratulations, you guessed it!\n")
            y += 100
            break
    else:
        print("\nGame over. The correct answer was", x)
        y = 0
    return y 

print('\n\n----------------------Welcome to Guess The Number----------------------\n\n')
print('Rule of the game: \n\t You have five chances to guess a number.\n\n')
y = 200
y = fun(y)
print("Final score:", y)
