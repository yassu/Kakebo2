#!/usr/bin/env python3

from sys import path
path.append('./')
import formatter
print(dir(formatter))


def income_test():
    jf = open('kakebo.json')
    formatter = JsonFormatter()
    kakebo = formatter.load(jf)
    print(kakebo.obtain_income())

if __name__ == '__main__':
    income_test()
