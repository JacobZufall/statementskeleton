"""
Skeleton.py
"""

from typing import Any

from src.statement_skeleton.elements.Account import Account
from src.statement_skeleton.elements.Divider import Divider
from src.statement_skeleton.elements.Header import Header
from src.statement_skeleton.elements.Title import Title
from src.statement_skeleton.elements.Total import Total


class Skeleton:
    subclasses: list[str] = [
        "Account",
        "Divider",
        "Header",
        "Title",
        "Total"
    ]

    months: dict[str:str] = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    def __init__(self, fnstmt: dict[str:dict[str:dict[str:any]]], company: str, fs_name: str, date: str,
                 min_width: int = 50, margin: int = 2, indent: int = 4, decimals: bool = True) -> None:
        """
        :param company: The name of the company.
        :param fs_name: The name of the financial statement.
        :param date: The date of the financial statement.
        :param fnstmt: The financial statement.
        :param min_width: The minimum width the financial statement will be in the output.
        :param margin: How many spaces are on each side of headers.
        :param indent: How many spaces are between an account name and the side.
        """
        self.company: str = company
        self.fs_name: str = fs_name
        self.f_date: str = self._format_date(date)
        self.fnstmt: dict[str:dict[str:dict[str:any]]] = fnstmt

        self.min_width: int = min_width
        self.margin: int = margin
        self.indent: int = indent
        self.decimals: bool = decimals
        self.calc_width: int = -1

        # In order to properly format the width, we need to know the longest string used, so we know how wide to make
        # the table.
        self.titles: list[str] = []
        self.implemented_elements: list[Any] = []

        if self.company is not None:
            self.add_title(self.company)

        if self.fs_name is not None:
            self.add_title(self.fs_name)

        if self.f_date is not None:
            self.add_title(self.f_date)

        if self.fnstmt is not None:
            for category, accounts in self.fnstmt.items():
                for account, attributes in accounts.items():
                    self.add_title(account)

        self.implement(Divider(self, True))
        self.implement(Header(self, "company"))
        self.implement(Divider(self, False))
        self.implement(Header(self, "fs"))
        self.implement(Divider(self, False))
        self.implement(Header(self, "date"))
        self.implement(Divider(self, False))

        for category, accounts in self.fnstmt.items():
            self.implement(Title(self, (category.lower()).capitalize()))

            total_bal: float | int = 0.0

            for account, attributes in accounts.items():

                if attributes["d/c"] == "debit":
                    total_bal += attributes["bal"]

                else:
                    total_bal -= attributes["bal"]

                self.implement(Account(self, account, attributes["bal"]))

            self.implement(Total(
                self,
                f"Total {(category.lower()).capitalize()}",
                abs(total_bal)
            ))

            self.implement(Divider(self, False))

    def _calc_width(self) -> None:
        """
        Calculates the width the output will be.
        :return: Nothing.
        """
        for title in self.titles:
            if len(title) > self.calc_width:
                self.calc_width = len(title)

            if self.calc_width < self.min_width:
                self.calc_width = self.min_width

    def _format_date(self, date: str) -> str:
        split_date: list[str] = date.split("/")
        return f"For year ended {self.months[split_date[0]]} {split_date[1]}, {split_date[2]}"

    def add_title(self, title: str) -> None:
        """
        Adds a title into a list that's used to calculate the width of the output. This method checks for redundancy
        and recalculates the width of the output automatically.
        :param title: The title to add/append.
        :return: Nothing.
        """
        if title not in self.titles:
            self.titles.append(title)

        self._calc_width()

    def implement(self, element: Any):
        if type(element).__name__ not in self.subclasses:
            raise KeyError(f"{type(element).__name__} isn't a valid element.")

        self.implemented_elements.append(element)

    def print_output(self) -> None:
        for element in self.implemented_elements:
            print(element)
