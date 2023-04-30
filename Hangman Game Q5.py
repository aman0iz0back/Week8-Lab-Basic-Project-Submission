import random

print('\n\n----------------------Welcome to Game of Hangman!!----------------------\n')
nm = input('\nEnter your name: ')

x = ['python', 'computer', 'programming', 'algorithm', 'coding']
print(f"\n\tHello {nm} !! Let's start ... \nYou have to guess characters of random word given from this list",x)
print("\n\t...You have 6 turns to guess the word...")

y = random.choice(x)
z = '_' * len(y)
turns = 6
gd = []
hangman = [
    """
     _______
    |/      +
    |      
    |      
    |       
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      
    |       
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |       |
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      / 
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      / \\
    |
    """
]
while turns > 0 and '_' in z:
    print(f'\n\tWord: {z}')
    print(f'\n\tTurns left: {turns}')
    print(f'\n\tGuessed letters: {", ".join(gd)}')
    print(hangman[6-turns])
    g = input('\n\tGuess a letter: ').lower()
    if not g.isalpha() or len(g) != 1:
        print('\n\tInvalid input! Please enter a single letter.')
        continue
    if g in gd:
        print(f'\n\tYou already guessed {g}!')
        continue
    gd.append(g)
    if g in y:
        print(f'\n\tCorrect! {g} is in the word.')
        z = ''.join([c if c == g or z[i] != '_' else '_' for i, c in enumerate(y)])
    else:
        print(f'\n\tWrong! {g} is not in the word.')
        turns -= 1
if '_' not in z:
    print(f'\n\tCongratulations {nm}, you won! The word was {y}.')
else:
    print(f'\n\tSorry {nm}, you lost! The word was {y}.')
    print(hangman[6])
