a = int (input('a='))
b = int (input('b='))
c = int (input('c='))
d = int (input('d='))
k = 0
if (a < b):
    for i in range(a, b+1):
        if (i%d == c):
            print(i)
            i += 1
            k += 1
        else:
            i += 1
    if k == 0:
        print("Таких чисел в диапазоне нет")
else:
    print("Диапазон задан некорректно.")