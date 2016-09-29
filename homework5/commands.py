# -*- coding: utf-8 -*-

def write_to_file(file, text):
    my_file = open(file, 'a')
    my_file.write(text)
    my_file.close()


def read_file(file):
    my_file = open(file, 'r')
    my_str = my_file.read()
    return my_str


def clear_file(file):
    my_file = open(file, 'w')
    my_file.write('')
    my_file.close()


def find_puple(name, text):
    match = re.search(name, text)
    if match:
        return match.group()
    else:
        print('not found')