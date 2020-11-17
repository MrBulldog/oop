class Hero:
    def hero1(self, attack, health):
        self.attack = attack
        self.health = health

#Object/Instance
hero1 = Hero()
hero2 = Hero()

hero1.name = "Kardel"
hero1.health = 100


hero2.name = "venomancer"
hero2.health = 100

print(hero1)
print(hero1.__dict__)
print(hero1.name)