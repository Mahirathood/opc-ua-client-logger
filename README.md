# OPC UA Client Logger
This repository contains the solution for **Assignment 2: OPC UA Client Development and Data Logging**.
The project demonstrates a basic OPC UA client-server setup using Python, where a local OPC UA server simulates data and a client reads and logs that data into CSV files.

---
## Project Overview
- A local OPC UA server is implemented using Python to simulate OPC UA tags.
- The server generates 10 dummy tags (`Tag1` to `Tag10`) with continuously changing values.
- An OPC UA client connects to the server and reads all tag values once every minute.
- The client logs the collected data into CSV files with timestamps and epoch time.
- CSV files are created based on hourly logging logic.
---

## Technologies Used
- Python 3.x
- opcua (Python OPC UA library)
- pandas (for CSV data handling)
---

## Project Structure


opc-ua-client-logger/
├── opcua_server.py
├── opcua_client.py
├── instructions.txt
├── screenshots/
│ ├── server_running.png
│ ├── client_running.png
│ ├── csv_hour1.png
│ └── csv_hour2.png
└── sample_output/
└── OPC_Log_YYYY-MM-DD_HH.csv

---
## How to Run the Project
### 1. Install Dependencies
python -m pip install opcua pandas

### 2. Start the OPC UA Server
python opcua_server.py
The server will start locally at: opc.tcp://localhost:1000

### 3. Run the OPC UA Client
Open a new terminal window and run:
python opcua_client.py

The client will connect to the server, read tag values every minute, and log the data into CSV files.

---
## Output
- CSV files are generated in the `sample_output` folder.
- Each CSV file contains:
  - Timestamp
  - Epoch time
  - Values of Tag1 to Tag10
- File naming format: OPC_Log_YYYY-MM-DD_HH.csv
---

## Screenshots
Screenshots demonstrating server execution, client execution, and CSV output are included in the `screenshots` folder.

---
## Purpose
This project was developed as part of an academic assignment to demonstrate OPC UA client-server communication, periodic data acquisition, and automated data logging using Python.

---
## Author
**Mahendar Bhukya**


