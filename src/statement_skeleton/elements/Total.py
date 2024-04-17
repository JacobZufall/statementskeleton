"""
Total.py
"""

from typing import Any

from .Account import Account


class Total(Account):
    def __init__(self, skeleton_obj: Any, total_name: str, total_bal: float | int) -> None:
        super().__init__(skeleton_obj, total_name, total_bal)

        self.total_bal: float | int = 0.0
        if self.skel.decimals:
            self.total_bal = float(round(total_bal, 2))
            self.fdecimal = ".2f"
        else:
            self.total_bal = int(round(total_bal))

        self.space_needed += self.skel.indent

        self.output: str = f"| {total_name}{" " * (self.space_needed - 2)}{self.total_bal:{self.fdecimal}}{" "}|"
