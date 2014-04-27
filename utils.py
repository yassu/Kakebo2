#!/usr/bin/env python3  
from itertools import dropwhile as _dropwhile
from datetime import datetime as _datetime

DUMPTY_CHARS = ('\n', '\t', ' ', '\r')

def trim(s):    #{{{
    """
    trim: string -> string
    ignore space charactors
    >>> trim('tjwppowqp')
    'tjwppowqp'
    """
    rm = lambda c: True if c not in DUMPTY_CHARS else False
    return ''.join(list(filter(rm, s)))
#}}}

def is_dummy_str(text): #{{{
    return list(filter(lambda c: c not in DUMPTY_CHARS, text)) == []
#}}}

def date_to_str(date):  #{{{
    year, month, day = date.timetuple()[:3]
    return '{:02d}/{:02d}/{:02d}'.format(year, month, day)
#}}}

def parse_date(s_date): #{{{
    # delete last of white space
    while s_date[-1] == ' ':
        s_date = s_date[:-1]

    year, month, day = map(int, s_date.split('/'))
    return _datetime(year, month, day) 
#}}}

def except_head_of_space(text): #{{{
    """
    except_head_of_test: str -> str
    ignore head of white space
    """
    while len(text) > 0 and text[0] in DUMPTY_CHARS:
        text = text[1:]
    return text
#}}}

def except_tail_of_space(text): #{{{
    """
    except_tail_of_test: str -> str
    ignore tail of white space
    """
    while len(text) > 0 and text[-1] in DUMPTY_CHARS:
        text = text[:-1]
    return text
#}}}

def except_both_ends(text): #{{{
    return except_tail_of_space(except_head_of_space(text))
#}}}

def is_dummy_str_test():#{{{
    dummy_text = '  \n  \r  \t  '
    print(is_dummy_str(dummy_text))  # -> True

    non_dummy_text = 'ahfp   qrjpq   '
    print(is_dummy_str(non_dummy_text))  # -> False
    #}}}


def except_both_ends_test():    #{{{
    text = '  ab  c  def '
    print(except_both_ends(text))
#}}}


if __name__ == '__main__':  #{{{
    import doctest
    doctest.testmod()
    s = trim('  \n tjwp  \n powqp \t  ')
#}}}

