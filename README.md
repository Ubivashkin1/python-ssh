# Python config retrieval tool

A python-based ssh script for automation and management of network devices

### Usage

```
usage: python-ssh.py [-h] [--command COMMAND]

optional arguments:
  -h, --help            show this help message and exit
  --command COMMAND, -c COMMAND
                        specify desired command
```                 
                      
### Example

```
$ python3 python-ssh.py -c "dis cur"

$ python3 python-ssh.py -c "dis ip int bri"

$ python3 python-ssh.py -c-command "dis cur"
```

### Notes
- Please note that the command syntax is specific to the device:
    - e.g dis cur on huawei or show run on cisco would display full configuration
    - commands should be embedded into double quotation marks when invoked eg "python-ssh.py -c "dis cur"

- For a full list of device types please refer to: 
https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py#L70

- Current script functionality does not incorporate entering privileged or global configuration
modes (e.g enable or conf t on Cisco or system-view on Huawei)

### Disclaimer

> - It is your responsibility to exercise caution and check which commands are being executed on the device, as per your 
> input. I do not accept any responsibility for any commands that are potentially destructive and 
> can cause irreversible damage to production environments.

> - This script has only been tested on Huawei devices, so please use at your own risk with other vendors

> - I do not accept any responsibility for unauthorised  or malicious use of this script. This is intended solely for 
> testing and educational purposes