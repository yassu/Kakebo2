#!/usr/bin/env python3
from math import sqrt


class AbstractStatics:

    def obtain_result(self, kakebo):
        pass

    def rep_result(self, kakebo):
        return self.__repr__() + ': ' + str(self.obtain_result(kakebo))


class Average(AbstractStatics):

    def obtain_result(self, kakebo):
        return kakebo.obtain_income() / len(kakebo)

    def __repr__(self):
        return 'average'


class Variance(AbstractStatics):

    def obtain_result(self, kakebo):
        incomes = kakebo.obtain_incomes()
        average = sum(incomes) / len(incomes)
        var = sum([(x - average) * (x - average)
                   for x in incomes]) / len(incomes)
        return sqrt(var)

    def __repr__(self):
        return 'variance'


class LineRegression(AbstractStatics):

    def obtain_result(self, kakebo):
        from scipy import polyfit
        incomes = kakebo.obtain_incomes()
        xs = list(range(len(incomes)))
        loop, sedgement = map(int, polyfit(xs, incomes, 1).tolist())

        out = '{a} * x'.format(a=loop)

        if sedgement == 0:
            return out

        sgn = ''
        if sedgement > 0:
            sgn = '+'
        elif sedgement < 0:
            sgn = '-'
            sedgement *= (-1)

        out += ' {sgn} {b}'.format(sgn=sgn, b=sedgement)
        return out

    def __repr__(self):
        return 'line regression'

ALL_STATS = (
    Average(),
    Variance(),
    LineRegression()
)
