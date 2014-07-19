#!/usr/bin/env python3 
from kakebo import Kakebo, Daily, Content
from utils import parse_date as _parse_date
from datetime import datetime as _datetime
from json import load as _json_load
from json import dump as _json_dump
from utils import (is_dummy_str,
                   except_head_of_space,
                   except_both_ends)


def get_formatter(filename):   
    d_format = {
                '.json': JsonFormatter(),
                '.txt':  TextFormatter(),
                '.yaml': YamlFormatter()
            }
    for extension in d_format.keys():
        if filename.endswith(extension):
            return d_format[extension]

    return None


class Formatter:
    def load(self, f):
        """
        @param: f: file object
        return Kakebo object
        """

    def dump(self, kakebo, f, indent=4):
        """
        save kakebo object to f.
        """


class TextFormatter(Formatter):   
    def load(self, f):
        """
        load: file object -> Kakebo
        return Kakebo Object from file object which is text-format
        """
        defined_first_money = False
        first_money         = None
        kakebo = None
        daily = None

        for line in f:
            if is_dummy_str(line):
                continue
            
            line = except_head_of_space(line)
            line = line.rstrip()

            # case: date
            if line.startswith('==='):
                line = line[len('==='): ]
                line = except_head_of_space(line)
                date = _parse_date(line)
                if daily is not None:
                    kakebo.append(daily)
                daily = Daily(date)
                continue

            # case: content
            content_name, income, rest = line.split(':')
            content_name, income, rest = map(
                    except_both_ends, 
                    (content_name, income, rest))
            rest, income = map(int, (rest, income))
            if kakebo is None:
                first_money = rest - income
                kakebo = Kakebo(first_money)
            content = Content(content_name, income)
            daily.append(content)
        kakebo.append(daily)
        return kakebo
        

    def dump(self, kakebo, f, indent=4):
        out = ''

        rest_money = kakebo.get_first_money()

        for daily in kakebo:
            year, month, day = daily.get_date().timetuple()[:3]
            s_date = '{:02d}/{:02d}/{:02d}'.format(year, month, day)
                # string format of date
            out += '=== {}\n'.format(s_date)
            for content in daily:
                income      = content.get_income()
                rest_money += income
                name        =  content.get_content_name()
                out        += '{space}{content}:{income}:{rest}\n'.format(
                    space   = ' ' * indent,
                    content = name,
                    income  = income,
                    rest    = rest_money
                )
        print(out[:-1], file=f)   # delete new line and space
    


class JsonFormatter(Formatter): 
    def load(self, yf): 
        """ jf:  json file object """
        ydata = _json_load(yf)
        print(ydata)
        first_money = jdata[0]
        del(jdata[0])
        kakebo = Kakebo(first_money)

        while jdata:
            date = _parse_date(jdata[0])
            daily = Daily(date)
            del(jdata[0])

            for a_content in jdata[0]:
                s_content, income = a_content
                ignore_statics = False
                if s_content.startswith('#') is True:
                    ignore_statics = True
                content = Content(
                    s_content, income, ignore_statics=ignore_statics)
                daily.append(content)
            del(jdata[0])
            kakebo.append(daily)
        return kakebo
    

    def dump(self, kakebo, f, indent=4):
        _json_dump(kakebo.get_buildin_obj(), f, indent=indent)
    
class YamlFormatter(Formatter):
    """ Formatter for yaml language """
    def load(self, f):
        from yaml import load as yaml_load
        ydata = yaml_load(f)
        first_money = ydata[0]
        del(ydata[0])
        kakebo = Kakebo(first_money)

        while ydata:
            date = _parse_date(ydata[0])
            daily = Daily(date)
            del(ydata[0])

            for a_content in ydata[0]:
                s_content, income = a_content
                ignore_statics = False
                if s_content.startswith('#') is True:
                    ignore_statics = True
                content = Content(
                    s_content, income, ignore_statics=ignore_statics)
                daily.append(content)
            del(ydata[0])
            kakebo.append(daily)
        return kakebo

    def dump(self, kakebo, f, indent=4):
        from yaml import dump as _yson_dump
        _yson_dump(kakebo.get_buildin_obj(), f, indent=indent)


#test 
def json_test():
    # load_test
    json_filename = 'kakebo.json'
    jf = open(json_filename, 'r')
    formatter = JsonFormat()
    kakebo = formatter.load(jf)
    print(kakebo)

    jf2 = open('kakebo2.json', 'w')
    formatter.dump(kakebo, jf2)


def text_dump_test():   
    # load
    filename = 'out_test.txt'
    formatter = JsonFormat()
    f = open(filename, 'r')
    kakebo = formatter.load(f)
    print(kakebo)

    # dump
    of = open('out_test_write.txt', 'w')
    formatter.dump(kakebo, of)

def yaml_format_test():
    filename = 'input_test.yaml'
    formatter = YamlFormatter()
    f = open(filename, 'r')
    
    # load test
    kakebo = formatter.load(f)
    
    # dump test
    of = open('out_test.yaml', 'w')
    formatter.dump(kakebo, of)

if __name__ == '__main__':
    yaml_format_test()
