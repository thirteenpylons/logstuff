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

APP_LOCATION = os.path.abspath('logstuff')

def main():
    """
    gather data
    """
    check_config()
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

def check_config():
    """
    Checks directory for config. If config not in dir -> assign default
    Default will be: foobar
    """
    if 'config.ini' not in os.listdir(APP_LOCATION):
        default = ['foobar']
        config(default)
        # default pops before even printed
        # probably should be checking get_dir() for config.ini existence
        print(f'Default directory {default} created... Use --config to change default.')

def get_dir():
    """
    Retrieves the pointer stored in config
    """
    c = configparser.ConfigParser()
    c.read(APP_LOCATION + '/' + 'config.ini')
    return c['WORKING_DIR']['Directory']

def make_dir():
    """
    Check to see if dir exists from config pointer
    ... If it doesn't exist -> create it
    """
    if get_dir() not in os.listdir(APP_LOCATION):
        os.mkdir(APP_LOCATION + '/' + get_dir())
        print(f'Successfully created directory {get_dir()}.')

def execute(args):
    """
    point execution in right direction
    """
    err = 'Usage: python iLog -c [targer_dir]'
    if len(args) > 1:
        if '-c' in args[:1] or '--config' in args[:1]:
            config(args[1:2])
    elif len(args) == 0:
        main()
    else:
        print(err)
