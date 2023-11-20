
dict_entry = {}
while True:
    action = input("Do you want to add or view an entry?: ")

    if action == "add" or action == "Add" or action == "add an entry" or action == "Add an entry":
        entry_num = int(input("How many entries do you want to add?: "))
        for x in range(entry_num):
            print()
            x = x + 1
            x = str(x)
            print("Entry #" + x)
            print()
            date = input("What is the date?: ")
            entry = input("I am thankful for... ")
            fullentry = date + ": I am thankful for " + entry
            dict_entry[date] = fullentry

        print()
        returnn = input("Do you want to return to the start?: ")
        if returnn == "yes" or returnn == "Yes":
            print()
            continue
        else:
            break

    elif action == "view" or action == "View" or action == "view an entry" or action == "View an entry":
        while True:
            False
            i = input("Which entry do you want to see? (date): ")
            if dict_entry == {}:
                print()
                print("That entry doesn't exist.")
                print()
            else:
                print()
                print(dict_entry[i])
                print()

            repeat = input("Do you want to review any other entries?: ")
            if repeat == "yes" or repeat == "Yes":
                True
            else:
                break      
        
        returnn = input("Do you want to return to the start?: ")
        if returnn == "yes" or returnn == "Yes":
            print()
            continue
        else:
            break

    else:
        break