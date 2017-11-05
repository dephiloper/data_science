#!/usr/bin/env python3
import os
import sys
import shutil
file_path = "./venv/"

def create_venv():
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        os.system("python3 -m venv venv/")

def install_requirements():
    create_venv()
    os.system("venv/bin/pip install -r requirements.txt")

def remove_venv():
    shutil.rmtree(file_path)

def show_help():
    print("Help:")
    print("setup -c create venv")
    print("setup -i install venv requirements (+create)")
    print("setup -r remove venv")
    print("setup -h show help menu")

menu = {
    "-c" : create_venv,             #create venv
    "-i" : install_requirements,    #install venv requirements
    "-r" : remove_venv,             #remove venv
    "-h" : show_help                #show help menu
}

if sys.argv[1] in menu.keys():
    menu[sys.argv[1]]()
else:
    print_help()
