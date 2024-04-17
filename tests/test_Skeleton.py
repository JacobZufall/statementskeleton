"""
test_Skeleton.py
"""

from src.statement_skeleton.skeletons.Skeleton import Skeleton

test_fs: dict[str:dict[str:dict[str:any]]] = {
    "Assets": {
        "Cash": {
            "d/c": "debit",
            "bal": 400.00,
            "term": "current"
        }
    },

    "Liabilities": {
        "Accounts Payable": {
            "d/c": "credit",
            "bal": 200.00,
            "term": "current"
        }
    },

    "Stockholders' Equity": {
        "Common Stock": {
            "d/c": "credit",
            "bal": 200.00
        }
    }
}

test_skeleton: Skeleton = Skeleton(test_fs, "Test Company", "Financial Statement",
                                   "12/31/20XX", decimals=True)

test_skeleton.print_output()
