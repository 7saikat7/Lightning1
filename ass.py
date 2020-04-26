import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(22.57613349325925, 88.42796842589601, 10)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
with open("Direction to pg.csv", 'r') as f:
    reader = csv.reader(f)
    k = 0
    for row in reader:
        lon = float(row[0])
        lat = float(row[1])
    if k == 0:
        gmap.marker(lat, lon, 'green')
        k = 1
    else:
        gmap.marker(lat, lon, 'blue')
gmap.marker(lat, lon, 'red')

gmap.draw("maptail.html")
