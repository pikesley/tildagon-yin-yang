from math import pi

from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .lib.background import Background
from .lib.circle_finder import circles

full_radius = 120


class YinYang(app.App):
    """YinYang."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.count = 3

    def update(self, _):
        """Update."""
        self.scan_buttons()

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))

        self.draw_overlays(ctx)

        radius = full_radius / self.count

        ctx.rgba(255, 0, 0, 1.0)
        for centre, radius in circles(self.count):
            ctx.arc(
                centre,
                0,
                radius,
                0,
                2 * pi,
                True,  # noqa: FBT003
            ).stroke()



    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            self.count += 1

        if self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.button_states.clear()
            self.count -= 1

__app_export__ = YinYang
