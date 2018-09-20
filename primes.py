#!/usr/bin/env python3

#Royal Cuevas and Abigail Wheaton 
#2285562 and 2299246 
#cueva114@mail.chapman.edu and wheaton@chapman.edu 
#PHYS220 Fall 2018
#CW 04

import math


def eratosthenes(n):
    primes = []
    for x in range(2, n+1):
        if all(x % i != 0 for i in range(2, x)):
            primes.append(x)
    return primes
