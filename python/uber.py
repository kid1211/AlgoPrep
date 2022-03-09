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


def mergeTransactions2(transactions):
    # exit?
    transactions = mergeTransactions(transactions)
    uf = UnionFind(transactions)
    uf.find("Wells Fargo")

    return transactions


class UnionFind:
    def __init__(self, transactions):
        self.father = {}

        for payee, payer in transactions:
            if payee not in self.father:
                self.father[payee] = payee
            self.father[payer] = payee
        # print(self.father)

    def find(self, bank):
        lastFather = None
        while bank != self.father[bank]:
            lastFather = bank
            print("bobo", bank, lastFather, self.father[bank])
            bank = self.father[bank]


# def mergeTransactions2(transactions):
#     # exit?
#     transactions = mergeTransactions(transactions)

#     banks = set()
#     for key in transactions:
#         payee, payer = key
#         banks.add(payee)
#         banks.add(payer)

#     indegree = {n: 0 for n in banks}
#     payeeMapping = collections.defaultdict(set)

#     for payee, payer in transactions:
#         indegree[payer] += 1
#         payeeMapping[payee].add(payer)

#     queue = collections.deque([n for n in indegree if indegree[n] == 0])
#     print("wtf")
#     tmp = []

#     while queue:
#         node = queue.popleft()

#         if node not in payeeMapping:
#             tmp += [node]

#         # xx
#         print(node)
#         for payer in payeeMapping[node]:
#             # node -> payer
#             for nextPayer in payeeMapping[payer]:
#                 # node -> nextPayer + transaction
#                 transactions[(node, nextPayer)] = transactions[(payer, nextPayer)]
#                 queue.append(nextPayer)
#                 # del
#                 del transactions[(payer, nextPayer)]
#             del transactions[(node, payer)]

#     print("huh", tmp)
#     print("wtf")

#     return transactions


print(mergeTransactions(transactions))
mergeTransactions2(transactions)
# print("2", mergeTransactions2(transactions))

