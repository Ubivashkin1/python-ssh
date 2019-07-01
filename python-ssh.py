import time
import configparser
from netmiko import ConnectHandler

# Script reads the parameters from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Link to config.ini file using configparser
username = config['CONFIGURATION']['USERNAME']
password = config['CONFIGURATION']['PASSWORD']
ip_address = config['CONFIGURATION']['IP_ADDRESS']
device_type = config['DEFAULT']['DEVICE_TYPE']

# Test to make sure code initialises
print("Before Config Push")

def connect_ssh():

    # Initialise SSH connection to target device. Device/IP/Username/Password
    device = ConnectHandler(device_type=str(device_type), ip=str(ip_address), username=str(username), password=str(password))

    # Send desired command matching CLI of type/model of device
    output = device.send_command("dis ip int brief")

    # Define Timestamp variable (data/time)
    timestr = time.strftime("%d.%m.%y-%H.%M.%S")

    # Create file with timestamp as file name + device hostname
    with open(str(timestr + "_ar1220_config.txt"), "w+") as confile:

        # Write command output contents to the newly created file in above line
        confile.write(output)

    # Disconnect from ssh session to prevent hanging sessions
    device.disconnect()

connect_ssh()
