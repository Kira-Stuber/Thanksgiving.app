
action = input("Do you want to add or view an entry?: ")

if action == "add" or action == "Add" or action == "add an entry" or action == "Add an entry":
    entry_num = int(input("How many entries do you want to add?: "))
    dict_entry = {}
    for x in range(entry_num):
        date = input("What is the date?: ")
        entry = input("I am thankful for... ")
        fullentry = date + ": I am thankful for " + entry
        dict_entry[x] = fullentry

    for i in dict_entry:
        print(f"Floor {i}: Rooms occupied = {dict_entry[i]}.")

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