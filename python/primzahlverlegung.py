while True:
    num = int(input("Enter a number!: "))
    div = 2
    factors = []

    while num > 1:
        if num % div == 0:
            factors.append(div)
            num = num // div
        else:
            div = div + 1

    print(factors)
