import requests, bs4, sys
#tuple is name, length, gain, highest, lat, long

for i in range(1, len(sys.argv)):
    r = requests.get(sys.argv[i])
    html = bs4.BeautifulSoup(r.text, "html.parser")
    hike_tuple = []

    hike_title = html.title.text
    hike_tuple.append(hike_title)

    hike_stat_text = html.find("div", {"id": "hike-stats"}).findAll("span")
    for val in hike_stat_text:
        hike_tuple.append(int(val.text))

    hike_stat_cord = html.find("div", {"class": "latlong"}).findAll("span")
    for val in hike_stat_cord:
        hike_tuple.append(str(val.text))

    print hike_tuple
