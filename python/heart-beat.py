class HeartBeat:

    def __init__(self):
        # do intialization if necessary
        self.slaves = {}

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """

    def initialize(self, slaves_ip_list, k):
        # write your code here
        self.k = k
        for ip in slaves_ip_list:
            self.slaves[ip] = 0
    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """

    def ping(self, timestamp, slave_ip):
        # write your code here
        if slave_ip not in self.slaves:
            return
        self.slaves[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """

    def getDiedSlaves(self, timestamp):
        # write your code here
        dead = []
        curr = timestamp - 2 * self.k
        for key in self.slaves.keys():
            if self.slaves[key] <= curr:
                dead.append(key)
        return dead
