from curses import echo
from os import system as console_log
import requests as httpserver
import platform as device
from time import sleep as sleep_me

try:
    if "Windows" in device.system():
        console_log("cls")
    else:
        console_log("clear")
except (NameError,IOError):
    exit()

class __devicemanageratme__(object):
    def __init__(self) -> None:
        console_log("cls")
        try:
            self.abm = device.architecture()
            try:
                if "64bit" in self.abm:
                    console_log("cd device && python class.py")
                else:
                    echo(f" Your device are not support like 32bit {self.abm} and wait for 32bit script coming soon")
            except(FileNotFoundError,FileExistsError):
                echo(f" 32bit not support")
                sleep_me(2)
                exit()
        except(KeyError,IOError,NameError):
            echo(" Something wrong please try again ")
            sleep_me(2)
            exit()
            
if __name__ == '__main__':
    print = echo
    __devicemanageratme__()
