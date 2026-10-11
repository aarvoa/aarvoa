while True:
    num1 = input("Enter the first fraction: ")
    num2 = input("Enter the second fraction: ")
    choice = int(input("Select: \n 1.Add \n 2.Subtract \n"))

    num1_split = num1.split("/")
    num2_split = num2.split("/")

    if num1_split[1] == num2_split[1]:
        if choice == 1:
            new_zah = int(num1_split[0]) + int(num2_split[0])
        elif choice == 2:
            new_zah = int(num1_split[0]) - int(num2_split[0])
        else:
            print("Not a valid choice!")

        print(str(new_zah) + "/" + num1_split[1])
        
    else:
        zah_num1 = int(num1_split[0]) * int(num2_split[1])
        zah_num2 = int(num2_split[0]) * int(num1_split[1])
        nen = int(num1_split[1]) * int(num2_split[1])

        if choice == 1:
            sum_zah = zah_num1 + zah_num2
            sum
            print(str(sum_zah) + "/" + str(nen))
        elif choice == 2:
            dif_zah = zah_num1 - zah_num2
            print(str(dif_zah) + "/" + str(nen))

    
