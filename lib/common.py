from collections import defaultdict, deque, Counter
import math
from math import inf, gcd
import itertools
import re

def filemap(func, filename, sep='\n'):
    with open(filename) as f:
        return list(map(func, f.read().strip().split(sep)))
