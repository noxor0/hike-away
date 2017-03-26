from math import radians, sin, cos, sqrt, atan2
import bisect

# userID name skillLevel lat long
test_user = [5, "Connor", 3.1, 42.000, -122.000]
# userID hikeID rating
test_rate = [1, 5, 1]

# TODO: Use dist formula to find hikes < 100 miles from user location
# TODO: Suggest 3 hikes with increasing difficulty (hikes wih values +/- value)

class hikeBuddy():
# 1 degree of Longitude =
# cosine (latitude in decimal degrees) * length of degree (miles) at equator.
    def find_distance(self, user_lat, user_long, trail_lat, trail_long):
        R = 6373.0
        lat1 = radians(user_lat)
        lon1 = radians(user_long)
        lat2 = radians(trail_lat)
        lon2 = radians(trail_long)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        distance = distance * .621371
        return distance


    def get_hikes(self):
        # TODO: get values from database
        # TODO: only get values that havent been hiked before
        hike_list = []
        # trailID, name, difficulty, lat, long
        hike_list.append([1, "Hike 1", 4.1, 42.123, -122.456])
        hike_list.append([2, "Hike 2", 4.0, 42.456, -122.567])
        hike_list.append([3, "Hike 3", 2.0, 42.123, -122.123])
        hike_list.append([4, "Hike 4", 3.0, 42.456, -122.123])

        return hike_list

    def find_suggestions(self):
        poss_hikes = []
        top_three = []
        user = test_user
        local_hikes = self.get_hikes()

        # find hikes within 80 miles
        for hike in local_hikes:
            if(self.find_distance(user[3], user[4], hike[3], hike[4]) < 80):
                if(abs(user[2] - hike[2]) <= 1.5):
                    poss_hikes.append([hike, abs(user[2] - hike[2])])


        for i in range(3):
            top_three.append(poss_hikes[i][0])
        return top_three

hb = hikeBuddy()
print(hb.find_suggestions())
