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
        Creates a skeleton to add elements into in order to neatly display a financial statement in the console.
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
        self.implemented_elements: list[list[str]] = []

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

        self.define_header()
        self.define_body()

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
        """
        Formats the date from a "mm/dd/yyyy" format to a "For year ended Month DD, YYYY" format.
        :param date: The date to format, in "mm/dd/yyyy" format.
        :return: The formatted date.
        """
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

    def implement(self, element: Any, key: str) -> None:
        """
        Implements an element into the skeleton.
        :param element: The element to implement.
        :param key: A unique key for the element.
        :return: Nothing.
        """
        if type(element).__name__ not in self.subclasses:
            raise KeyError(f"{type(element).__name__} isn't a valid element.")

        # Ensures no two elements have the same key.
        for implement in self.implemented_elements:
            if key == implement[1]:
                raise KeyError(f"There is already an element with the key {key}.")

        else:
            self.implemented_elements.append([element, key])

    def annul(self, key: str) -> None:
        """
        Removes an element from the skeleton.
        :param key: The unique key of the element.
        :return: Nothing.
        """
        for implement in self.implemented_elements:
            if key == implement[1]:
                self.implemented_elements.remove(implement)
                break

        else:
            raise KeyError(f"No element with a key of {key} was found.")

    # The reason define_header() and define_body() are separate methods is so that you can easily override one without
    # affecting the other. The body for this class is extremely generic, and may not be what people want their output
    # to look like. However, the header is usually pretty consistent across most financial statements.
    def define_header(self) -> None:
        """
        Defines the header of the financial statement with stuff such as company information. This will always be
        printed before the body.
        :return: Nothing.
        """
        self.implement(Divider(self, True), "div_top")
        self.implement(Header(self, "company"), "head_company")
        self.implement(Divider(self, False), "div_1")
        self.implement(Header(self, "fs"), "head_fs")
        self.implement(Divider(self, False), "div_2")
        self.implement(Header(self, "date"), "head_date")
        self.implement(Divider(self, False), "div_3")

    def define_body(self) -> None:
        """
        Defines the body of the financial statement with stuff such as accounts and totals. This will always be printed
        after the header.
        :return: Nothing
        """
        # This is important to determine the bottom-most divider.
        next_div_num: int = 4

        # The formatting below is pretty general and doesn't contain any subtotal lines for specific things, such as
        # a total line for current assets and current liabilities. These should be taken care of in the subclasses.
        for category, accounts in self.fnstmt.items():
            self.implement(Title(self, (category.lower()).capitalize()),
                           f"title_{category.lower()}")

            total_bal: float | int = 0.0

            for account, attributes in accounts.items():

                if attributes["d/c"] == "debit":
                    total_bal += attributes["bal"]

                else:
                    total_bal -= attributes["bal"]

                self.implement(Account(self, account, attributes["bal"]),
                               f"account_{account.lower()}")

            self.implement(Total(
                self,
                f"Total {(category.lower()).capitalize()}",
                abs(total_bal)
            ),
                f"total_{category.lower()}"
            )

            self.implement(Divider(self, False), f"div_{next_div_num}")
            next_div_num += 1

        # Removes the last divider and replaces it with a properly formatted one.
        self.annul(f"div_{next_div_num - 1}")
        self.implement(Divider(self, True), "div_bottom")

    def print_output(self) -> None:
        """
        Prints the skeleton.
        :return: Nothing.
        """
        for implement in self.implemented_elements:
            print(implement[0])
