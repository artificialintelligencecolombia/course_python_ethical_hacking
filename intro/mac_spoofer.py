#!/usr/bin/env python 3

# MAC SPoofer

# Import required libraries
import subprocess


def run_process():
    subprocess.call(["ipconfig"], shell=True)
    subprocess.call("ipconfig eth0 down", shell=True)
    subprocess.call(["ipconfig eth0 hw ether A0:B1:C2:D3:E4:F5"], shell=True)
    subprocess.call(["ipconfig eth0 up"], shell=True)
    subprocess.call(["ipconfig"], shell=True)
    print("Process executed")
    

run_process()
