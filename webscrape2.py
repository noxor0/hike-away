import requests, json
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

with open("hikes.txt", "rb") as file_in:
    content = json.load(file_in)
with open("stringJson.txt", "wb") as fout:
    json.dump(content, fout, indent=1)
