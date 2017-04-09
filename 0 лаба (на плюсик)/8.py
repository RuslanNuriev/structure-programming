a = []
for i in range(int(input('Введите количество эл-в массива '))):
    a.append(int(input('Новый эл-т массива: ')))

for elem in a[:-2]:
    print(elem, end=' ')
    if (((elem > 0) and ((elem + 1) > 0)) or ((elem < 0) and ((elem + 1 < 0)))):
        print(elem, "и", elem + 1, "стоят рядом и имеют одинаковый знак.")














