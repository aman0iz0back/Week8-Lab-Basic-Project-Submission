import random 

print('\n\n----------------------Welcome to Game of Rock Paper and Scissor----------------------\n\n')

x = 'Y'

while x == 'Y' or x == 'y':
    ch1 = random.choice(['Rock','Paper','Scissor'])
    ch2 = input('\nEnter your choice: ')
    if (ch1 == 'Rock' and ch2 == 'Scissor') or (ch1 == 'Paper' and ch2 == "Rock") or (ch1 == 'Scissor' and ch2 == 'Paper'):
        print('\n              Computer Wins... !!')
    elif ch1 == ch2:
        print("\n              It is a Tie Game...")
    else:
        print('\n              You Wins...')
    x = input("\nDo you want to continue(Y/N): ")
