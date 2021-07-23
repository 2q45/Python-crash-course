x = 0

print("Enter what toppings you would like enter enter quit when you want to stop")
while x < 6:
    x += 1
    topping = input(f"topping {x}:")
    if topping == "quit":
        x += 5
    else:
        print(f"you're topping {x} is {topping}")
    