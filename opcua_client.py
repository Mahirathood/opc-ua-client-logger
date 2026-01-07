from opcua import Client
from datetime import datetime
import pandas as pd
import time
import os

SERVER_URL = "opc.tcp://localhost:1000"
OUTPUT_DIR = "sample_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
client = Client(SERVER_URL)
client.connect()
print("Now Connected to the OPC UA Server...")

objects = client.get_objects_node()
children = objects.get_children()

tag_nodes = {}
for child in children:
    name = child.get_browse_name().Name
    if name.startswith("Tag"):
        tag_nodes[name] = child

if len(tag_nodes) != 10:
    raise Exception(f"Expected 10 tags, found {len(tag_nodes)}")

current_hour = None
data_buffer = []

try:
    while True:
        now = datetime.now()
        hour_key = now.strftime("%d-%m-%Y_%H")
        if hour_key != current_hour:
            if data_buffer and current_hour:
                df = pd.DataFrame(data_buffer)
                df.to_csv(f"{OUTPUT_DIR}/OPC_Log_{current_hour}.csv", index=False)
                data_buffer.clear()
            current_hour = hour_key
        row = {
            "Timestamp": now.strftime("%d-%m-%Y %S:%M:%H"),
            "EpochTime": int(now.timestamp())
        }
        for i in range(1, 11):
            row[f"Tag{i}"] = tag_nodes[f"Tag{i}"].get_value()
        data_buffer.append(row)
        print(row)
        time.sleep(60)
except KeyboardInterrupt:
    print("Stopping OPC UA Client")
finally:
    client.disconnect()
