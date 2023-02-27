from libs.listproxy import *
from time import sleep
import os

banner = '''
+==========================+
  =    By PabloBzerra    =

API: https://geonode.com
+==========================+
'''

banner2 = '''
 _____                 _____         
|  _  |___ ___ _ _ _ _|   __|___ ___ 
|   __|  _| . |_'_| | |  |  | -_|   |
|__|  |_| |___|_,_|_  |_____|___|_|_|
                  |___|

PROTOCOL | ANONLEVEL | COUNTRY | IP | PORT
'''
def main():
    os.system("clear")
    print(banner)
    sleep(3)
    os.system("clear")
    print(banner2)
    ListProxy.gen()

main()