'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''


class PubSubPattern:
    def __init__(self):
        # do intialization if necessary
        self.subscriber = collections.defaultdict(set)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def subscribe(self, channel, user_id):
        # write your code here
        self.subscriber[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def unsubscribe(self, channel, user_id):
    	# write your code here
        self.subscriber[channel].discard(user_id)

    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """

    def publish(self, channel, message):
        if channel in self.subscriber:
            for user in self.subscriber[channel]:
                PushNotification.notify(user, message)
