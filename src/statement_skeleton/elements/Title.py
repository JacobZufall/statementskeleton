"""
Title.py
"""

from typing import override, Any


class Title:
    def __init__(self, skeleton_obj: Any, title_name: str) -> None:
        self.skel: Any = skeleton_obj

        self.output: str = ""

        self.space_needed: int = (self.skel.calc_width + self.skel.margin - len(title_name))

        self.output = f"| {title_name}{" " * (self.space_needed - 1)}|"

    @override
    def __str__(self) -> str:
        return self.output
