from pet import Pet
from buttons import Buttons
from display import Display
import time

print("Teste")  # For some reason, this is needed for the CI to work...

pet = Pet("Byte")
buttons = Buttons()
screen = Display()

UPDATE_INTERVAL = 3000  # 3000 ticks = 3 seconds
last_update = time.ticks_ms()

print("Cyber Pet started.")

screen.draw_pet(pet)

while pet.alive:
    now = time.ticks_ms()

    if time.ticks_diff(now, last_update) >= UPDATE_INTERVAL:
        pet.update()
        pet.show_status()
        screen.draw_pet(pet)
        last_update = now

    action = buttons.read()

    if action == "feed":
        pet.feed()
        screen.draw_pet(pet)

    elif action == "play":
        pet.play()
        screen.draw_pet(pet)

    elif action == "sleep":
        pet.sleep()
        screen.draw_pet(pet)

    time.sleep_ms(50)

print("Game Over.")
