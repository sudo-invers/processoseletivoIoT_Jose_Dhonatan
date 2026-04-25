# MicroPython SSD1306 driver

# Main references used:
# https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
# https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/
# https://github.com/TimHanewich/MicroPython-SSD1306
# And some help from AI, making this has hard.

from micropython import const
import framebuf

# SSD1306 command set (datasheet commands)
SET_CONTRAST = const(0x81)
SET_ENTIRE_ON = const(0xA4)
SET_NORM_INV = const(0xA6)
SET_DISP = const(0xAE)

SET_MEM_ADDR = const(0x20)
SET_COL_ADDR = const(0x21)
SET_PAGE_ADDR = const(0x22)

SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP = const(0xA0)

SET_MUX_RATIO = const(0xA8)
SET_COM_OUT_DIR = const(0xC0)
SET_DISP_OFFSET = const(0xD3)
SET_COM_PIN_CFG = const(0xDA)

SET_DISP_CLK_DIV = const(0xD5)
SET_PRECHARGE = const(0xD9)
SET_VCOM_DESEL = const(0xDB)

SET_CHARGE_PUMP = const(0x8D)


class SSD1306(framebuf.FrameBuffer):
    """
    Base SSD1306 display driver.

    Inherits from FrameBuffer so drawing functions like:
      - pixel()
      - line()
      - text()
      - fill()

    are available automatically.
    """

    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc

        # Display is organized in memory pages.
        # Each page is 8 pixels tall.
        self.pages = height // 8

        # Allocate framebuffer
        self.buffer = bytearray(self.pages * width)

        # Initialize framebuffer using vertical least significant bit mode
        super().__init__(self.buffer, width, height, framebuf.MONO_VLSB)

        self.init_display()

    def init_display(self):
        """
        Send SSD1306 initialization sequence.
        Configures addressing mode, contrast,
        multiplex ratio, charge pump, and turns display on.
        """

        for cmd in (
            SET_DISP,  # Display OFF
            SET_MEM_ADDR,
            0x00,  # Horizontal addressing mode
            SET_DISP_START_LINE,
            SET_SEG_REMAP | 0x01,
            SET_MUX_RATIO,
            self.height - 1,
            SET_COM_OUT_DIR | 0x08,
            SET_DISP_OFFSET,
            0x00,
            SET_COM_PIN_CFG,
            0x02 if self.height == 32 else 0x12,
            SET_DISP_CLK_DIV,
            0x80,
            SET_PRECHARGE,
            0x22 if self.external_vcc else 0xF1,
            SET_VCOM_DESEL,
            0x30,
            SET_CONTRAST,
            0xFF,
            SET_ENTIRE_ON,
            SET_NORM_INV,
            SET_CHARGE_PUMP,
            0x10 if self.external_vcc else 0x14,
            SET_DISP | 0x01,  # Display ON
        ):
            self.write_cmd(cmd)

        # Clear screen on startup
        self.fill(0)
        self.show()

    def poweroff(self):
        """Turn display OFF."""
        self.write_cmd(SET_DISP)

    def poweron(self):
        """Turn display ON."""
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        """Set display contrast (0-255)."""
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        """Enable or disable inverted colors."""
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        """
        Push framebuffer contents to OLED.
        Copies local RAM buffer to display memory.
        """

        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.width - 1)

        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)

        self.write_data(self.buffer)


class SSD1306_I2C(SSD1306):
    """
    I2C transport implementation for SSD1306.
    Extends base driver with I2C command/data writes.
    """

    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c
        self.addr = addr

        # Temporary command buffer
        self.temp = bytearray(2)

        # 0x40 marks following bytes as display data
        self.write_list = [b"\x40", None]

        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        """
        Send a single command byte to display.
        Control byte 0x80 indicates command mode.
        """

        self.temp[0] = 0x80
        self.temp[1] = cmd

        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        """
        Send framebuffer data to display.
        Uses writevto for efficient transfer.
        """

        self.write_list[1] = buf

        self.i2c.writevto(self.addr, self.write_list)
