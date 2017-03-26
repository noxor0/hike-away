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
test = Database()
test.add_trails()