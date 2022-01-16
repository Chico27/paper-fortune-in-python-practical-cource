import random

maked_num = random.random()

# print('maked_num')
# print(maked_num)

if maked_num < 0.25:
    print('大凶！')
elif 0.25 <= maked_num < 0.5:
    print('末吉！')
elif 0.5 <= maked_num < 0.75:
    print('吉！')
elif 0.75 <= maked_num:
    print('大吉！')
