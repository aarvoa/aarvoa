print("PrintTeilerOrNot!")

while True:
    num = int(input("Enter a number: "))



    print("{",1, end = ";")

    for i in range(2, num // 2):
        if num % i == 0:
            print(i, end = ";")

    print(num,"}")