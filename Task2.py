cycle_off = True
while(cycle_off):
    number_of_cranes = input()
    if number_of_cranes.isdigit() == False:
        print("неверный тип данных, введите число!")
    else:
        cycle_off = False


Peter = int(number_of_cranes)/6
Sergey = int(number_of_cranes)/6
Katya = int(number_of_cranes)/6*4
print(Peter, " ", Katya, " ", Sergey)