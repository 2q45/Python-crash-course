a = 0
b = 1
c = a + b
r = round(c/b, 11)
print(1)
while r != 1.61803398875:
        a = b
        b = c 
        c = a + b
        r = round(c/b,11)
        print(f"{c}\t{r}")
