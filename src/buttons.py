from machine import Pin
import time


class Buttons:
    def __init__(self):

        self.feed_btn = Pin(14, Pin.IN, Pin.PULL_UP)

        self.play_btn = Pin(27, Pin.IN, Pin.PULL_UP)

        self.sleep_btn = Pin(26, Pin.IN, Pin.PULL_UP)

        self.last_press = 0

    def debounce(self):

        now = time.ticks_ms()

        if time.ticks_diff(now, self.last_press) < 250:
            return False

        self.last_press = now

        return True

    def read(self):

        if not self.feed_btn.value():
            if self.debounce():
                return "feed"

        if not self.play_btn.value():
            if self.debounce():
                return "play"

        if not self.sleep_btn.value():
            if self.debounce():
                return "sleep"

        return None
