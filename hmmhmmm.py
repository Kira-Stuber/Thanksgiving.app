
action = input("Do you want to add or view an entry?: ")

if action == "add" or action == "Add" or action == "add an entry" or action == "Add an entry":
    entry_num = int(input("How many entries do you want to add?: "))
    dict_entry = {}
    for x in range(entry_num):
        print()
        printX = x + 1
        printX = str(printX)
        print("Entry #" + printX)
        print()
        date = input("What is the date?: ")
        entry = input("I am thankful for... ")
        fullentry = date + ": I am thankful for " + entry
        dict_entry[x] = fullentry

i = int(input("Which entry do you want to see?: "))
i = i - 1
print(dict_entry[i])

if action == "view" or action == "View" or action == "view an entry" or action == "View an entry":
    i = int(input("Which entry do you want to see?: "))
    i = i - 1
    print(dict_entry[i])




"""
cooking = input("Are you cooking a turkey?: ")
if cooking == "yes" or cooking == "Yes":
    weight = float(input("What is its weight in pounds?: "))
    time = weight * 20
    if time % 1 == 0:
        time = int(time)
    time = str(time)
    print("You should cook the turkey for " + time + " minutes.")
"""