import json
import time

def combine_data():

    print("Starting data fusion...\n")

    while True:
        try:
            with open("gps_data.json", "r") as f:
                gps = json.load(f)

            with open("person_data.json", "r") as f:
                person = json.load(f)

            combined = {
                "utc": gps["utc"],
                "local": gps["local"],
                "latitude": gps["lat"],
                "longitude": gps["lon"],
                "person_count": person["person_count"]
            }

            print(combined)

        except:
            print("Waiting for data...")

        time.sleep(1)


if __name__ == "__main__":
    combine_data()
