#!usr/bin/env python3
import subprocess

def mac_spoofer():
    interface = input("Interface >")
    new_mac = input("New MAC address (00:11:22:33:44:55)>")
    
    subprocess.call(["ipconfig", interface,"down"])
    subprocess.call(["ipconfig", interface,"hw","ether", new_mac])
    subprocess.call(["ipconfig", interface,"up"])
    print("MAC address successfully CHANGED")
    
if __name__ == "__main__":
    mac_spoofer()