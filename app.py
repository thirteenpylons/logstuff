"""
Build a idea logger

Create a pointer for directory:
    calling py app -c or --config -> capability to edit config
    config dir: /something
    

Author: Christian M. Fulton
Date: 09.Nov.2021
"""
import configparser
import os
from os import path

from lib.ffs import Manage
from lib import options


# TODO: Move APP_LOCATION from both app.py and options.py into config.ini
APP_LOCATION = os.path.abspath("logstuff")


def main():
    """
    gather data
    """
    options.check_config()
    loopin = True
    fname = input("Enter the name for your file: ")

    make_dir()

    my_file = Manage(APP_LOCATION + "/" + get_dir() + "/" + fname)

    while loopin:
        usr_data = input("Enter the idea to log or to stop type !q: ")
        if usr_data == "!q":
            loopin = False
        else:
            my_file.write_line(usr_data)


def get_dir():
    """
    Retrieves the pointer stored in config
    """
    c = configparser.ConfigParser()
    c.read(APP_LOCATION + "/" + "config.ini")
    return c["WORKING_DIR"]["Directory"]


def make_dir():
    """
    Check to see if dir exists from config pointer
    ... If it doesn't exist -> create it
    """
    if get_dir() not in os.listdir(APP_LOCATION):
        os.mkdir(APP_LOCATION + "/" + get_dir())
        print(f"Successfully created directory {get_dir()}.")


def execute(args):
    """
    point execution in right direction
    """
    err = "Usage: python iLog <FLAG> [arg]"
    if len(args) > 1:
        options.flags(args)
    elif len(args) == 0:
        main()
    else:
        print(err)
