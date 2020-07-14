'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class MiniUber:

    def __init__(self):
        # initialize your data structure here.
        self.driverLocation = {}
        self.trip = {}

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        self.driverLocation[driver_id] = (lat, lng)
        if driver_id not in self.trip:
            return None
        return self.trip[driver_id]

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        # Write your code here
        minD = sys.maxsize
        closestD = None
        for driver in self.driverLocation.keys():
            if driver in self.trip:
                continue
            lat1, lng1 = self.driverLocation[driver]
            dis = Helper.get_distance(lat1, lng1, lat, lng)
            if dis < minD:
                minD = dis
                closestD = driver

        trip = Trip(rider_id, lat, lng)
        trip.driver_id = closestD
        self.trip[closestD] = trip
        return trip
