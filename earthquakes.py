# the eq_data file is a json file that contains detailed information about
# earthquakes around the world for a period of a month.

# NOTE: No hard-coding allowed except for keys for the dictionaries

import json

infile = open("eq_data.json","r")
eq = json.load(infile)

# 1) print out the number of earthquakes
print("\nNumber of earth quakes:", eq["metadata"]["count"],"\n\n")


# 2) iterate through the dictionary and extract the location, magnitude,
#    longitude and latitude of the location and put it in a new
#    dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
#    magnitude > 6. Print out the new dictionary.
eq_dict = {"mag6":[]}

for feature in eq["features"]:
    if feature["properties"]["mag"] > 6:
        eq_dict["mag6"].append({"location": feature["properties"]["place"],
                    "magnitude": feature["properties"]["mag"],
                    "longitude": feature["geometry"]["coordinates"][0],
                    "latitude": feature["geometry"]["coordinates"][1]})

# 3) using the eq_dict dictionary, print out the information as shown below (first three shown):
# print(eq_dict)

for i in range(len(eq_dict["mag6"])):
    print(f"Location: {eq_dict['mag6'][i]['location']}")
    print(f"Magnitude: {eq_dict['mag6'][i]['magnitude']}")
    print(f"Longitude: {eq_dict['mag6'][i]['longitude']}")
    print(f"Latitude: {eq_dict['mag6'][i]['latitude']}\n\n")

# Location: Northern Mid-Atlantic Ridge
# Magnitude: 6.2
# Longitude: -36.0923
# Latitude: 35.4364


# Location: 166km SSE of Muara Siberut, Indonesia
# Magnitude: 6.1
# Longitude: 100.0208
# Latitude: -2.8604


# Location: 14km ENE of Puerto Madero, Mexico
# Magnitude: 6.6
# Longitude: -92.2981
# Latitude: 14.7628



