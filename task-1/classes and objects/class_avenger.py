class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Gender      : {self.gender}")
        print(f"Super Power : {self.super_power}")
        print(f"Weapon      : {self.weapon}")
        print(f"Leader      : {self.is_leader()}")
        print("-" * 30)

    def is_leader(self):
        return "Yes" if self.leader else "No"
    
avengers = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield", True),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor", True),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")
]
for hero in avengers:
    hero.get_info()