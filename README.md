# 🚌 Bus Occupancy Tracker

A real-time bus occupancy monitoring system built on a **Raspberry Pi** that combines live GPS tracking with AI-powered passenger counting using **YOLOv8**. Data is served via a Flask API and visualized on a locally hosted web dashboard.

---

## 📌 Features

- 🛰️ **Live GPS Tracking** — Reads NMEA data from a GPS module over serial and converts to IST
- 👥 **AI Passenger Detection** — Uses YOLOv8 and a webcam to count passengers in real time
- 🔗 **Data Fusion** — Combines GPS and person count into a unified data stream
- 🌐 **Flask API** — Exposes live bus data as a JSON endpoint for external consumption
- 🗺️ **Web Dashboard** — Locally hosted page showing live map location and occupancy

---

## 🗂️ Project Structure

```
Bus-Occupancy-Tracker/
│
├── gps_read2.py          # Reads GPS data from serial and writes to gps_data.json
├── person_webcam1.py     # YOLOv8 person detection, writes to person_data.json
├── combine_data.py       # Fuses GPS + person count data and prints live output
├── pi_api.py             # Flask API endpoint for external access (/bus_data)
├── server.py             # Flask server for local web dashboard
│
├── templates/
│   └── index.html        # Web dashboard UI
│
├── gps_data.json         # Auto-generated — live GPS data (do not edit)
├── person_data.json      # Auto-generated — live person count (do not edit)
├── yolov8n.pt            # YOLOv8 nano model weights
│
├── requirements.txt      # Python dependencies
└── .gitignore
```

---

## ⚙️ Hardware Requirements

- Raspberry Pi (3B+ or later recommended)
- GPS Module (connected via `/dev/ttyAMA0` at 9600 baud)
- USB Webcam

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/usraul/Bus-Occupancy-Tracker.git
cd Bus-Occupancy-Tracker
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the System

Each component runs as a **separate process**. Open a terminal for each:

### Terminal 1 — GPS Reader
```bash
python gps_read2.py
```
Reads live NMEA sentences from the GPS module and writes `gps_data.json`.

### Terminal 2 — Person Detector
```bash
python person_webcam1.py
```
Runs YOLOv8 on the webcam feed, counts passengers, and writes `person_data.json`.

### Terminal 3 — Data Fusion (optional monitor)
```bash
python combine_data.py
```
Prints the combined GPS + occupancy data to the console every second.

### Terminal 4 — Web Dashboard
```bash
python server.py
```
Serves the dashboard at `http://<raspberry-pi-ip>:5000`

### Terminal 5 — External API (optional)
```bash
python pi_api.py
```
Exposes the bus data at `http://<raspberry-pi-ip>:5000/bus_data`

---

## 📡 API Reference

### `GET /bus_data`
Returns live bus data as JSON.

**Response:**
```json
{
  "lat": 9.9312,
  "lon": 76.2673,
  "passenger_count": 12,
  "timestamp": "2025-01-01 10:30:00+05:30",
  "total_seats": 50
}
```

### `GET /data`
Used internally by the web dashboard.

**Response:**
```json
{
  "lat": 9.9312,
  "lon": 76.2673,
  "count": 12,
  "utc": "2025-01-01 05:00:00+00:00",
  "local": "2025-01-01 10:30:00+05:30"
}
```

---

## 📦 Dependencies

Key libraries used:

- `ultralytics` — YOLOv8 model for person detection
- `opencv-python` — Webcam frame capture and annotation
- `flask` — Web server and API
- `pynmea2` — NMEA GPS sentence parsing
- `pyserial` — Serial communication with GPS module

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🔒 Notes

- `gps_data.json` and `person_data.json` are auto-generated at runtime and not tracked in git
- `yolov8n.pt` model weights are downloaded automatically by `ultralytics` on first run if not present
- The system is designed to run fully offline on the Raspberry Pi

---

## 👤 Author

**usraul** — [github.com/usraul](https://github.com/usraul)
