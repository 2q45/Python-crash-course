height = input("How tall are you")
height = int(height)

if height > 23:
    print("you are tall enough to ride")
else:
    print("sorry you are too short")

toppings = []
prompt = "\nPlease enter what topping you would want "
prompt += "\n enter quit when you are finished "
toppings_num = 1 

while toppings_num < 6:
        topping = input(f"you're {toppings_num} topping would be"
        toppings_num += 1