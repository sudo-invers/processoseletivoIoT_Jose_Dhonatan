from machine import Pin, SoftI2C
import ssd1306


class Display:
    def __init__(self):
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

        self.oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    def draw_pet(self, pet):

        self.oled.fill(0)

        mood = pet.mood()

        if mood == "Happy":
            face = "^_^"

        elif mood == "Hungry":
            face = "T_T"

        elif mood == "Tired":
            face = "-_-"

        elif mood == "Sick":
            face = "x_x"

        else:  # Normal
            face = "o_o"

        self.oled.text(pet.name, 0, 0)
        self.oled.text(face, 45, 18)

        self.oled.text("F:" + str(pet.hunger), 0, 42)
        self.oled.text("E:" + str(pet.energy), 64, 42)

        self.oled.text("H:" + str(pet.health), 0, 54)

        self.oled.show()
