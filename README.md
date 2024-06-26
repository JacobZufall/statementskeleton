# StatementSkeleton
StatementSkeleton is a package for formatting your output to appear as a financial statement. This package was designed
to be used with PyActy, but it can be used by itself.

## Classes

### Skeleton
This is the main class and all other elements are nested inside of it. You can create a Skeleton like so:
```py
from statementskeleton import Skeleton

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
            "bal": 1_000
        }
    }
}
```
If it isn't formatted like this, it won't work.

Using all the information above, we can complete the creation of our Skeleton object:
```py
from statementskeleton import Skeleton

skel: Skeleton = Skeleton(financial_statement, "Company Name", "Financial Statement", "12/31/2024", decimals=False)

# This is the method to actually print the financial statement.
skel.print_output()
```

### Account
This class adds an account to the `Skeleton` that contains a name and a balance. You can add it to the `Skeleton` like so:
```py
from statementskeleton import Skeleton, Account

skel: Skeleton = Skeleton(financial_statement, "Company Name", "Financial Statement", "12/31/2024", decimals=False)

skel.implement(Account(skel, "Cash", 400), "cash_account")
```
The `implement()` method has two arguments. The first is the actual element you're implementing, and the second is a 
unique ID for that element so that it can be modified later if needed.

When implementing an element, the first argument of the object must be the `Skeleton` object you are implementing the
element to. This applies to EVERY element.

It's recommended to make a new class that inherits `Skeleton` and override the `define_header()` and `define_body()` 
methods, but this will be covered in a later section.

### Divider

### Element

### Header

### Spacer

### Subtotal

### Title

### Total