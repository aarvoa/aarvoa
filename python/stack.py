def is_balanced(exp:str):
    stack = []
    kvmap = {
            "(": ")",
            "[": "]",
            "<": ">",
            "{": "}"
    }
    if len(exp) % 2 != 0:
        return False
    else:
        for i in exp:
            if i in ["<", "(", "[", "{"]:
                stack.append(i)
            else:
                el = stack.pop()
                if kvmap[el] != i:
                    return False

        if len(stack) == 0:
            return True
while True:
    exp = input("Enter Expression: ")
    print(is_balanced(exp))