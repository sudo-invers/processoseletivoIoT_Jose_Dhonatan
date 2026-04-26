class Pet:
    def __init__(self, name):

        self.name = name

        self.hunger = 50
        self.energy = 100
        self.happiness = 80
        self.health = 100

        self.age = 0

        self.alive = True

    def clamp(self):

        if self.hunger < 0:
            self.hunger = 0

        if self.hunger > 100:
            self.hunger = 100

        if self.energy < 0:
            self.energy = 0

        if self.energy > 100:
            self.energy = 100

        if self.happiness < 0:
            self.happiness = 0

        if self.happiness > 100:
            self.happiness = 100

        if self.health > 100:
            self.health = 100

    def feed(self):

        print("Feeding...")

        self.hunger -= 20
        self.happiness += 5

        self.clamp()

    def play(self):

        print("Playing...")

        self.happiness += 15
        self.energy -= 10
        self.hunger += 5

        self.clamp()

    def sleep(self):

        print("Sleeping...")
        if (self.hunger < 20 and self.happiness > 80 and self.energy > 10)
            self.health += 2

        self.energy += 25
        self.hunger += 5

        self.clamp()

    def update(self):

        self.age += 1

        self.hunger += 3
        self.energy -= 2
        self.happiness -= 1

        if self.hunger > 80:
            self.health -= 5

        if self.energy < 10:
            self.health -= 3

        if self.happiness < 10:
            self.health -= 2

        if self.health <= 0:
            self.alive = False  # And he dies ): the inevitable end

        self.clamp()

    def mood(self):

        if self.health < 30:
            return "sick"

        if self.hunger > 70:
            return "hungry"

        if self.energy < 20:
            return "tired"

        if self.happiness > 70:
            return "happy"

        return "normal"

    def show_status(self):

        print("------------------")
        print("Pet:", self.name)
        print("Age:", self.age)
        print("Mood:", self.mood())
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Happiness:", self.happiness)
        print("Health:", self.health)
        print("------------------")
