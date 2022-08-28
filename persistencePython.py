# This is the link to this Python coding challenge
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)
def persistence(n):
    print(f'The given number is {n}')
    numlength = len(str(n))
    while numlength != 1:
        num = n
        # print(num)
        nstring = str(n)
        # print(nstring)
        # print(type(nstring))
        prod = 1
        for i in nstring:
            digit = int(i)
            prod *= digit
            num = prod
        print(f'product = {prod}')
        # print(num)
        numlength = len(str(num))
        # print(numlength)
        n = prod
    print(f'The final  persistent product is {n}')
persistence(999)
print('========')
persistence(39)