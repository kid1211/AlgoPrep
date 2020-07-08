import random


class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        # Write your code here
        db = cls()
        db.ids = set()
        db.machines = {}
        db.n = n  # segment in ring
        db.k = k  # virtual notes
        return db

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """

    def addMachine(self, machine_id):
        # write your code here
        ids = []

        for i in range(self.k):
            idx = self.getUniqueIds()
            ids.append(idx)
            self.ids.add(idx)

        ids.sort()
        self.machines[machine_id] = ids
        return ids
    """
    @param: hashcode: An integer
    @return: A machine id
    """

    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        machine_id = -1
        distance = self.n + 1
        # 顺时针遇到的第一个节点，不管是虚拟还是实体，都是属于这个机器的
        # 所以我们要找最近的距离， 同时因为ids是排好序的，所以可以二分
        for key, value in self.machines.items():
            import bisect
            # like a binary search
            index = bisect.bisect_left(value, hashcode) % len(value)
            d = value[index] - hashcode
            if d < 0:
                d += self.n

            if d < distance:
                distance = d
                machine_id = key

        return machine_id

    def getUniqueIds(self):
        idx = random.randint(0, self.n - 1)

        if idx in self.ids:
            return self.getUniqueIds()

        return idx
