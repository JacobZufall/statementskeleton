"""
Account.py
"""

from typing import Any

from .Element import Element


class Account(Element):
    def __init__(self, skeleton_obj: Any, account_name: str, account_bal: float | int) -> None:
        """
        Adds an individual account and its balance to the skeleton.
        :param skeleton_obj: The skeleton to implement the element into.
        :param account_name: The name of the account to display.
        :param account_bal: The balance of the account to display.
        """
        super().__init__(skeleton_obj)

        self.space_needed: int = 0
        self.account_bal: float | int = 0.0
        self.fdecimal: str = ""

        if self.skel.decimals:
            self.account_bal = float(round(account_bal, 2))
            self.fdecimal = ".2f"
            self.space_needed -= 1

        else:
            self.account_bal = int(round(account_bal))

        self.space_needed += (self.skel.calc_width - len(account_name) + self.skel.margin - self.skel.indent -
                              len(str(self.account_bal)))

        self.output: str = (
            f"|{" " * self.skel.indent}{account_name}{"·" * (self.space_needed - 1)}{self.account_bal:{self.fdecimal}}"
            f"{" "}|"
        )
