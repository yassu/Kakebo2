#!/usr/bin/env python3 
from statics import ALL_STATS

from sys      import stdout   as _stdout
from json     import load     as _json_load
from copy     import deepcopy as _deepcopy
from datetime import datetime as _datetime
from math     import sqrt

class Content:
    def __init__(self, content_name , income):
        self._content_name = content_name
        self._income = income
	
    def get_content_name(self):
        return self._content_name

    def get_income(self):
        return self._income

    def __len__(self):
        l = len(self.get_content_name())
        return len(self.get_content_name())

    def __repr__(self):
        return 'Content<name={}, income={}>'.format(self._content_name, self._income)

class Daily:
    def __init__(self, date):
        """ date is datetime instance """
        self._date = date
        self._contents = []
	
    def append(self, content):
        self._contents.append(content)
	
    def get_date(self):
        return self._date

    def get_year(self):
        return self._date.timetuple()[0]

    def get_month(self):
        return self._date.timetuple()[1]

    def get_day(self):
        return self._date.timetuple()[2]

    def get_week_day(self):
        """
        0 means Monday and 6 means Sunday.
        """
        return self._date.timetuple()[6]

    def get_contents(self):
        return deepcopy(self._contents)

    def obtain_income(self):
        return sum(content.get_income() for content in self._contents)

    def __getitem__(self, ind):
        return self._contents[ind]

    def __repr__(self):
        year  = self._date.year
        month = self._date.month
        day   = self._date.day
        return '{year:04d}/{month:02d}/{day:02d}<{contents}>'.format(
                year  = year,
                month = month,
                day   = day,
                contents = self._contents) 
		

class Kakebo:
    def __init__(self, first_money):
        self._first_money = first_money
        self._dailies = []
	
    def append(self, daily):
        self._dailies.append(daily)
	
    def get_first_money(self):
        return self._first_money
	
    def get_dailies(self):
        return deepcopy(self._dailies)

    ## statics
    def obtain_incomes(self):
        return [daily.obtain_income() for daily in self._dailies]

    def obtain_income(self):
        return sum(self.obtain_incomes())

    @staticmethod
    def load_from_json(jf):
        """ jf:  json file object """
        jdata = _json_load(jf)
        first_money = jdata[0]
        del(jdata[0])
        kakebo = Kakebo(first_money)

        while jdata:
            date = parse_date(jdata[0])
            daily = Daily(date)
            del(jdata[0])

            for a_content in jdata[0]:
                s_content, income = a_content
                content = Content(s_content, income)
                daily.append(content)
            del(jdata[0])
            kakebo.append(daily)
        return kakebo

    def output(self, outfile, indent=4):
        """ output as a text file """
        out = ''

        money = self._first_money

        for daily in self:
            year, month, day = daily.get_date().timetuple()[:3]
            s_date = '{:02d}/{:02d}/{:02d}'.format(year, month,day)	
                # string format of date
            out += '=== {}\n'.format(s_date)
            for content in daily:
                money += content.get_income()
                name = content.get_content_name()
                out += '{space}{content}:{income}:{rest}\n'.format(
                            space = ' ' * indent,
                            content = name,
                            income = content.get_income(),
                            rest = money
                        )
        out += '\n'

        print(out, file=outfile)

    def print_statics(self, outfile=_stdout):
        for stat in ALL_STATS:
            print(stat.rep_result(self), file=outfile)
        
	
    def _iter_content(self):
        """
        iterator of contents
        """
        for daily in self:
            for content in daily:
                yield content

    def act_filter(self, filter_method, filter_args):
        self._dailies = list(filter(filter_method(*filter_args), self._dailies))
        self._first_money = None    # means we cant't use this attribute

    def __len__(self):
        return len(self._dailies)

    def __getitem__(self, ind):
        return self._dailies[ind]

    def __repr__(self):
        return '\n'.join(map(str, self._dailies))

def parse_date(s_date):
    year, month, day = map(int, s_date.split('/'))
    return _datetime(year, month, day)


def income_test():
    jf = open('kakebo.json')
    kakebo = Kakebo.load_from_json(jf)
    print(kakebo.obtain_income())

def obtain_average_of_income_test():
    jf = open('kakebo.json')
    kakebo = Kakebo.load_from_json(jf)
    print(kakebo.obtain_average_of_income())

def obtain_variance_of_income_test():
    jf = open('kakebo.json')
    kakebo = Kakebo.load_from_json(jf)
    print(kakebo.obtain_variance_of_income())

def obtain_correlation_test():
    jf = open('kakebo.json')
    kakebo = Kakebo.load_from_json(jf)
    print(kakebo.obtain_correlation_coefficient())

def output_test():
    jf = open('kakebo.json')
    kakebo = Kakebo.load_from_json(jf)
    kakebo.output(outfile=_stdout)

def main_test():
    jf = open('kakebo.json')
    kakebo = Kakebo.load_from_json(jf)
    kakebo.print_statics()
	
def main(filename):
    jf = open(filename, 'r')	
    kakebo = Kakebo.load_from_json(jf)
    kakebo.print_statics()

main('kakebo.json')

