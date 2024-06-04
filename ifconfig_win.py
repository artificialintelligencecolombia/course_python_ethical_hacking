#!/usr/bin/env python3
import platform
import subprocess


def main():
    if platform.system() == "Windows":
        subprocess.call("ipconfig", shell= True) # execute on windows
    else:
        subprocess.call("ifconfig", shell=True) # execute on unix
        
if __name__ == "__main__":
    main() # Run main function if this script is the main program {usr_mac}