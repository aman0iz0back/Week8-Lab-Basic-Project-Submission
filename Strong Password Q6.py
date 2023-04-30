import random 
import string

print('\n\n----------------------Welcome to Strong Password Generator----------------------\n')

u = string.ascii_uppercase
l = string.ascii_lowercase
d = string.digits
pu = string.punctuation

ps = ''
n = int(input('\n How many characters you want in password (8/12):'))

if n == 8:
    u1 = random.choices(u,k=2)
    l1 = random.choices(l,k=2)
    d1 = random.choices(d,k=2)
    pu1 = random.choices(pu,k=2)
    psl = u1 + l1 + d1 + pu1
    for i in psl:
        ps = ps + i
elif n==9:
    u1 = random.choices(u,k=2)
    l1 = random.choices(l,k=2)
    d1 = random.choices(d,k=2)
    pu1 = random.choices(pu,k=3)
    psl = u1 + l1 + d1 + pu1
    for i in psl:
        ps = ps + i
elif n==10:
    u1 = random.choices(u,k=2)
    l1 = random.choices(l,k=2)
    d1 = random.choices(d,k=3)
    pu1 = random.choices(pu,k=3)
    psl = u1 + l1 + d1 + pu1
    for i in psl:
        ps = ps + i
elif n==11:
    u1 = random.choices(u,k=2)
    l1 = random.choices(l,k=3)
    d1 = random.choices(d,k=3)
    pu1 = random.choices(pu,k=3)
    psl = u1 + l1 + d1 + pu1
    for i in psl:
        ps = ps + i
elif n==12:
    u1 = random.choices(u,k=3)
    l1 = random.choices(l,k=3)
    d1 = random.choices(d,k=3)
    pu1 = random.choices(pu,k=3)
    psl = u1 + l1 + d1 + pu1
    for i in psl:
        ps = ps + i
else:
    print('Enter valid choice...')
    n = int(input('\n How many characters you want in password (8/12): '))

print('\n\t\t Generated password is: ',ps)
