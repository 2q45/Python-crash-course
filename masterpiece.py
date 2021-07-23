coders = ["ishan","shreyash","ali","saahd","akshat"]
print(f"coders are {coders}")
for coder in coders:
    if coder == "akshat":
        print(f"but {coder} is not a coder")
    else:
        print(f"{coder} is a coder")
coders.pop()
print(f"coders are now: {coders}")
print("Akshat has been popped from the list")
    