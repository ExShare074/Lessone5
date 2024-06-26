class Warrior():
    def __init__(self, name, endurance, power, age):
        self.name = name
        self.endurance = endurance
        self.power = power
        self.age = age

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 3

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 2

    def hit(self):
        print(f"{self.name} сделал удар")
        self.endurance -= 7

    def walk(self):
        print(f"{self.name} бегает")

    def info(self):
        print(f"имя воина - {self.name}")
        print(f"выносливость - {self.endurance}")
        print(f"сила - {self.power}")
        print(f"возраст - {self.age}")

war1 = Warrior("Степа", 45, 62, 20)
war2 = Warrior("Егор", 50, 80, 29)

war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.info()

war2.sleep()
war2.eat()
war2.hit()
war2.walk()
war2.info()