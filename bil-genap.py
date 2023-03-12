
for i in range(20,100,2):
    print(i)

num = int(input("Masukkan bilangan: "))

factorial = 1
if num < 0:
    print("Faktorial tidak dapat dihitung untuk bilangan negatif.")
elif num == 0:
    print("Faktorial dari 0 adalah 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Faktorial dari {} adalah {}.".format(num, factorial))
