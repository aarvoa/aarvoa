

print("Simple Calculator")
print("What would you like to do?:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

opt = input("Enter the number of your choice (1/2/3/4): ")
if int(opt) > 4:
    print("Oops. Invalid Option")
    exit(0)

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))



def add(a, b):
    return a + b

def subtract(a, b):
    check_nums(a,b)
    return a - b


def check_nums(num1,num2):
    if num1 < num2:
        print("Oops. The First Number is smaller than the Second Number")
        exit(0)


def multiply(a, b):
    return a * b

def divide(a, b):
    check_nums(a,b)
    return a / b


if opt == "1":
    ans = add(num1,num2)
    print("The Answer is ",ans)

elif opt == "2":
    ans = subtract(num1,num2)
    print("The Answer is ",ans)

elif opt == "3":
    ans = multiply(num1,num2)
    print("The Answer is ",ans)

elif opt == "4":
    ans = divide(num1,num2)
    print("The Answer is ",ans)

else:
    print("Oops. Invalid Option")