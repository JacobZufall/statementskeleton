"""
Header.py
"""

from typing import Any

from .Element import Element


class Header(Element):
    def __init__(self, skeleton_obj: Any, header_type: str, header_name: str = "") -> None:
        super().__init__(skeleton_obj)

        self.header_name: str = ""

        if header_type.lower() == "company":
            self.header_name = self.skel.company

        elif header_type.lower() == "fs":
            self.header_name = self.skel.fs_name

        elif header_type.lower() == "date":
            self.header_name = self.skel.f_date

        else:
            # Allows a custom header title with proper formatting.
            self.skel.add_title(header_name)
            self.header_name = header_name

        self.space_needed: int = (self.skel.calc_width + self.skel.margin - len(self.header_name))
        self.l_space_needed: int = 0
        self.r_space_needed: int = 0

        if self.space_needed % 2 != 0:
            self.l_space_needed = int((self.space_needed / 2) - 0.5)
            self.r_space_needed = int((self.space_needed / 2) + 0.5)

        else:
            self.l_space_needed = self.r_space_needed = self.space_needed // 2

        self.output = f"|{" " * self.l_space_needed}{self.header_name}{" " * self.r_space_needed}|"
