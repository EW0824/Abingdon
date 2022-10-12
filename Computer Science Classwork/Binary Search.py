


my_list = [1, 2, 5, 11, 238, 1024]
target = input("Input number to find")
found = False

While True:
    if target in my_list and my_list != []:
        middle_term = my_list[len(my_list)//2]
        if my_list[middle_item] == target:
            found = True
            break
        else:
            if my_list[middle_item] < target:
                my_list = my_list[middle_item+1:]
            else:
                my_list = my_list[:middle_item]

    else:
        print ("Reinput message")
