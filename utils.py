#!/usr/bin/env python3  
from itertools import dropwhile as _dropwhile
from datetime import datetime as _datetime
from re import sub as _re_sub

DUMPTY_CHARS = ('\n', '\t', ' ', '\r')

def trim(s):    
    """
    trim: string -> string
    ignore space charactors
    """
    return _re_sub('[\n\r\t ]','',s)


def is_dummy_str(text): 
    return list(filter(lambda c: c not in DUMPTY_CHARS, text)) == []


def date_to_str(date):  
    year, month, day = date.timetuple()[:3]
    return '{:02d}/{:02d}/{:02d}'.format(year, month, day)


def parse_date(s_date): 
    # delete last of white space
    while s_date[-1] == ' ':
        s_date = s_date[:-1]

    year, month, day = map(int, s_date.split('/'))
    return _datetime(year, month, day) 

def trim_test():
    s = ' 12  3 4  56 7 8 9'
    assert(trim(s) == '123456789')

def is_dummy_str_test():
    dummy_text = '  \n  \r  \t  '
    print(is_dummy_str(dummy_text))  # -> True

    non_dummy_text = 'ahfp   qrjpq   '
    print(is_dummy_str(non_dummy_text))  # -> False


if __name__ == '__main__':
    trim_test()
