alien_0 = {"color":"green","points":"1"}
alien_1 = {"color":"yellow","points":"2"}
alien_2 = {"color":"red","points":"3"}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)


aliens = []
for alien_number in range(30):
    new_alien = {"color":"green", "points":"1", "speed":"naruto"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("aaaaqwdwed2ef")
print(f"total num of aliens: {len(aliens)}")


