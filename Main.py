import os
import sys
import time

black='\033[30m'
red='\33[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
bold='\033[1m'
white  = '\33[37m'

def cls():
    os.system("clear")
def logo():
    print yellow + """
        __  __           __
       / / / /___  _____/ /____  _____
      / /_/ / __ \/ ___/ __/ _ \/ ___/
     / __  / /_/ (__  ) /_/  __/ /
    /_/ /_/\____/____/\__/\___/_/
"""
cls()
logo()
print cyan + "     Expose Your Localhost On The Web"
print ""
print lightgreen + bold + "[1] Ngrok "
print "[2] Localhost Run"
print white + ""
var=raw_input("Root@Kali:~$ ")
print yellow + bold + ""

if var == '1':
    varn=raw_input("Enter Port To Host : ")
    print ""
    print yellow + "Configuring Ngrok...."
    time.sleep(1)
    os.system("./ngrok http %s " % (varn))
elif var == '2':
    varl=raw_input("Enter Port To Host : ")
    print ""
    print yellow + "You Need a Ssh Key Linked To Your Github Account"
    print "Trying To Run..."
    os.system("ssh -R 80:localhost:%s ssh.localhost.run" % (varl))
