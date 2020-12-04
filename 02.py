#!/usr/bin/env python3

import sys, os, re
import unittest
from lib.common import *

filename = "inputs/2020_12_02_input.txt"
class day02:
    def __init__(self):
        self.data = []
        # Data will have the structure:
        # [
        #   {min, max, char, pass, result}
        #   {min, max, char, pass, result}
        #   ...
        # ]
    
    def load_data(self, data):
        my_data = []
        for item in data:
            # the format of the line::
            # XX-YY C: ZZZZZZ...
            splits = re.split(r"[- :]+", item)
            if len(splits)<4:
                print("Found a line that doesn't follow the pattern::\n%s" % item)
                exit(1)
                
            my_data.append( {'min':int(splits[0]), 'max':int(splits[1]),
                             'char':splits[2], 'pass':splits[3]} )
            
        self.data = my_data
        
    def solve_passwords(self):
        for i in range(0, len(self.data)):
            pass_to_test = self.data[i]
            
            l_min = pass_to_test["min"]
            l_max = pass_to_test["max"]
            l_char = pass_to_test["char"]
            l_pass = pass_to_test["pass"]
            
            chars = l_pass.count(l_char)
            if chars > l_max:
                res = "high"
            elif chars < l_min:
                res = "low"
            else:
                res = "pass"
                
            self.data[i]["result"] = res
            
    def count_valid(self):
        count = 0
        for item in self.data:
            if item["result"]=="pass":
                count += 1
                
        return count


class day02part1(day02):
    def solve(self, args):
        pass


class day02part2(day02):
    def solve_toboggan(self):
        for i in range(0, len(self.data)):
            pass_to_test = self.data[i]
            l_pass = pass_to_test['pass']
            l_char = pass_to_test['char']
            indexA = pass_to_test['min']-1
            indexB = pass_to_test['max']-1
            
            res = ''
            if self.xor( l_char, l_pass[indexA], l_pass[indexB] ):
                res = 'good'
            else:
                res = 'fail'
            
            self.data[i]['tob'] = res
            
    def xor(self, test_arg, arg_a, arg_b):
        # sort-of emulating an xor operator, but using both of the character checks
        
        a = test_arg == arg_a
        b = test_arg == arg_b
        x = a ^ b
        return x

    def count_toboggan(self):
        count = 0
        for item in self.data:
            if item['tob']=='good':
                count += 1
                
        return count
    
    def fancy_format(self):
        from colors import red,green,blue
        
        for item in self.data:
            c1 = item['min']-1
            c2 = item['max']-1
            cs = item['pass']
            cc = item['char']
            output = ''
            
            if item['tob']=='good':
                output += green('good') + "  "
            else:
                output += red('FAIL') + "  "
                
            output += str(c1).zfill(2)+"-"+str(c2).zfill(2)+"|"+cc+"| "
            
            if c1==0:
                cleft=''
            else:
                cleft = cs[0:c1]
                
            if cs[c1]==cc:
                cX = blue(cs[c1])
            else:
                cX = red(cs[c1])
                
            if c1+1 == c2-1:
                cmid = cs[c1+1]
            else:
                cmid = cs[ c1 + 1 : c2 - 1 ]
                
            if cs[c2]==cc:
                cY = blue(cs[c2])
            else:
                cY = red(cs[c2])
            
            if c2==len(cs):
                cright = ''
            else:
                cright = cs[c2+1:]
                
            output += cleft + cX + cmid + cY + cright
            
            print(output)
                
            
        
        

class examples(unittest.TestCase):
    def test_examples_part1(self):
        test_data1 = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        day2 = day02part1()
        day2.load_data(test_data1)
        day2.solve_passwords()
        test1_valid =  day2.count_valid()
        
        self.assertEqual(test1_valid, 2, "Unable to calculate the correct number of valid passwords.")
        print("All Passed part 1")
        # self.assetTrue()

    def test_examples_part2(self):
        test_data1 = ['1-3 a: cbade', '1-3 b: cdefg', '2-9 c: ccccccccc', '2-9 c: 1c345678c']
        day2 = day02part2()
        day2.load_data(test_data1)
        day2.solve_toboggan()
        #print(day2.data)
        test2_valid =  day2.count_toboggan()

        self.assertEqual(test2_valid, 1, "Unable to calculate the correct number of valid passwords.")
        day2.fancy_format()


class solutions(unittest.TestCase):
    def test_part1(self):
        day2 = day02part1()

    def test_part2(self):
        day2 = day02part2()


def my_file(name):
    data = list(filemap(lambda x: x, name))
    return data

if __name__ == '__main__':
    mydata = my_file(filename)
    day2 = day02part1()
    day2.load_data(mydata)
    day2.solve_passwords()
    valids =  day2.count_valid()
    print("Number of valid passwords: %d" % valids)
    
    print("\n----\n")
    
    day22 = day02part2()
    day22.load_data(mydata)
    day22.solve_toboggan()
    valid2 =  day22.count_toboggan()
    #day22.fancy_format()
    print("Number of toboggan passwords: %d" % valid2)

