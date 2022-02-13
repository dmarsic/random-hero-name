#!/usr/bin/env python

from hero_name.random_hero_name import random_name

if __name__ == '__main__':
    for i in range(10):
        print(i, random_name())

