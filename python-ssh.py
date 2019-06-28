import time
from netmiko import ConnectHandler

# Test to make sure code initialises
print("Before Config Push")

# Initialise SSH connection to target device. Device/IP/Username/Password
device = ConnectHandler(device_type="huawei", ip="10.100.20.99", username="admin", password="Password1")

# Send desired command matching CLI of type/model of device
output = device.send_command("dis ip int brief")

# Define Timestamp (data/time)
timestr = time.strftime("%d.%m.%y-%H.%M.%S")

# Create file with timestamp as file name + device hostname
f = open(str(timestr + "_ar1220_config.txt"), "w+")

# Write command output contents to the newly created file in above line
f.write(output)

# Disconnect from ssh session to prevent hanging sessions
device.disconnect()

