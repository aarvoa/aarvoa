

def summer(num):
    s = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        s = s + rem
    # print(s)
    return s

def div_by_three(num):
    total = summer(num)
    if total % 3 == 0:
        # print("Divisible by 3!")
        return True
    else:
        # print("Not divisable by 3!")
        return False

def div_by_two(num):
    rem = num % 10
    if rem % 2 == 0:
        # print("Divisible by two!")
        return True
    else:
        # print("Not divisible by two!")
        return False

def div_by_six(num):
    if div_by_two(num) and div_by_three(num):
        # print("Divisible by six!")
        return True
    else:
        # print("Not divisible by six!")
        return False

def div_by_nine(num):
    total = summer(num)
    if total % 9 == 0:
        return True
    else:
        return False

def div_by_seven(num):
    rem = num % 100
    num = num // 100
    rem = rem*2
    if (num - rem) % 7 == 0:
        return True
    else:
        return False

def div_by_five(num):
    rem = num % 10
    if rem == 0 or rem == 5:
        return True
    else:
        return False

def div_by_eight(num):
    rem = num % 1000
    if rem % 8 == 0:
        return True
    else:
        return False

    
while True:

    print("Welcome to DivisibleBy!")
    num = int(input("Tell me a number!: "))

    if div_by_three(num):
        print("Divisible by 3!")
    else:
        print("Not divisible by 3!")

    if div_by_two(num):
        print("Divisible by 2!")
    else:
        print("Not divisible by 2!")

    if div_by_six(num):
        print("Divisible by 6!")
    else:
        print("Not divisible by 6!")

    if div_by_nine(num):
        print("Divisible by 9!")
    else:
        print("Not divisible by 9!")

    if div_by_seven(num):
            print("Divisible by 7!")
    else:
        print("Not divisible by 7!")

    if div_by_five(num):
                print("Divisible by 5!")
    else:
        print("Not divisible by 5!")

    if div_by_eight(num):
        print("Divisible by 8!")
    else:
        print("Not divisible by 8!")

