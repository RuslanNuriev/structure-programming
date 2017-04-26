# задание 1 
'''
from math import sin
N = int(input('На сколько равноотстоящих отрезков вы хотите разбить отрезок [A, B]? (>2) '))
print('Введите точки А и В (А<В)')
A = float(input('Точка А: '))
B = float(input('Точка B: '))
ablen = B - A
k = ablen / N
H = 0
while H < ablen:
    x = 1 - sin(A+H)
    H = H + k
    print('F(x) в данной точке: ', x)
'''

# задание 2
'''
k = int(input('Введите k: '))
s = 0
p = int
W = 0
for i in range(-3, k+1):
    if (i != 0) and i-5 !=0:
        s += ((-1)**i)/((i-5)**2)
        n=i
        for n in range(n, k*2):
            if n!= 0 and n!=-4 and n**3 != 8:
                W += s * (n**3-8)/n+4 
print('W = ',W)
'''

# задание 3 
'''
def IsPrime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
res=[]
n=int(input('Введите натуральное число n: '))
for i in range(2, n+1):
  if IsPrime(i) == 1 and n%i == 0:
      res.append(i)
print(res)
'''

# задание 4
'''
N = int(input('Сколько учащихся в классе? '))
list = []
sum = 0
for i in range(1, N+1):
    list.append(int(input('Рост ученика равен: ')))
print(list)
for j in range(len(list)-1, -1, -1):
    sum += list[j]
sum = sum / N
print(sum)
'''

# задание 5
'''
print('Расходы > стипендии.')
A = int(input('Стипендия: '))
B = int(input('Расходы: '))
x = 0
k = B
summ = B
for i in range(1, 11):
    c = k + k * 0.03
    k = c
    summ += k
x = A*10 - summ
print('Нужно иметь',abs(x),'грн, чтобы выжить 10 месяцев')
'''


