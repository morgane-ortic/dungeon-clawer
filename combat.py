def attack(self, target):
    print(f"{self.name} attacks {target.name}")
    target.defend(self)

def defend(self, attacker):
    print(f"{self.name} defends against {attacker.name}'s attack")
    self.take_damage(10)

def take_damage(self, damage):
    self.health -= damage
    if self.health <= 0:
        print(f"{self.name} has been defeated!")
    else:
        print(f"{self.name} takes {damage} damage and has {self.health} health remaining")