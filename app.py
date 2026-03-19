from math import atan2, degrees, pi

import imu
from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app

from .common.angles_for_leds import led_for_angle
from .common.rgb_from_hue import rgb_from_hue
from .lib.circle_finder import circles
from .lib.conf import conf
from .lib.gamma import gamma_corrections
from .lib.hue_generator import hues


class YinYang(app.App):
    """YinYang."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.conf = conf
        self.counts_index = self.conf["default-count-index"]
        self.valid_counts = self.conf["valid-counts"]
        self.hue_offset = 0
        self.rotation_offset = 0
        self.spin_speed = self.conf["spin-speed"]["default"]

        self.light_leds()

    def update(self, _):
        """Update."""
        self.count = self.valid_counts[self.counts_index]
        self.scan_buttons()
        self.hues = hues(self.count, offset=self.hue_offset)
        self.hue_offset += self.conf["hue-increment"]

        if self.spin_speed != 0:
            self.rotation_offset -= self.spin_speed
            self.chasing_leds()

        else:
            acc = imu.acc_read()
            weighting = min(1.0, int(abs(10 - acc[2])) / 9)
            self.rotation_offset = (atan2(acc[1], acc[0])) * weighting
            self.light_leds()

    def draw(self, ctx):
        """Draw."""
        ctx.rotate(-self.rotation_offset)

        for index, (centre, radius) in enumerate(circles(self.count)):
            for key in ["top", "bottom"]:
                ctx.rotate(pi)
                draw_semicircle(ctx, self.hues[key][index], centre, radius)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            if self.counts_index < len(self.valid_counts) - 1:
                self.counts_index += 1

        if self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.button_states.clear()
            if self.counts_index > 0:
                self.counts_index -= 1

        if self.button_states.get(BUTTON_TYPES["RIGHT"]):
            self.button_states.clear()
            if self.spin_speed < self.conf["spin-speed"]["max"]:
                self.spin_speed += 0.1

        if self.button_states.get(BUTTON_TYPES["LEFT"]):
            self.button_states.clear()
            if self.spin_speed > 0 - self.conf["spin-speed"]["max"]:
                self.spin_speed -= 0.1

    def light_leds(self):
        """Light lights."""
        brightness = self.conf["led-brightness"]
        colour = [
            gamma_corrections[int(c * brightness * 255)]
            for c in rgb_from_hue(self.hue_offset)
        ]

        for index in range(12):
            tildagonos.leds[index + 1] = colour

        tildagonos.leds.write()

    def chasing_leds(self):
        """Lights following the pattern."""
        tildagonos.leds[led_for_angle((degrees(self.rotation_offset)) % 360)] = [
            gamma_corrections[int(i * 255 * conf["led-brightness"])]
            for i in rgb_from_hue(self.hues["bottom"][0])
        ]

        tildagonos.leds[led_for_angle((degrees(self.rotation_offset + pi)) % 360)] = [
            gamma_corrections[int(i * 255 * conf["led-brightness"])]
            for i in rgb_from_hue(self.hues["top"][0])
        ]

        tildagonos.leds.write()


def draw_semicircle(ctx, hue, centre, radius):
    """Draw semi."""
    layers = [
        (rgb_from_hue(hue), ctx.fill),
        ((0, 0, 0), ctx.stroke),
    ]

    for colour, method in layers:
        ctx.rgb(*colour)
        ctx.arc(
            centre,
            0,
            radius,
            0,
            0 - pi,
            True,  # noqa: FBT003
        )
        method()


__app_export__ = YinYang
