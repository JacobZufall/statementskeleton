"""
Title.py
"""

from typing import override

from .Skeleton import Skeleton


class Title:
    def __init__(self, skeleton_obj: Skeleton, title_name: str) -> None:
        self.skel: Skeleton = skeleton_obj

        self.output: str = ""

        self.space_needed: int = (self.skel.calc_width + self.skel.margin - len(self.title_name))

        self.output = f"|{title_name}{" " * self.space_needed}|"

    @override
    def __str__(self) -> str:
        return self.output
