import json


# Directly from dictionary
def object_dump(json_string: json):
    with open("dump/json_data.json", "w") as outfile:
        json.dump(json_string, outfile)
    print("Complete!")


# Using a JSON string
def json_dump(json_string: str):
    with open("dump/json_data.json", "w") as outfile:
        outfile.write(json_string)
    print("Complete!")


def json_read():
    with open("dump/json_data.json") as json_file:
        data = json.load(json_file)
        print(data)
        return data
