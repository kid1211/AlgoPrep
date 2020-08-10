class Solution:
    """
    @param employees: information of the employees
    @param friendships: the friendships of employees
    @return: return the statistics
    """

    def departmentStatistics(self, employees, friendships):
        # write your code here.
        idToDepartment = {}
        departmentHeadCounts = {}
        departmentEmployees = collections.defaultdict(set)

        for person in employees:
            info = person.split(', ')

            if len(info) != 3:
                continue

            departmentHeadCounts[info[2]] = departmentHeadCounts.get(
                info[2], 0) + 1
            idToDepartment[info[0]] = info[2]

        for relationship in friendships:
            friendPair = relationship.split(', ')
            employee1, employee2 = friendPair

            if len(friendPair) != 2 or idToDepartment[employee1] == idToDepartment[employee2]:
                continue

            departmentEmployees[idToDepartment[employee1]].add(employee1)
            departmentEmployees[idToDepartment[employee2]].add(employee2)

        res = []
        for department in sorted(departmentHeadCounts):
            res.append(
                f"{department}: {len(departmentEmployees[department])} of {departmentHeadCounts[department]}")

        return res
