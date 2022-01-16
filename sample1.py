import random

maked_num = random.random()

# print('maked_num')
# print(maked_num)

if maked_num < 0.2:
    print('大凶！')
elif 0.2 <= maked_num < 0.8:
    print('吉！')
elif 0.8 <= maked_num:
    print('大吉！')
