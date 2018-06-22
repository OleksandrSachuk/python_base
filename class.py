class Enemy:
    life = 3

    def __init__(self, x):
        self.energy = x

    def attack(self):
        print('ouch!')
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print('Dead')
        else:
            print(str(self.life) + " life left")

    def get_energy(self):
        print(str(self.energy) + " energy")


enemy1 = Enemy(5)

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy1.checkLife()
enemy1.get_energy()
