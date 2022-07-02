list = ('python')

for i, x in enumerate(list, 1):  # i - индекс, x - значение элемента
                                # list - итерируемый объект,
                                # 1 - начальное значение индекса (отcчет будет с единицы, т.к. по умолчанию 0)
    print(i, x)




a = [1, 4, 2, -5, 0, 11]

for i, x in enumerate(a):
    if x % 2 == 0:
        a[i] += 1

#print(a)

for i, x in enumerate(a):
    if x % 2 == 1:
        a[i] += 1

#print(a)
