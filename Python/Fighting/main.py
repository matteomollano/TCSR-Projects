import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.level = 1

    def attack(self, enemy):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        enemy.health -= damage
        print(f"{self.name} attacked {enemy.name} for {damage} damage!")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health = min(100, self.health + heal_amount)
        print(f"{self.name} healed for {heal_amount} health!")

    def level_up(self):
        self.level += 1
        self.attack_power += 5
        print(f"{self.name} leveled up! Now at level {self.level}.")

    def check_status(self):
        print(f"{self.name} - Health: {self.health}, Attack Power: {self.attack_power}, Level: {self.level}")

# do code for character creation and fighting here ...