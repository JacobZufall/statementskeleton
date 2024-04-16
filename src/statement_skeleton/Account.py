"""
Account.py
"""

from typing import override

from Skeleton import Skeleton


class Account:
    def __init__(self, skeleton_obj: Skeleton, account_name: str, account_bal: float | int) -> None:
        self.skel: Skeleton = skeleton_obj
        self.space_needed: int = (self.skel.calc_width - len(account_name) + self.skel.margin - self.skel.indent -
                                  len(str(account_bal)))

        self.output: str = f"|{" " * self.skel.indent}{account_name}{" " * (self.space_needed - 1)}{account_bal}{" "}|"

    @override
    def __str__(self) -> str:
        return self.output
