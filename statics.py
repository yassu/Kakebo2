#!/usr/bin/env python3 
from math import sqrt

class AbstractStatics:
    def obtain_result(self, kakebo):
        pass

    def rep_result(self, kakebo):
        return self.__repr__() + ': ' + str(self.obtain_result(kakebo))

class Average(AbstractStatics):
    def obtain_result(self, kakebo):
        return kakebo.obtain_income()/ len(kakebo)

    def __repr__(self):
        return 'average'

class Variance(AbstractStatics):
    def obtain_result(self, kakebo):
        incomes = kakebo.obtain_incomes()
        average = sum(incomes) / len(incomes)
        var  = sum([(x - average)*(x - average) for x in incomes]) / len(incomes)
        return sqrt(var)

    def __repr__(self):
        return 'variance'

class LineRegression(AbstractStatics):
    def obtain_result(self, kakebo):
        incomes = kakebo.obtain_incomes()
        l = len(incomes)
        xs = incomes
        bar_xs = sum(xs)/len(xs)
        ys = range(l)
        bar_ys = sum(ys)/len(ys)
        loop = sum([(xs[i] - bar_xs)*(ys[i] - bar_ys)  for i in range(l)]) /    \
                    sum([(x-bar_xs)*(x-bar_xs) for x in xs])
        sedgement = bar_ys - loop * bar_xs
        return '{a}*x + {b}'.format(a=loop, b=sedgement)

    def __repr__(self):
        return 'line regression'

ALL_STATS = (
        Average(),
        Variance(),
        LineRegression()
    )
