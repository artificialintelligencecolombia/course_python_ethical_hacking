#!/usr/bin/env python

# We can pass variables/arguments at the script calling in the cli.
# python mac_spoof.py --interface eth0 --mac 00:11:22:33:44:55

import subprocess
import optparse # This module allows the user to input arguments in the cli
# and parse them to be used whitin the code.

# Create instance for OptionParser class, which can handle user inputs used as
# arguments
parser = optparse.OptionParser()

# Add the options for the parser object
parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')
# 'dest=' specifies the attr name where the option value will be stored.
# 'help' provides a description of what the option does. 

# parse_args() parses the options provided on the command line
# 'values' will contain the actual values of the options
# 'attrs' is typically used to handle any remaining arguments that are not options
(values, attrs) = parser.parse_args()

# Store the command-line arguments (options) into variables for later use
usr_interface = values.interface
usr_new_mac = values.new_mac

# Define the function that changes the MAC address
def mac_spoofer(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"]) # Bring down the network interface
    subprocess.call(["ifconfig", interface, "hw","ether", new_mac]) # Change the MAC address of the interface
    subprocess.call(["ifconfig", interface, "up"]) # Bring up the network interface
    print("MAC address changed successfully") # Print a success message

# This condition ensures that the script runs only if it is executed directly, not when imported
if __name__ == '__main__':
    mac_spoofer(usr_interface, usr_new_mac)