#!/usr/bin/env python3

import sys, os
import unittest
import numpy as np
from lib.common import *

filename = "inputs/2020_12_01_input.txt"
class day01:
    def __init__(self):
        pass

    def load_data(self,data):
        self.data = []
        self.a = 0
        self.b = 0
        self.c = 0
        array_max = max(data)
        print("Max value of loaded data:", array_max)
        self.check_array = np.zeros(array_max)

        for item in data:
            self.data.append( item )
            self.check_array[ item-1 ] = 1

        self.data.sort(reverse=True)


class day01part1(day01):
    def solve_for_add(self, target):
        # 'target' variable is how much we are looking for when adding the two together.
        for key in self.data:

            # 'key' is the A, so see if the B (together will add to the target) is in the array
            bee = target - key
            if self.check_array[bee-1] == 1:
                self.a = key
                self.b = bee
                return [key, bee]

        return [0,0]

    def solve_for_multiply(self):
        # Use the .a and .b, found in the previous retouine, and return their product

        return (self.a * self.b)


class day01part2(day01):
    def solve_for_add_three(self, target):
        # 'target' variable is how much we are looking for when adding the two together.
        for key in self.data:

            # 'key' is the A, so need to find B and C that all total to the target
            bee = target - key
            trimmed = self.check_array[ 0:bee ]
            
            for oppo in range(1, bee):
                site = bee - oppo
                if ((trimmed[oppo-1] == 1) and (trimmed[site-1] == 1)):
                    self.a = key
                    self.b = oppo
                    self.c = site
                    return [key, oppo, site]

        return [0,0,0]

    def solve_for_mult_three(self):
        # Use the .a and .b, found in the previous retouine, and return their product

        return (self.a * self.b * self.c)
    
    
class examples(unittest.TestCase):
    def test_examples_part1(self):
        day1 = day01part1()
        day1.load_data([1721,979,366,299,675,1456])

        twofactors = day1.solve_for_add(2020)
        self.assertNotEqual(
        twofactors[0], 0, msg='Failed to find an A/B match' )
        self.assertEqual( twofactors[0] + twofactors[1], 2020, msg='Found factors do not add to 2020' )

        mult_result = day1.solve_for_multiply()
        self.assertEqual(mult_result, 514579)
                      
        # self.assetTrue()

    def test_examples_part2(self):
        day1 = day01part2()
        day1.load_data([1721,979,366,299,675,1456])
        three_factors = day1.solve_for_add_three(2020)

        self.assertNotEqual(
        three_factors[0], 0, msg='Failed to find an A/B match' )

        self.assertEqual( sum(three_factors), 2020, msg='Found factors do not add to 2020' )
        print("A,B,C:",day1.a,day1.b,day1.c)

        mult_result = day1.solve_for_mult_three()
        self.assertEqual(mult_result, 241861950)

class solutions(unittest.TestCase):
    def test_part1(self):
        pass

    def test_part2(self):
        day1 = day01part2()


def my_file(name):
    data = list(map(int, filemap(lambda x: x, name)))
    return data


if __name__ == '__main__':
    p1 = day01part1()
    p1.load_data( my_file(filename) )
    factors = p1.solve_for_add(2020)
    print("Found the two factors: %d and %d" % (factors[0], factors[1]))
    p1solve = p1.solve_for_multiply()
    print("Part1 answer: %d" % p1solve)
    
    print("\n---\n")
    
    p2 = day01part2()
    p2.load_data( my_file(filename) )
    factors = p2.solve_for_add_three(2020)
    print("Found the three factors: %d, %d, %d" % (factors[0], factors[1], factors[2]))
    p2solve = p2.solve_for_mult_three()
    print("Part2 answer: %d" % p2solve)
    


