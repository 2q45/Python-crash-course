
HK = {"China":"7 million"}
London = {"UK":"3 million"}
cities = ["HK","London"]
print("\n")

for location,population in HK.items():

    print(f"{cities[0]}:{population}")
    print(f"{cities[0]}:{location}")
print("\n")
for location,population in London.items():
    
    print(f"{cities[1]}:{population}")
    print(f"{cities[1]}:{location}")
print("\n")
