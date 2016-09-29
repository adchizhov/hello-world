# -*- coding: utf-8 -*-

import re
from commands import (read_file,
                      write_to_file,
                      clear_file)
__author__ = 'adchizhov'


print('List of acceptable commands:')
commands = ['show all marks',
             'add <pupil name> from <class> got <grade> on <lesson>',
             'show <puple name> from <class> marks', 'clear file']


for index, comm in enumerate(commands):
    print(index, comm)

if __name__ == "__main__":
    while True:
        user_input = input('Which command you want to perform? (press Enter to exit) ')
        if not user_input:
            print('bye-bye')
            break
        elif user_input.startswith('add'):
            write_to_file('storage.txt', user_input + '\n')
        elif user_input == 'show all marks':
            print(re.findall(r'\s\d\s', read_file('storage.txt')))
        elif user_input.startswith('show'):
            pass
        elif user_input.startswith('clear'):
            clear_file('storage.txt')
        else:
            print('wrong command pattern, please try again')