def one_grid():
    for i in range(5):
        print(i, end = " ")

def two_grid():
    for i in range(5):
        for j in range(5):
            print("*", end = " ")
        print("")


def triangle():
    for i in range(4):
        for j in range(i-1):
            print("*", end = "")
        print()

def main():
    # one_grid()
    # two_grid()
    triangle()

main()



