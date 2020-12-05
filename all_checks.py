import sys
import os

def main():
    if chec_reboot():
    	print("pending reboot")
    	sys.exit(1)
    else: 
    	print("everything okay")
    	sys.exit(0)

def chec_reboot():
    '''returns Ture if reboot is pending'''
    return os.path.exists("/run/reboot-required")

main()