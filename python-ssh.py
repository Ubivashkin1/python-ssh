import datetime
from netmiko import ConnectHandler

print("Before Config Push")

device = ConnectHandler(device_type="huawei", ip="10.100.20.99", username="admin", password="Password1")

output = device.send_command("dis ip int brief")

#print(output)

x = datetime.datetime.now()

f = open(x.strftime("%B"), "w+")

f.write(output)

device.disconnect()

print("After Config Push")