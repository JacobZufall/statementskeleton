"""
Divider.py
"""

from typing import Any

from .Element import Element


class Divider(Element):
    def __init__(self, skeleton_obj: Any, border: bool = False) -> None:
        super().__init__(skeleton_obj)

        if border:
            self.output = f"+{"-" * (self.skel.calc_width + self.skel.margin)}+"
        else:
            self.output = f"|{"-" * (self.skel.calc_width + self.skel.margin)}|"
