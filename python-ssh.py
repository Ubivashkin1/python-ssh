import time
import configparser
import argparse
from netmiko import ConnectHandler

# Script reads the parameters from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Define Timestamp variable (data/time)
timestr = time.strftime("%d.%m.%y-%H.%M.%S")

# Link to config.ini file using configparser
username = config['CONFIGURATION']['USERNAME']
password = config['CONFIGURATION']['PASSWORD']
ip_address = config['CONFIGURATION']['IP_ADDRESS']
device_type = config['DEFAULT']['DEVICE_TYPE']


# Test to make sure code initialises
print("Before Config Push")


def run_command():

    # Initialise SSH connection to target device. Device/IP/Username/Password
    device = ConnectHandler(device_type=str(device_type), ip=str(ip_address), username=str(username),
                            password=str(password))

    # Send desired command matching CLI of type/model of device
    output = device.send_command(str(command_input))

    # Create file with timestamp as file name + device hostname
    with open(str(timestr + "_ar1220_config.txt"), "w+") as confile:

        # Write command output contents to the newly created file in above line
        confile.write(output)

    # Disconnect from ssh session to prevent hanging sessions
    device.disconnect()


def runn():

    global command_input
    option_long = "--command"
    option_short = "-c"

    # initiate the parser
    parser = argparse.ArgumentParser()

    # add long and short argument
    parser.add_argument(str(option_long), str(option_short), help="specify desired command")

    # read arguments from the command line
    args = parser.parse_args()

    command_input = "dis_ip_int_bri"

    if args.command:
        if args.command == command_input:
            run_command()
            print("Iworked")


runn()
