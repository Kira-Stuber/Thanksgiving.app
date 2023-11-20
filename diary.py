
dict_entry = {}
while True:
    action = input("Do you want to add or view an entry?: ")

    if action == "add" or action == "Add" or action == "add an entry" or action == "Add an entry":
        #allow the user to add multipule entries
        entry_num = int(input("How many entries do you want to add?: "))
        for x in range(entry_num):
            print()
            # print what entry the user is inputing
            x = x + 1
            x = str(x)
            print("Entry #" + x)
            print()
            # ask for the user's entry
            date = input("What is the date?: ")
            entry = input("I am thankful for... ")
            fullentry = date + ": I am thankful for " + entry
            # save each entry by date
            dict_entry[date] = fullentry

        # allow the user to choose to continue the progam
        print()
        returnn = input("Do you want to return to the start?: ")
        if returnn == "yes" or returnn == "Yes":
            print()
            continue
        else:
            break

    elif action == "view" or action == "View" or action == "view an entry" or action == "View an entry":
        while True:
            i = input("Which entry do you want to see? (date): ")
            #alert the user if they haven't made any entries yet
            if dict_entry == {}:
                print()
                print("That entry doesn't exist.")
                print()
            # retrieve entry by date
            else:
                print()
                print(dict_entry[i])
                print()

            #allow the user to view any other entries
            repeat = input("Do you want to review any other entries?: ")
            if repeat == "yes" or repeat == "Yes":
                continue
            else:
                break      
        
        # allow the user to choose to continue the progam
        returnn = input("Do you want to return to the start?: ")
        if returnn == "yes" or returnn == "Yes":
            print()
            continue
        else:
            break

    else:
        break