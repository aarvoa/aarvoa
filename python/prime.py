print("PrintPrimeOrNot!")
num = int(input("Write a number!: "))

if num == 0:
  print("Number 0 is not divisible or a prime number >:(")
  exit()


for i in range(2, num // 2):
  if num % i == 0:
    print("This number is not a prime number :(")
    exit()
print("The number is a prime number :)")