#!/usr/bin/python3
""" Program that read file """


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout """
    with open(filename, encoding='utf8') as f:
        f_contents = f.read()
        print(f_contents,  end='')
