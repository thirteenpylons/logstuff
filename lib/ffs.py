"""
File manipulation lib

Author: Christian M. Fulton
Date: 03.Nov.2021
"""
import shutil
import os
from json import dumps
from json import loads


class Manage:
    """
    File lib
    :Use: Instantiate file object { fileobj = Manage('name') }
        -> Work with fileobj
    
    Parameter title: Title of the file to work with.
    Parameter save: Saves file as .txt by default.
    Preconditions: title must be a valid string following os naming convention
    """
    def __init__(self, title, save=True):
        self.title = title
        self.save = save
        self.ext = ''
        if save:
            self.make_file()

    def name(self):
        """return the name of the file with extension"""
        
        return self.title + self.ext
    
    def make_file(self, ext='.txt'):
        """
        Make file if it doesn't exist
        file extension default = .txt
        TODO: Ability to save to path..
        
        This currently creates a file in the path that the program is executed.

        """
        self.ext = ext
        if not ext.startswith('.'):
            ext = '.' + ext
        if self.name() in os.listdir():
            print('File already exists...')
        else:
            # check to see if file exists before creation
            fname = open(self.name(), 'wt')
            fname.close()
    
    def write_line(self, data):
        """
        Append existing file with single line
        """
        with open(self.name(), 'a') as rfile:
            rfile.write(data + '\n')
    
    def write_data(self, data):
        """
        Write data: should be tuple | list
        """
        NotImplementedError
    
    def read_me(self):
        """
        Read the file
        """
        with open(self.name(), 'r') as rfile:
            for line in rfile.readlines():
                print(line)

    def move_me(self, dst):
        """
        Move file around
        Parameter dst:
        Preconditions:
        """
        # if you're moving the file, you have to move with it 
        #   || have a pointer -> file
        # if dst == '..' -> move up 1 level
        if dst == '..':
            dst = os.path.abspath(os.path.join('.', os.pardir))
        try:
            shutil.move(self.name(), dst)
        except:
            print(f'An error occurred when trying to move {self.title}')

    def read_counter(self):
        """
        :Use: create an instance: counter = Manage.read_counter()
        """
        if os.path.exists('counter.json'):
            return loads(open('counter.json'), 'r') + 1
    
    def write_counter(self):
        """
        Works with read_counter()
        :Use: atexit.register(counter)
        """
        counter = self.read_counter()
        with open('counter.json', 'w') as rfile:
            rfile.write(dumps(counter))

class Fthis:
    """
    play with fs
    """
    NotImplementedError