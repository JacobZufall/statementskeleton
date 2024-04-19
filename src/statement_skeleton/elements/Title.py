"""
Title.py
"""

from typing import Any

from .Element import Element


class Title(Element):
    def __init__(self, skeleton_obj: Any, title_name: str) -> None:
        super().__init__(skeleton_obj)
        self.space_needed: int = (self.skel.calc_width + self.skel.margin - len(title_name))
        self.output = f"| {title_name}{" " * (self.space_needed - 1)}|"
