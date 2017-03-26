import MySQLdb

db = MySQLdb.connect(host="hikeaway.crmldenzgavh.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                     user="hikeaway",         # your username
                     passwd="hikeaway",  # your password
                     db="hikeaway")        # name of the data base
c = db.cursor()
c.execute("SELECT * FROM test")

for row in c.fetchall():
    print row[0]

db.close()
