# import requests, json
# r = requests.get("http://www.wta.org/go-outside/map/@@trailhead-search/getHikes?jsonp_callback=WtaTrailheadSearch.setHikes")
# pre_text = r.text
# text = pre_text[28:len(pre_text)-1]
#
# hike_list = text.split('},')
# for line in hike_list:
#     line += '},'
#     print line

# print json.dumps(hike_list)
import ast

# with open("hikes.json", "r") as file_in:
#     for line in file_in:
#         new_dict = ast.literal_eval(line[1:len(line)-1])
#         print new_dict

new_dict = ast.literal_eval("{"rating": "0.0", "length": "14.0", "kml": "", "features": "rmvpe", "name": "Grand Park via Sunrise", "lat": "46.9143", "lng": "-121.6402", "elevGain": null, "id": "}")
