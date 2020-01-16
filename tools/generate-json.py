import os
import re
import sys
import json

print("Generate Json [v0.0.1]\n\n")


# Location of covers/
coversDir = str(input("Path to covers/ directory [covers/]: "))

# If nothing was input
if coversDir == "":
    # Use default value
    coversDir = "covers"

# Check if directory exists
if not os.path.exists(coversDir):
    # Exit if it does not exist
    print("Directory '"+ coversDir +"' could not be found")
    sys.exit()


# Save release data in array
data = []

for path, dirs, files in os.walk(coversDir):
    # Remove path to covers directory in output
    name = "".join(path.rsplit(coversDir))

    # Only sort releases
    if ("[" in name) and ("]" in name):

        item = {
            "artist": "",
            "release_name": "",
            "year": ""
        }

        # Split name via path "/"
        if os.name == 'nt':
            nameSplit = name.split("\\")
        else:
            nameSplit = name.split("/")

        # Get artist as first directory
        item["artist"] = nameSplit[0]

        # Extract year from "[]"
        item["year"] = re.search('(?<=\[).+?(?=\])', nameSplit[1]).group(0)

        # Extract Title - everything after "]"
        item["release_name"] = re.search('(?<=\] ).*', nameSplit[1]).group(0)

        # Add item to data array
        data.append(item)


# Save data to json file
with open('album-covers-data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
