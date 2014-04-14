#!/usr/bin/env python3 
from kakebo import Kakebo, Daily, Content, parse_date

from json import load as _json_load
from json import dump as _json_dump

class AbstractFormatter:
    def load(self, f):
        pass

    def dump(self, kakebo, f, indent=4):
        pass

class JsonFormatter(AbstractFormatter):
    def load(self, jf):#{{{
        """ jf is a json file object """
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
                if s_content.startswith('#') is True:
                    ignore_statics = True
                content = Content(
                    s_content, income, ignore_statics=ignore_statics)
                daily.append(content)
            del(jdata[0])
            kakebo.append(daily)
        return kakebo
    #}}}

    def dump(self, kakebo, f, indent=4):
        _json_dump(kakebo.get_buildin(), f, indent)
        

class TextFormatter(AbstractFormatter):
    def load(self, f):
        pass

    def dump(self, f):
        pass


def json_formatter_test():
    formatter = JsonFormatter()
    with open('kakebo.json') as jf:
        kakebo = formatter.load(jf)
    
    with open('kakebo_test.json', 'w') as jf:
        formatter.dump(kakebo, jf)

json_formatter_test()
