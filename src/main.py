from pet import Pet
from buttons import Buttons
from display import Display
from animations import EAT_ANIMATION, PLAY_ANIMATION, SLEEP_ANIMATION
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

    # Periodic pet update
    if time.ticks_diff(now, last_update) >= UPDATE_INTERVAL:
        pet.update()

        pet.show_status()

        screen.draw_pet(pet)

        last_update = now

    action = buttons.read()

    if action == "feed":
        # Play apple animation
        screen.play_animation(EAT_ANIMATION, delay=600)

        # Apply game logic
        pet.feed()

        # Return to main screen
        screen.draw_pet(pet)

    elif action == "play":
        # Play ball animation
        screen.play_animation(PLAY_ANIMATION, delay=400)

        pet.play()

        screen.draw_pet(pet)

    elif action == "sleep":
        # Play sleep scene
        screen.play_animation(SLEEP_ANIMATION, delay=800)

        pet.sleep()

        screen.draw_pet(pet)

    # Small loop delay
    time.sleep_ms(50)


pet.show_status()

print("Game Over.")
