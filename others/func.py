def add_num(a, b):
    summe = a+b
    return summe

def speak():
    print("its a beautiful day")

def is_sunday():
    return False

def is_weekday(day):
    if day == "saturday"or day == "sunday":
        return False
    else:
        return True

def say_hello(name):
    print(f"hello {name}")


n = input("Enter your name: ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


say_hello(name=n)
ans = add_num(num1, num2) #add num is returning the answer
print(ans)
