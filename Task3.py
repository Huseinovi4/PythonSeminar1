# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.



cycled_0ff = True
print("Введите 6-ти значный номер билета")
while(cycled_0ff):
    numbers = input()
    if numbers.isdigit() == False:
        print("неверный тип данных введите пожалуйста число!")
    else:
        cycled_0ff = False
    if len(numbers) > 6:
        print("число содержит больше 6 цифр")
        cycled_0ff = False

num1 = int(numbers[0])+int(numbers[1])+int(numbers[2])
num2 = int(numbers[3])+int(numbers[4])+int(numbers[5])

if num1 == num2:
    print("Yes")
else:
    print("No")