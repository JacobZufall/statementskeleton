# StatementSkeleton
StatementSkeleton is a package for formatting your output to appear as a financial statement. This package was designed
to be used with PyActy, but it can be used by itself.

## Classes

### Skeleton
This is the main class and all other elements are nested inside of it. You can create a Skeleton like so:
```py
from statement_skeleton import Skeleton

skel: Skeleton = Skeleton()
```
The class takes five arguments:
1. The financial statement you wish to print.
2. The name of the company the financial statement belongs to.
3. The name of the financial statement.
4. The date of the financial statement (MM/DD/YYYY format).
5. If the numbers show decimals or not.

The financial statement must be specifically formatted for this to work. An example is as follows:
```py
financial_statement: dict[str:dict[str:dict[str:str | float]]] = {
    "Assets": {
        "Cash": {
            "d/c": "debit",
            "bal": 400.0,
            "term": "current"
        },

        "Accounts Receivable": {
            "d/c": "debit",
            "bal": 1_000.0,
            "term": "current"
        }
    },

    "Liabilities": {
        "Accounts Payable": {
            "d/c": "credit",
            "bal": 200.0,
            "term": "current"
        }
    },

    "Stockholders' Equity": {
        "Common Stock": {
            "d/c": "credit",
            "bal": 200
        },

        "Retained Earnings": {
            "d/c": "credit",
            "bal": 1000
        }
    }
}
```
If it isn't formatted like this, it won't work.

Using all the information above, we can complete the creation of our Skeleton object:
```py
from statement_skeleton import Skeleton

skel: Skeleton = Skeleton(financial_statement, "Company Name", "Financial Statement", "12/31/2024", decimals=False)

# This is the method to actually print the financial statement.
skel.print_output()
```

### Account

### Divider

### Element

### Header

### Spacer

### Subtotal

### Title

### Total