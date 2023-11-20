import json 
#import geojson
import pandas as pd

def cleanOfficialCountryNames(): 
    raw = open("data/officialNames/raw.txt", "r")
    f_out = open("data/officialNames/refined.csv", "w")

    for line in raw: 
        # Remove – and  - characters (with space on each side) 
        line = line.replace(" – ", ",")
        line = line.replace(" - ", ",")

        # Remove ’ character
        line = line.replace("’", "")

        # Handle St. Lucia, etc. 
        line = line.replace("St.", "Saint")

        # Change spaces and - (for countries such as Guinea-Bisseau) to underscores
        line = line.replace(" ", "_")
        line = line.replace("-", "_")

        f_out.write(line)
    
    raw.close()
    f_out.close()

def parseGeoJson(): 
    data = {}
    with open("countryBorders.geojson") as f: 
        data = json.load(f)

    out = open("data/countryBorders.geojson", "w")
    for row in data["features"]: 
        if row["properties"]["ISO_A3"] != "-99":
            
            print(row["properties"]["ISO_A3"])
