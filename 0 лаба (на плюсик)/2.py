a = int (input('a='))
b = int (input('b='))
c = int (input('c='))
if (a > b) and (a > c):
    print('Наибольшее - ', a)
elif (b > a) and (b > c):
    print('Наибольшее - ', b)
elif (c > a) and (c > b):
    print('Наибольшее - ', c)