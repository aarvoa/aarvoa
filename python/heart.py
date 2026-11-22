# Idea for M

for x in range(3):
    for y in range(13):
        if x == 0 and y in [2, 4, 8 , 10]:
            print("*", end = "")
        elif x == 1 and y in [1, 5 , 7, 11]:
            print("*", end = "")

        elif x == 2 and y in [0, 6, 12]:
            print("*", end = "")

        else:
            print("-", end = "")

    print("\n")

# Idea for V

for x in range(7):
    for y in range(13):
        if x == y or x + y == 12:
            print("*", end = "")
        else:
            print("-", end = "")

    print("\n")



