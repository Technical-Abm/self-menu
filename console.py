import os
import platform
import subprocess
import Cython
import requests

try:
    import pip
except(NameError,IOError,OSError):
    os.system("python -m pip install -U --force-reinstall pip")

try:
    packages = ["requests","Cython"]
    pip.main(['install'] + packages + ['--upgrade'])
except(NameError,IOError,OSError):
    exit(f" Modules not installed, Please try again")

try:
    if "Windows" in platform.system():
        os.system("cls")
    else:
        os.system("clear")
except(NameError,IOError,OSError):
    exit(f"Something wrong")

os.system("cls")

puts = """
       __________  __  _______  ______    ______
      / ____/ __ \/  |/  / __ \/  _/ /   / ____/
     / /   / / / / /|_/ / /_/ // // /   / __/
    / /___/ /_/ / /  / / ____// // /___/ /___
    \____/\____/_/  /_/_/   /___/_____/_____/
---------------------------------------------------
 (~) Author :- Technical Abm
 (~) Github :- https://github.com/Technical-Abm
 (~) Page   :- https://www.facebook.com/techabm
 (~) Project:- Cython compile and reverse website
---------------------------------------------------
"""

class MENUUSER(object):
    def __init__(self) -> None:
        os.system("cls")
        print(puts)
        print(" [1] Get Source code from website")
        print(" [2] Install Cython and compile cython on python3")
        print(" [3] How to use Cython")
        print(" [4] Exit")
        print()
        self.menu = input(" [!] Enter an option :- ")
        if "1" in self.menu:
            os.system("cls")
            print(puts)
            print("\tUsage Example : https://www.google.com")
            print()
            try:
                self.here = input(" [!] Enter a website link here :- ")
                print(f" [!] Your website link is {self.here}")
                self.html = requests.get(self.here).text
                open("html.txt","w").write(self.html)
                print(f" Your website {self.here} files saved as html.txt ")
                input(" Press enter to back :- ")
                MENUUSER()
            except(FileNotFoundError,IOError,FileExistsError):
                print(f" You put {self.here} file not found")
                MENUUSER()
        elif "2" in self.menu:
            os.system("cls")
            print(puts)
            try:
                print(("\tCreate a python project without any error after run").expandtabs(1))
                print(("\tDo not use any encrypt before use cython").expandtabs(1))
                print()
                self.files = input(" [!] Enter file name to compile cython :- ")
                os.system("cythonize --3str -i "+self.files)
            except(FileNotFoundError,IOError,FileExistsError):
                print(f" You put {self.files} is not found")
                MENUUSER()
        elif "3" in self.menu:
            os.system("cls")
            print(puts)
            help = "cython --help"
            subprocess.Popen(help, shell=True)
            exit()
        elif "4" in self.menu:
            exit()

if __name__ == '__main__':
    MENUUSER()
