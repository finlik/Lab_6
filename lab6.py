def convert(n):
    try:
        n = int(n)
    except Exception:
        return -1
    return n

n = 0
while n == 0:
    n = input('Введите количество критериев: ')
    n = convert(n)
    if n == -1 or n < 1:
        print ('Вы ввели неверное число или посторонний символ. Количество должно быть целым числом от 1 до 9.')
        n = 0 
               
a = [[0] * n for i in range(n)]

def criterion(table, n):
    for i in range(n):
        for j in range(n):
            if (i == j):
                table[i][j] = 1
            if (i < j):
                while table[i][j] == 0:
                    temp = input('Введите отношение критерия {0} к критерию {1}: '.format(i+1, j+1))
                    temp = convert(temp)
                    if (temp == -1) or (1 <= temp <= 9) == False: 
                        print('Вы ввели неверное число или посторонний символ. Отношение должно быть целым числом от 1 до 9.')
                    else:
                        table[i][j] = temp    
    for i in range(n):
        for j in range(n):
            if i > j:
                table[i][j]=1/table[j][i]
    return table

def matrix_s(table, n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += table[i][j]
    return s

def coef(table, n, s):
    array_coef = list()
    for i in range(n):
        coef_s = 0
        for j in range(n):
            coef_s += table[i][j]
        array_coef.append(coef_s/s)
    return array_coef

 
    
a = criterion(a,n)
a_s = matrix_s(a, n)
CF = coef(a, n, a_s)
print('Весовые коэффициенты: ', end=' ')
for cf in CF:
    print("{0:.2f}".format(cf), end=' ')

