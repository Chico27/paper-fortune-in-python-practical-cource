import random

maked_num = random.random()

# print('maked_num')
# print(maked_num)

if maked_num < 0.2:
    print('\033[34m'+'大凶！'+'\033[0m')
elif 0.2 <= maked_num < 0.8:
    print('\033[33m'+'吉！'+'\033[0m')
elif 0.8 <= maked_num:
    print('\033[31m'+'大吉！'+'\033[0m')
