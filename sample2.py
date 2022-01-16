import random

maked_num = random.random()

# print('maked_num')
# print(maked_num)

if maked_num < 0.25:
    print('\033[34m'+'大凶！'+'\033[0m')
elif 0.25 <= maked_num < 0.5:
    print('\033[33m'+'末吉！'+'\033[0m')
elif 0.5 <= maked_num < 0.75:
    print('\033[32m'+'吉！'+'\033[0m')
elif 0.75 <= maked_num:
    print('\033[31m'+'大吉！'+'\033[0m')
