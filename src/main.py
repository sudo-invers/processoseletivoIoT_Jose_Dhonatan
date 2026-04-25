from pet import Pet
from buttons import Buttons
import time

pet = Pet("Byte")  # He is just a little byte
buttons = Buttons()

UPDATE_INTERVAL = 3000
last_update = time.ticks_ms()  # 1 sec = 1000 ticks

print("Cyber Pet")

while pet.alive:
    now = time.ticks_ms()

    if time.ticks_diff(now, last_update) >= UPDATE_INTERVAL:
        pet.update()
        pet.show_status()
        last_update = now

    action = buttons.read()

    if action == "feed":
        pet.feed()

    elif action == "play":
        pet.play()

    elif action == "sleep":
        pet.sleep()

    time.sleep_ms(50)

print("Game Over.")
