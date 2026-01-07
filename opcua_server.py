from opcua import Server
import time
import random

server = Server()
server.set_endpoint("opc.tcp://localhost:1000")
server.set_server_name("This is Python OPC UA Demo Server")
uri = "http://example.opcua.server"
server.register_namespace(uri)
idx = 1

objects = server.get_objects_node()
tags = []
for i in range(1, 11):
    tag = objects.add_variable(idx, f"Tag{i}", 0)
    tag.set_writable()
    tags.append(tag)
server.start()
print("OPC UA Server is started now on opc.tcp://localhost:1000")
print("Namespace index used:", idx)
try:
    while True:
        for tag in tags:
            tag.set_value(random.randint(1, 100))
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping OPC UA Server")
finally:
    server.stop()
