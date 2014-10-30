#!/usr/bin/env python3

"""
filter methods.
each functions returns function daily -> bool
"""

from const import d_date as _d_date


def since_filter(s_since):  
    a_sp = s_since.split('/')
    for i in range(len(a_sp)):
        if a_sp[i] == '':
            del(a_sp[i])
    a_since = list(map(int, a_sp))

    if len(a_since) == 0:
        year, month, day = 0, 0, 0
    if len(a_since) == 1:
        year = a_since[0]
        month, day = 0, 0
    if len(a_since) == 2:
        year, month = a_since[:2]
        day = 0
    if len(a_since) == 3:
        year, month, day = a_since[:3]

    def f(daily):
        if daily.get_year() > year:
            return True
        elif daily.get_year() < year:
            return False
        if daily.get_month() > month:
            return True
        elif daily.get_month() < month:
            return False
        if daily.get_day() > day:
            return True
        elif daily.get_day() < day:
            return False
        return True

    return f  


def equal_to_year_filter(y):  
    return lambda daily: daily.get_year() == y  


def equal_to_month_filter(m):  
    return lambda daily: daily.get_month() == m  


def equal_to_day_filter(d):  
    return lambda daily: daily.get_day() == d  


def equal_to_week_day_filter(s_wday):  
    """
    wday in (0, 1, 2, 3, 4, 5, 6)
    0 means Monday and 6 means Sunday.
    """
    return lambda daily: daily.get_week_day() == _d_date[s_wday]  

D_FILTER = {
    's_since_date': since_filter,
    'year': equal_to_year_filter,
    'month': equal_to_month_filter,
    'day': equal_to_day_filter,
    'wday': equal_to_week_day_filter
}
