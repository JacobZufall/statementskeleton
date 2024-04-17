"""
Divider.py
"""

from typing import override, Any


class Divider:
    def __init__(self, skeleton_obj: Any, border: bool = False) -> None:
        self.skel: Any = skeleton_obj

        self.output: str = ""

        print(self.skel.calc_width)

        if border:
            self.output = f"+{"-" * (self.skel.calc_width + self.skel.margin)}+"
        else:
            self.output = f"|{"-" * (self.skel.calc_width + self.skel.margin)}|"

    @override
    def __str__(self) -> str:
        return self.output
