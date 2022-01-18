# import requests
# import mysql.connector
# import pandas as pd

# During a day, there are millions of transactions happening between banks. Because there are so many transactions, those are sorted only at the end of each day, when the balances between each bank are calculated. This is called “settlement”. The process of calculating the end of day balances between banks, and moving the money from one to another. Because this process is so complex, banks work with “clearing houses”. Those are third party financial institutions to which banks send all their transactions and that processes the “settlement” for them.
# We want to build the software for a clearing house.

# min (bank!, n)

transactions = [
    {"payee": "BoA", "amount": 132, "payer": "Chase"},
    {"payee": "BankB", "amount": 827, "payer": "BankC"},
    {"payee": "BankD", "amount": 751, "payer": "BankE"},
]

transactions = [
    {"payee": "BoA", "amount": 132, "payer": "Chase"},
    {"payee": "BoA", "amount": 827, "payer": "Chase"},
    {"payee": "Wells Fargo", "amount": 751, "payer": "BoA"},
    {"payee": "BoA", "amount": 585, "payer": "Chase"},
    {"payee": "Chase", "amount": 877, "payer": "Wells Fargo"},
    {"payee": "Wells Fargo", "amount": 157, "payer": "Chase"},
    {"payee": "Wells Fargo", "amount": 904, "payer": "Chase"},
    {"payee": "Chase", "amount": 548, "payer": "Wells Fargo"},
    {"payee": "Chase", "amount": 976, "payer": "BoA"},
    {"payee": "BoA", "amount": 872, "payer": "Wells Fargo"},
    {"payee": "Wells Fargo", "amount": 571, "payer": "Chase"},
]

# result: {('BoA', 'Wells Fargo'): -121.0, ('Chase', 'Wells Fargo'): 207.0, ('BoA', 'Chase'): 207.0}
# result: {('BoA', 'Wells Fargo'): -121.0, ('BoA', 'Wells Fargo'): 207.0}
# result: {('BoA', 'Wells Fargo'): 86.0}

# return [(string, string): int]
import collections


def mergeTransactions(transactions):
    transaction = collections.defaultdict(int)

    for item in transactions:
        payee = item["payee"]  # receiving
        amount = item["amount"]
        payer = item["payer"]  # paying

        if payer > payee:
            transaction[(payee, payer)] -= amount
        else:
            transaction[(payer, payee)] += amount

    return transaction


# result: {('BoA', 'Wells Fargo'): -121.0, ('Chase', 'Wells Fargo'): 207.0, ('BoA', 'Chase'): 207.0}
# result: {('BoA', 'Wells Fargo'): -121.0, ('BoA', 'Wells Fargo'): 207.0}
# result: {('BoA', 'Wells Fargo'): 86.0}

# banks  orig
# build key
# key => [bank, banksAfterAlbet]
from heapq import heappop, heappush

# payee, payer, amount for payer
# def mergeTransactions2(transactions):
#     # exit?
#     transactions = mergeTransactions(transactions)
#     banks = set()
#     for key in transactions:
#         payee, payer = key
#         banks.add(payee)
#         banks.add(payer)
#     banks = list(sorted(banks))

#     def dfs(index):
#         # not sure
#         if index + 1 > len(banks):
#             return

#         if (banks[index], banks[index + 1]) not in transactions:
#             return

#         payee, lastPayer, lastAmount = (
#             banks[index],
#             banks[index + 1],
#             transactions[(banks[index], banks[index + 1])],
#         )

#         for i in range(index + 1, len(banks)):
#             currPayer = banks[i]
#             if (lastPayer, currPayer) not in transactions:
#                 continue
#             amount = transactions[(lastPayer, currPayer)]

#             del transactions[(payee, lastPayer)]
#             del transactions[(lastPayer, currPayer)]
#             transactions[(payee, currPayer)] += amount + lastAmount
#             lastPayer, lastAmount = currPayer, transactions[(payee, currPayer)]

#     dfs(0)
#     return transactions


def mergeTransactions2(transactions):
    # exit?
    transactions = mergeTransactions(transactions)
    payeeMapping = collections.defaultdict(set)
    for payee, payer in transactions:
        payeeMapping[payee].add(payer)
    print("wtf")
    print(payeeMapping)

    return transactions


print(mergeTransactions(transactions))
print(mergeTransactions2(transactions))
print(-568 + 207 - 121)

