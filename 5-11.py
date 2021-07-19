print("ordinal numbers")
ordinal = [1,2,3,4,5,6,7,8,9]
for number in ordinal:
        if number == "1":
            print("{number}st")
        if number == "2":
            print("{number}nd")
        if number == "3":
            print("{number}rd")
        else:
            print("{number}th")