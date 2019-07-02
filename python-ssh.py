import time
import configparser
import argparse
from netmiko import ConnectHandler

# Script reads the parameters from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Define Timestamp variable (data/time)
timestring = time.strftime("%d.%m.%y-%H.%M.%S")

# Link to config.ini file using configparser
username = config['CONFIGURATION']['USERNAME']
password = config['CONFIGURATION']['PASSWORD']
ip_address = config['CONFIGURATION']['IP_ADDRESS']
device_type = config['DEFAULT']['DEVICE_TYPE']


# Test to make sure code initialises
print("Before Config Push")


# Connects to a device and executes a command (-c COMMAND) during script execution
def run_command():

    # Initialise SSH connection to target device. Device/IP/Username/Password
    device = ConnectHandler(device_type=str(device_type), ip=str(ip_address), username=str(username),
                            password=str(password))

    # Send desired command matching CLI of type/model of device
    output = device.send_command(str(command_input))

    # Create file with timestamp as file name + device hostname
    with open(str(timestring + "_ar1220_config.txt"), "w+") as confile:

        # Write command output contents to the newly created file in above line
        confile.write(output)

    # Disconnect from ssh session to prevent hanging sessions
    device.disconnect()


def argument_parser():

    global command_input
    option_long = "--command"
    option_short = "-c"

    # initiate the parser
    parser = argparse.ArgumentParser()

    # add long and short argument
    parser.add_argument("-c", "--command", help="specify desired command")

    # read arguments from the command line
    args = parser.parse_args()

    command_input = args.command

    # checks if any arguments during script execution
    if args.command:

        # executes run_command function if -c was used in combination with a command
        # like "display current configuration"
        run_command()
        print("Iworked")


argument_parser()
