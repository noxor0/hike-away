import MySQLdb
import json
from decimal import Decimal
from eqs import get_difficulty
from Hike import Hike, User
class Database(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="hikeaway.crmldenzgavh.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                                    user="hikeaway",         # your username
                                    passwd="hikeaway",  # your password
                                    db="hikeaway")        # name of the data base


        self.cursor = self.conn.cursor()
    def add_trails(self):
        with open('hikes.json') as data_file:
            data = json.load(data_file)

        for trail in data:
            try:
                distance = float(trail['length'])
                lat = float(trail['lat'])
                lng = float(trail['lng'])
                if trail['elevGain'] is None:
                    gain = 0
                else:
                    gain = float(trail['elevGain'])
                diff = get_difficulty(distance, gain)
                sql = """INSERT INTO Trail(trailID, trailName, difficulty, lat, lng) VALUES ('%s', "%s", '%3.1f', '%7.4f', '%7.4f')""" % (trail['id'], trail['name'], diff, lat, lng)
                print sql
                try:
                    self.cursor.execute(sql)
                    self.conn.commit()
                except:
                    self.conn.rollback()
            except:
                pass
        self.conn.close()
    def get_hikes(self, user_id=1):
        hikes = []
        self.cursor.execute("SELECT trailID, trailName, difficulty, lat, lng \
                            FROM Trail t WHERE trailID NOT IN (SELECT trailID FROM User_Hike WHERE userID = %d);" % (user_id))
        result = self.cursor.fetchall()
        for hike in result:
            temp = Hike(hike[0], hike[1], hike[2], hike[3], hike[4])
            hikes.append(temp)

        return hikes

    def get_user(self, user_id=1):
        self.cursor.execute("SELECT * FROM User WHERE userID = %d" % (user_id))
        temp = self.cursor.fetchone()
        return User(temp[0], temp[1], temp[2], temp[3], temp [4])

    def add_user_hike(self, user_id, trail_id, liked=None):
        self.cursor.execute("INSERT INTO User_Hike(userID, trailID, liked)\
                             VALUES ('%s', '%s', '%d')" % (user_id, trail_id, liked))
        self.conn.commit()

    def get_trail_difficulty(self, trail_id):
        self.cursor.execute("SELECT difficulty FROM Trail WHERE trailID = '" + trail_id + "'")
        return self.cursor.fetchone()[0]

    def get_liked_trails(self, user_id, trail_id):
        self.cursor.execute("SELECT liked FROM User_Hike WHERE userID = " + str(user_id) + " AND trailID = '" + trail_id + "'")
        return self.cursor.fetchone()[0]

    def update_user_level(self, user_id, user_skill):
        self.cursor.execute("UPDATE User SET skill = " + str(user_skill) + " WHERE userID = " + str(user_id))

        self.conn.commit()
        

