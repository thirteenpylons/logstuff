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

from ffs import Manage

APP_LOCATION = os.path.abspath('.')

def main():
    """
    gather data
    """
    loopin = True
    fname = input('Enter the name for your file: ')

    make_dir()
    
    my_file = Manage(APP_LOCATION + '/' + get_dir() + '/' + fname)

    while loopin:
        usr_data = input('Enter the idea to log or to stop type !q: ')
        if usr_data == '!q':
            loopin = False
        else:
            my_file.write_line(usr_data)

def config(args):
    """
    This function will create config.ini
    """
    config = configparser.ConfigParser()

    this_arg = args.pop()

    print('Writing to config...')
    config['WORKING_DIR'] = {'Directory': this_arg}
    with open(APP_LOCATION + '/' + 'config.ini', 'w') as cfile:
        config.write(cfile)
    print(f'Target directory changed to {this_arg}.')

def get_dir():
    """
    Retrieves the pointer stored in config
    """
    c = configparser.ConfigParser()
    c.read('config.ini')
    return c['WORKING_DIR']['Directory']

def make_dir():
    """
    Check to see if dir exists from config pointer
    ... If it doesn't exist -> create it
    """
    if get_dir() not in os.listdir(APP_LOCATION):
        os.mkdir(APP_LOCATION + '/' + get_dir())

def execute(args):
    """
    point execution in right direction
    """
    err = 'Usage: python iLog -c [targer_dir]'
    if len(args) > 1:
        config(args[1:2])
    elif len(args) == 0:
        main()
    else:
        print(err)
