#!/usr/bin/env python3 

"""
filter methods.
each functions returns function daily -> bool
"""

def since_year_filter(y):
    return lambda daily: daily.get_year()  >= y

def since_month_filter(m):
    return lambda daily: daily.get_month() >= m

def since_day_filter(d):
    return lambda daily: daily.get_day() >= d

def equal_to_year_filter(y):
    return lambda daily: daily.get_year() == y 

def equal_to_month_filter(m):
    return lambda daily: daily.get_month() == m

def equal_to_day_filter(d):
    return lambda daily: daily.get_day()   == d