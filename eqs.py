import MySQLdb

# Returns difficulty of trail based on distance and gain
def get_difficulty(distance, gain):
    # TODO handle null and negative input
    print str(distance) + " " + str(gain)
    dist = distance * 5280.0 # Convert from miles to feet
    d = dist / 20000
    g = gain / 2000.0
    s = (gain * 20) / dist
    difficulty = d + g + s
    return min(10.0, difficulty)

# Returns starting level of user
def get_first_lvl(weight, height, level):
    # Autoset level if invalid input
    if level > 10 or level < 0 or weight < 0 or height < 0:
        return 1
    bmi = weight / (height ** 2)
    lvl = 0.0
    if bmi > 25:
        lvl = min(level, 2.5)
    elif bmi > 30:
        lvl = 1.0
    else:
        lvl = level

    return lvl

# Updates user level after hike completed
# def update_usr_lvl(usr_id, trl_id):
#
#     # Open database
#     # TODO migrate to driver file
#     db = MySQLdb.connect(host="hikeaway.crmldenzgavh.us-west-2.rds.amazonaws.com",    # your host, usually localhost
#                          user="hikeaway",         # your username
#                          passwd="hikeaway",  # your password
#                          db="hikeaway")        # name of the data base
#     c = db.cursor()
#
#     # SELECT liked
#     # FROM usr_hike
#     # WHERE USR_ID == usrID && TRAIL_ID == trlID;
#     c.execute("SELECT * FROM test")
#     usr_lvl =
#     c.execute("SELECT * FROM test")
#     trail_lvl =
#     c.execute("SELECT * FROM test")
#     liked =
#     if liked != null:
#         # Too easy
#         if liked == -1:
#             # Raise level
#             if trail_lvl >= usr_lvl:
#                 usr_lvl = min(10.0, trail_lvl + .5)
#             else:
#                 usr_lvl = min(10.0, usr_lvl + .25)
#
#         # Too hard
#         elif liked == 1:
#             # Lower level
#             if trail_lvl <= usr_lvl:
#                 usr_lvl = max(0.0, trail_lvl - .5)
#             else:
#                 usr_lvl = min(10, usr_lvl - .25)
#
#         # Perfect
#         else:
#             usr_lvl = trail_lvl
#
#     db.close()
