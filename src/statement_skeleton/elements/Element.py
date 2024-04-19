"""
Element.py
"""

from typing import override, Any


class Element:
    def __init__(self, skeleton_obj: Any) -> None:
        self.skel: Any = skeleton_obj
        self.output: str = ""

    @override
    def __str__(self) -> str:
        return self.output

