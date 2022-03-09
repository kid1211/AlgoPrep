from random import randint


class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.servers = []
        self.maps = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id):
        # write your code here
        if server_id in self.maps:
            self.remove(server_id)
        self.servers.append(server_id)
        self.maps[server_id] = len(self.servers) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id):
        # write your code here
        if server_id not in self.maps:
            return

        # get its index in array and remove values
        emptiedIndex = self.maps[server_id]
        del self.maps[server_id]

        # move lastElement to from
        lastServerId = self.servers.pop()

        if lastServerId == server_id or not self.servers:
            return

        self.servers[emptiedIndex] = lastServerId
        self.maps[lastServerId] = emptiedIndex

    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self):
        # write your code here
        return self.servers[randint(0, len(self.servers) - 1)]
