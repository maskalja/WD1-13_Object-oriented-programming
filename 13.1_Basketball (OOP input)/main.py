import json

class Player():
    def __init__(self, height_cm, weight_kg, points, rebounds):
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds

# Player stats
me = Player(input("Enter your height [cm]: "), input("Enter your weight [kg]: "), input("Enter your average points per game: "), input("Enter rebounds: "))
ld77 = Player(201, 104, 25.7, 8.4)
kd = Player(210, 102, 22, 6.2)
giannis = Player(211, 109, 26, 9.6)

# Test query
print("................................................................................")
print("My stats: {0} [cm], {1} [kg], average {2} points, average {3} rebounds per game.".format(me.height_cm, me.weight_kg, me.points, me.rebounds))
print("................................................................................")

# Write to and read from JSON
dict = {"me": me.__dict__, "ld77": ld77.__dict__, "kevin": kd.__dict__, "giannis": giannis.__dict__}

with open("stats.json", "w") as file:
    file.write(json.dumps(dict))

with open("stats.json", "r") as file:
    player_stats = json.loads(file.read())

for player in player_stats:
    print(player, "-----> Height [cm] =", player_stats[player]["height_cm"], "| Weight [kg] =", player_stats[player]["weight_kg"], "| Points =", player_stats[player]["points"], "| Rebounds =", player_stats[player]["rebounds"])
print("................................................................................")