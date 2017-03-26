import MySQLdb
import json
from decimal import Decimal
from eqs import get_difficulty

class Database(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="hikeaway.crmldenzgavh.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                                    user="hikeaway",         # your username
                                    passwd="hikeaway",  # your password
                                    db="hikeaway")        # name of the data base


        self.cursor = self.conn.cursor()
        

    def add_trails(self):
        with open('hikes.json') as data_file:    
            data = json.load(data_file, parse_float=Decimal)

        for trail in data:
            distance = float(trail['length'])
            lat = float(trail['lat'])
            lng = float(trail['lng'])
            if trail['elevGain'] is None:
                gain = 0
            else:
                gain = float(trail['elevGain'])
            diff = get_difficulty(distance, gain)
            self.cursor.execute("INSERT INTO Trail(trailID, trailName, difficulty, lat, long)\
                                 VALUES ('%s', '%s', '%d', '%d', '%d')" % \
                                 (trail['id'], trail['name'], diff, lat, lng))
        self.cursor.commit()
test = Database()
test.add_trails()