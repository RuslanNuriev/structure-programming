''' Задание 1 '''
'''
import math
y = float(input('Введите переменную y '))
N = 3*(y**2)+math.sqrt(y+1)
print('Ответ:', N)
'''

''' Задание 2 '''
'''
import math
y = float(input('Введите переменную y '))
n = float(input('Введите переменную n '))
H = ((y**2)-(0.8*y)+math.sqrt(y))/(23.1*(n**2)+math.cos(n))
print('Ответ: ', H)
'''

''' Задание 3 '''
'''
from math import log, atan, sqrt
a = float(input('Введите переменную a '))
b = float(input('Введите переменную b '))
x = float(input('Введите переменную x '))
y = float(input('Введите переменную y '))
T = (sqrt(x+b-a)+log(y))/(atan(b+a))
print('Ответ: ', T)
'''

''' Задание 4 '''
'''
import math
a = float(input("Введите длину большего основания а: "))
b = float(input("Введите длину меньшего основания b: "))
alpha = float(input("Введите угол при большем основании в градусах: "))
alphar = alpha*math.pi/180
print("Площадь трапеции равна ",(a**2-b**2)/4*math.tan(alphar))
'''

''' Задание 5 '''
'''
from math import log10, pow, fabs, sqrt, cos
x = 0.9
t = int(input('Введите переменную t: '))
b = pow(log10(fabs(x)), 2)
a = t*x+fabs(sqrt(b))
y = pow(cos(a+pow(b, 3)), 3)
print('b = lg²|x|')
print('b =', b)
print('a = tx+|√b|')
print('a =', a)
print('y = cos³(a+b³)')
print('y =', y)
'''

''' Здаание 6 '''
'''
from math import sqrt, pow
L = 0.7
m = 2
W = 4
w1 = W/(pow(m, 2)-1)
I = sqrt((2*w1)/L)
print('Энергия равна:', w1, 'Сила тока равна:', I)
'''
