print("Welcome!")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


factors = []
big = 0
small = 0

if num1 > num2:
    big = num1
    small = num2
else:
    big = num2
    small = num1

for i in range(1,small + 1):
    if big % i == 0 and small % i == 0:
        factors.append(i)

print(factors)
print(factors[-1])