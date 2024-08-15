#!/usr/bin/env python3
# This script should be running by using py3 interpreter.

import platform
import subprocess
# 'platform' access the platform data, such as the OS type.
# 'subprocess' allows to spawn new processes -> used to execute shell commands within python

def main():
    if platform.system() == "Windows": # checks the operating system type
        subprocess.call("ipconfig", shell= True) # execute on windows
    else:
        subprocess.call("ifconfig", shell=True) # execute on unix
        
if __name__ == "__main__":
    main() # Run main function if this script is the main program {usr_mac}