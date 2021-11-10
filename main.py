"""
Log ideas so that I don't have them in 100+ tabs in IDE.

############
TODO:
Create a pointer for directory:
    calling py app -c or --config -< capability to enter config
    config dir: /something
############

Author: Christian M. Fulton
Date: 09.Nov.2021
"""

from lib.ffs import Manage


def main():
    """
    
    """
    loopin = True
    fname = input('Enter the name for your file: ')

    my_file = Manage(fname)

    while loopin:
        usr_data = input('Enter the idea to log or !q to stop: ')
        if usr_data == '!q':
            loopin = False
        else:
            my_file.write_line(usr_data)

if __name__ == '__main__':
    main()
