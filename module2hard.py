x = False
while x == False:
    stoun1 = int(input("Введите число от 3 до 20: "))
    if stoun1 < 3 or stoun1 > 20:
        x = False
    else:
        x = True

ch = []
for i in range(1, stoun1 - 1):
    for j in range(i + 1, stoun1):
        if i + j == stoun1 or (stoun1 % i + j) == 0:
            ch.append([i, j])
print('Число', stoun1)
print('Пары чисел', ch)
