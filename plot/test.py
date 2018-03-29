import itertools
import operator
import math
import multiprocessing
import numpy as np


def square(channel):
    global a
    channel.send(list(map(lambda x: x**2, a)))


class Person:
    def __init__(self, gender):
        self._gender = gender

    @property
    def gender(self):
        return self._gender


class Students(Person):
    def __init__(self, name, gender):
        super(Students, self).__init__(gender)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, m_name):
        if(m_name != 'wwc129'):
            print('you are not wwc129') 
        self._name = m_name 
    
    def __repr__(self):
        return "name : {}, gender: {}".format(self._name, self._gender)


p = Students('wwc', 'm')

p.name = 'mama'
multiprocessing.Value('f', 10)
print(p)
