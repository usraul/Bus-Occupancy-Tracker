import json
import serial
import pynmea2
from datetime import datetime, timezone, timedelta

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

IST = timezone(timedelta(hours=5, minutes=30))

print("Reading GPS data...")

while True:
    raw = ser.readline()
    if not raw:
        continue

    line = raw.decode('ascii', errors='ignore').strip()
    if not line.startswith('$'):
        continue

    try:
        msg = pynmea2.parse(line)

        if msg.sentence_type == 'RMC' and msg.status == 'A':
            gps_utc = datetime.combine(
                msg.datestamp,
                msg.timestamp,
                tzinfo=timezone.utc
            )

            local_time = gps_utc.astimezone(IST)

            print(
                f"UTC: {gps_utc} | "
                f"Local: {local_time} | "
                f"Lat: {msg.latitude} | "
                f"Lon: {msg.longitude}"
            )

            # ✅ Write JSON inside the valid block
            gps_data = {
                "utc": str(gps_utc),
                "local": str(local_time),
                "lat": msg.latitude,
                "lon": msg.longitude
            }

            with open("gps_data.json", "w") as f:
                json.dump(gps_data, f)

    except pynmea2.ParseError:
        pass
