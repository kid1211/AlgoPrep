class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    def accountsMerge(self, accounts):
        # write your code here
        uf = UnionFind(accounts)
        childrenMap = collections.defaultdict(set)

        # all email point to the first one
        for account in accounts:
            n = len(account)

            if n < 2:
                continue
            father = account[1]
            for i in range(2, n):
                uf.merge(father, account[i])

        # construct children
        for account in accounts:
            if not account:
                continue
            for i in range(1, len(account)):
                father = uf.find(account[i])
                childrenMap[father].add(account[i])

        # get answer format
        res = []
        for account in childrenMap.keys():
            current = [uf.owner[account]]
            for email in sorted(list(childrenMap[account])):
                current.append(email)
            res.append(current)

        return res


class UnionFind:
    def __init__(self, accounts):
        self.father = {}
        self.owner = {}

        for account in accounts:
            for i in range(1, len(account)):
                self.father[account[i]] = account[i]
                self.owner[account[i]] = account[0]

    def find(self, email):
        path = []

        while self.father[email] != email:
            path.append(email)
            email = self.father[email]

        for item in path:
            self.father[item] = email

        return email

    def merge(self, email1, email2):
        dad1, dad2 = self.find(email1), self.find(email2)

        if dad1 != dad2:
            self.father[dad1] = dad2
