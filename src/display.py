from machine import Pin, SoftI2C
import ssd1306
import time


class Display:
    def __init__(self):

        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

        self.oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    def draw_pet(self, pet):

        self.oled.fill(0)

        mood = pet.mood()

        if mood == "happy":
            face = "^_^"

        elif mood == "hungry":
            face = "T_T"

        elif mood == "tired":
            face = "-_-"

        elif mood == "sick":
            face = "x_x"

        else:  # Neutral
            face = "o_o"

        # Set the status to the user see what is happening
        self.oled.text(pet.name, 0, 0)

        self.oled.text(face, 45, 18)

        self.oled.text("F:" + str(pet.hunger), 0, 42)

        self.oled.text("E:" + str(pet.energy), 64, 42)

        self.oled.text("H:" + str(pet.health), 0, 54)

        self.oled.show()

    def draw_frame(self, frame):

        self.oled.fill(0)

        y = 0

        for line in frame:
            self.oled.text(line, 0, y)

            y += 8

        self.oled.show()

    def play_animation(self, frames, delay=400):

        for frame in frames:
            self.draw_frame(frame)

            time.sleep_ms(delay)
