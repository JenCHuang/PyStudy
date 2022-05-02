# 猜數字遊戲: 終極密碼
import random
# Initial Condition
bl, bu = 1, 100
chance = 10
ans = random.randint(1,100)
exitl = ['exit','Exit','EXIT']

print(f'Please guess a integer number between 1~100. \n    You have {chance} chances ! (or "exit").')

i=1
while True:
    if i > chance: 
        print('Chances used out !!')
        break
    num=input(f'Input a number between {bl}~{bu} (round {i}) : ')
    if num in exitl: break
    i+=1
    if num.isdigit():
        num = int(num)      
        if num not in range(bl,bu+1):
            print(f"The number is not in range {bl}~{bu} !!")
        elif num>ans: 
            bu=num
            print(f'{bl}~{bu}')
        elif num<ans: 
            bl=num
            print(f'{bl}~{bu}')
        else:
            print('Bingo!!')
            break
    else:
        try:
            float(num)
            print(f'{num} is not an integer !!!!')
        except:
            print(f'Your input "{num}" is not even a number !!!!')
