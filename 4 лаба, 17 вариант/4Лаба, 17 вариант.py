# задание 1
'''
a = input('Введите строку: ')
print(a)
while len(a) != 25:
    a = a + '_'
print('Допишем "_", чтобы было 25 символов: ',a)
'''

# задание 2
'''
a = input('Введите строку: ')
print(a)
for i in range(len(a)):
    if a[i] == '№':
        a = a[:i] + 'номер по порядку' + a[i+1:]
print('Каждый символ "№" заменен строкой "номер по порядку"', a)
'''

# задание 3
'''
a = input('Введите строку: ')
b = []
print(a)
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print('Разных символов в строке: ', len(b))
'''

# задание 4 (9.168)
'''
a = input('Введите предложение: ')
kn = 0
kp = 0
print(a)
for i in range(len(a)):
    if a[i] == ' ':
        if a[i-1] == 'р':
            kp += 1
        if a[i+1] == 'н':
            kn += 1
if a.startswith('н'):
    kn += 1
if a.endswith('р'):
    kp += 1
print('Количество слов, начинающихся с "н" =', kn)
print('Количество слов, оканчивающихся "р" =', kp)
'''
