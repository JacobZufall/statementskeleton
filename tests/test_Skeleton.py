"""
test_Skeleton.py
"""

from src.statement_skeleton.Skeleton import Skeleton
from src.statement_skeleton.Divider import Divider
from src.statement_skeleton.Header import Header

test_fs: dict[str:dict[str:dict[str:any]]] = {
    "asset": {
        "Cash": {
            "d/c": "debit",
            "bal": 0.0,
            "term": "current"
        }
    },

    "liability": {
        "Accounts Payable": {
            "d/c": "credit",
            "bal": 0.0,
            "term": "current"
        }
    },

    "equity": {
        "Common Stock": {
            "d/c": "credit",
            "bal": 0.0
        }
    }
}

test_skeleton: Skeleton = Skeleton(test_fs, "Test Company", "Financial Statement",
                                   "12/31/20XX")

# TODO: Make this all happen automatically based on the dictionary above.

test_skeleton.implement(Divider(test_skeleton, True))
test_skeleton.implement(Header(test_skeleton, "company"))
test_skeleton.implement(Divider(test_skeleton))
test_skeleton.implement(Header(test_skeleton, "fs"))
test_skeleton.implement(Divider(test_skeleton))
test_skeleton.implement(Header(test_skeleton, "date"))
test_skeleton.implement(Divider(test_skeleton))

test_skeleton.print_output()
