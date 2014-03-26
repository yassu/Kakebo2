#!/usr/bin/env python3 
from   json     import load     as _json_load
from   copy     import deepcopy as _deepcopy
from   datetime import datetime as _datetime
from   math     import sqrt
from   scipy	import stats	as _stats
import scipy					as _scipy
import numpy					as np

class Content:
	def __init__(self, content_name , income):
		self._content_name = content_name
		self._income = income
	
	def get_content_name(self):
		return self._content_name

	def get_income(self):
		return self._income

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

	def obtain_average_of_income(self):
		return self.obtain_income()/len(self._dailies)

	def obtain_variance_of_income(self):
		incomes = self.obtain_incomes()
		return sqrt(np.var(incomes))

	def obtain_correlation_coefficient(self):
		"""
		return correlation coefficient of incomes and straight data.
		"""
		incomes = self.obtain_incomes()
		l = len(incomes)
		return np.corrcoef(incomes, range(l))[0][1]

	def obtain_line_regression(self):
		"""
		return list of (loop, sedgement)
		"""
		incomes = self.obtain_incomes()
		l = len(incomes)
		return _scipy.stats.linregress(incomes, range(l))[:2]

	def __getitem__(self, ind):
		return self._dailies[ind]
	
	def __repr__(self):
		return '\n'.join(map(str, self._dailies))

def parse_date(s_date):
	year, month, day = map(int, s_date.split('/'))
	return _datetime(year, month, day)

def parse(jf):
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

def income_test():
	jf = open('kakebo.json')
	kakebo = parse(jf)
	print(kakebo.obtain_income())

def obtain_average_of_income_test():
	jf = open('kakebo.json')
	kakebo = parse(jf)
	print(kakebo.obtain_average_of_income())

def obtain_variance_of_income_test():
	jf = open('kakebo.json')
	kakebo = parse(jf)
	print(kakebo.obtain_variance_of_income())

def obtain_correlation_test():
	jf = open('kakebo.json')
	kakebo = parse(jf)
	print(kakebo.obtain_correlation_coefficient())
	
def main(filename):
	jf = open(filename, 'r')	
	kakebo = parse(jf)
	print(kakebo)

obtain_correlation_test()

