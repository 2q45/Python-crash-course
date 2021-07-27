Food = {}

active = True
while active:
    name = input("\nWhat is your name? ")
    response = input("What food do you want")
 
Food[name] = response
 
repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    active = False
 
    print("\n------------------Orders-------------------")
    for name, response in Food.items():
        print(f"{name} would like to climb {response}.")