#!/usr/bin/env python3
from statics        import ALL_STATS
from filter_methods import D_FILTER
from optparse       import OptionParser

from sys      import stdout   as _stdout
from json     import load     as _json_load
from copy     import deepcopy as _deepcopy
from datetime import datetime as _datetime
from math import sqrt


class Content:

    def __init__(self, content_name, income, ignore_statics=False):
        self._content_name = content_name
        self._income = income
        self._ignore_statics = ignore_statics

    def get_content_name(self):
        return self._content_name

    def get_income(self):
        return self._income

    def get_ignore_statics(self):
        return self._ignore_statics

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
        year = self._date.year
        month = self._date.month
        day = self._date.day
        return '{year:04d}/{month:02d}/{day:02d}<{contents}>'.format(
            year=year,
            month=month,
            day=day,
            contents=self._contents)


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

    # statics
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
                ignore_statics = False
                if s_content.startswith('#'):
                    ignore_statics = True
                content = Content(s_content, income, ignore_statics=ignore_statics)
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
            s_date = '{:02d}/{:02d}/{:02d}'.format(year, month, day)
                # string format of date
            out += '=== {}\n'.format(s_date)
            for content in daily:
                money += content.get_income()
                name = content.get_content_name()
                out += '{space}{content}:{income}:{rest}\n'.format(
                    space=' ' * indent,
                    content=name,
                    income=content.get_income(),
                    rest=money
                )
        print(out[:-2], file=outfile)   # delete new line and space

    def _obtain_ignore_statics_contents(self):
        kakebo = Kakebo(None)
        for daily in self:
            q_daily = Daily(daily.get_date())
            for content in daily:
                if content.get_ignore_statics() is False:
                    print(content)
                    q_daily.append(content)
            kakebo.append(q_daily)
        return kakebo

    def print_statics(self, outfile=_stdout):
        # except ignore statics contents
        kakebo = self._obtain_ignore_statics_contents()
        print('static kakebo:')
        print(kakebo)
        for stat in ALL_STATS:
            print(stat.rep_result(kakebo), file=outfile)

    def _iter_content(self):
        """
        iterator of contents
        """
        for daily in self:
            for content in daily:
                yield content

    def act_filter(self, filter_method, filter_args):
        self._dailies = list(
            filter(filter_method(*filter_args), self._dailies))
        self._first_money = None    # means we cant't use this attribute

    def plot(self):
        """
        plot graph of incomes by using matplotlib.pyplot
        """
        import pylab
        incomes = pylab.array(self.obtain_incomes())
        dates = pylab.array(range(len(incomes)))

        pylab.suptitle('Kakebo')    # title of this graph

        # draw datas
        pylab.plot(dates, incomes, 'b-', label='data')

        ## draw regression line
            # loop and sedgement of regression line of this Kakebo
        from scipy import polyfit
        loop, sedgement = polyfit(dates, incomes, 1).tolist()
        # plot regression line of incomes
        pylab.plot(dates, [loop * x + sedgement for x in dates], 'r-', label='regression line')

        # show graph
        pylab.legend(loc='upper left')
        pylab.show()

    def __len__(self):
        return len(self._dailies)

    def __getitem__(self, ind):
        return self._dailies[ind]

    def __repr__(self):
        return '\n'.join(map(str, self._dailies))


def parse_date(s_date):
    year, month, day = map(int, s_date.split('/'))
    return _datetime(year, month, day)

# Tests


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


def main(parser):
    jf = open(filename, 'r')
    kakebo = Kakebo.load_from_json(jf)
    kakebo.print_statics()


def build_options(parser):
    # assume fllowing dests of option == 
    parser.add_option(
        '-s', '--since',
        action='store',
        type='string',
        dest='s_since_date',
        help='since this date'
    )
    parser.add_option(
        '-y', '--year',
        action='store',
        type='int',
        dest='year',
        help='decide year'
    )
    parser.add_option(
        '-m', '--month',
        action='store',
        type='int',
        dest='month',
        help='month'
    )
    parser.add_option(
        '-d', '--day',
        action='store',
        type='int',
        dest='day',
        help='day'
    )
    parser.add_option(
        '-w', '--wday',
        action='store',
        type='string',
        dest='wday',
        help='weekday'
    )
    parser.add_option(
        '-g', '--graph',
        action='store_false',
        dest='is_plotting',
        help='plot datas'
    )
    parser.add_option(
        '-t', '--text',
        action='store_false',
        dest='output_as_text',
        help='output as plain text format'
    )

if __name__ == '__main__':
    is_main = True

    if is_main:
        # define option
        parser = OptionParser()
        build_options(parser)
        (options, filenames) = parser.parse_args()
        # print(options)
        try:
            filename = filenames[-1]
        except IndexError:
            print('Please enter filename.')
            exit()
        
        # define Kakebo
        kakebo = None
        with open(filename, 'r') as jf:
            kakebo = Kakebo.load_from_json(jf)

        # pass filter
        for filter_name, _filter in D_FILTER.items():
            filter_args = None
            if getattr(options, filter_name) is not None:
                filter_args = None
                if getattr(options, filter_name):
                    filter_args = [getattr(options, filter_name)]
                else:
                    filter_args = []
                kakebo.act_filter(_filter, filter_args)

        # outputs
        kakebo.print_statics()

        if options.is_plotting is not None:
            kakebo.plot()
        if options.output_as_text is not None:
            kakebo.output(outfile=_stdout)
