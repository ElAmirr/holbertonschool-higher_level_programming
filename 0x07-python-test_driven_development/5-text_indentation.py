#!/usr/bin/python3


def text_indentation(text):
    if not (isinstance(text, str)):
        raise TypeError('text must be a string')
    flag = 0
    for c in text:
        if(c == '.' or c == '?' or c == ':'):
            print(c, end='')
            print('')
            print('')
            flag = 1
        else:
            if (flag == 0):
                print(c, end='')
            else:
                if (c == ' ' or c == '\t'):
                    pass
                else:
                    print(c, end='')
                    flag = 0
