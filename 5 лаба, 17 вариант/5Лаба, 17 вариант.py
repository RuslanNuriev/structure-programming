# задание 1
'''
a = []
zero = 0
neg = 0
pos = 1
print('Заполните массив из 15 эл-в: ')
for i in range(0, 15):
    a.append(int(input()))
print(a)
for i in range(len(a)):
    if a[i] > 0:
        pos *= a[i]
    elif a[i] < 0:
        neg += 1
    else:
        zero += 1
print('Отрицательных:', neg, 'Нулевых:', zero, 'Произведение положительных:',pos)
'''

# задание 2
'''
a = []
k = 0
for i in range(int(input('Введите размер массива, а затем заполните его: '))):
    a.append(int(input()))
print(a)
for i in range(len(a)):
    if a[i] < a[i-1] and a[i] < a[i+1]:
        k += 1
print('Локальных минимумов в массиве', k)
'''

# задание 3
'''
a = int(input('Введите число: '))
k0 = bin(a)
k = []
x = 0
s1 = str
s2 = str
for i in range(2, len(k0)):  # избавляемся от "0b" в двоичной последовательности 
    k.append(k0[i])
s1 = ''.join(k) # преобразование массива "до" в строку
x = k[-1]
for i in range(len(k)-1, 0, -1):  # циклический сдвиг элементов массива вправо
    k[i] = k[i-1]
k[0] = x
s2 = ''.join(k) # преобразование массива "после" в строку
print(a,'в двоичной СС:',s1)
print('А это',a,'после циклического сдвига вправо:',s2)
s1 = int(s1, 2)
s2 = int(s2, 2)
print('Сумма чисел до и после преобразования в двоичной СС:',bin(s1+s2)[2:])
print('Сумма чисел до и после преобразования в десятиричнойй СС:',s1+s2)
'''

# задание 4
'''
import random
n = 10
m = 10
s = 0
a = [[random.randint(0,9) for j in range(m)] for i in range(n)] 
for row in a:                                                   
    print(' '.join([str(elem) for elem in row]))
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
    print('Сумма элементов',i+1,'строки:',s)
    s = 0
'''

# задание 5
'''
import random
n = 5
m = 5
s = 0
a = [[random.randint(-9,9) for j in range(m)] for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))
for row in a:
    for elem in row:
        if abs(elem) > s:
            s = elem
print('Максимальное по модулю в матрице:',s)
b = [[0 for j in range(m)] for i in range(n)]
print('Разделим матрицу поэлементно на максимальный:')
for i in range(5):
    for j in range(5):
        b[i][j] = a[i][j]/s
for row in b:
    print(' '.join([str(elem) for elem in row]))

'''

# задание 6
'''
import random
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
a = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        a[0][j] = 1
        a[i][0] = 1
        a[i][j] = a[i-1][j]+a[i][j-1]
for row in a:
    print(' '.join([str(elem).rjust(6) for elem in row]))
'''





