import random

class turtle():
    def __init__(self):
        self.power = 100
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)

    def move(self):
        new_x = self.x + random.choice([1,2,-1,-2])
        new_y = self.y + random.choice([1,2,-1,-2])

        if new_x > 10:
            self.x = 10 - (new_x - 10)
        elif new_x < 0:
            self.x = 0 - new_x

        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)

        self.power -= 1
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class fish():
    def __init__(self):
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)

    def move(self):
        new_x = self.x + random.choice([1,-1])
        new_y = self.y + random.choice([1,-1])

        if new_x > 10:
            self.x = 10 - (new_x - 10)
        elif new_x < 0:
            self.x = 0 - new_x

        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)

        return (self.x,self.y)

Turtle = turtle()
Fish = []
for i in range(10):
    new_fish = fish()
    Fish.append(new_fish)
while True:
    if not len(Fish):
        print("鱼被吃完了")
        break
    if not Turtle.power:
        print("没有体力了")
        break

    pos = Turtle.move()

    for each_fish in Fish[:]:
        if each_fish.move() == pos:
            Turtle.eat()
            Fish.remove(each_fish)
            print("一条鱼被吃掉了")

