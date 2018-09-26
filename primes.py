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

def gen_eratosthenes():
    index = 0
    count = 0
    list_primes = [2]
    next_prime = 3
    yield list_primes[index]
    while (True):
        for i in range(2, next_prime):
            if (next_prime %I != 0):
                count += 1
            else:
                break
            if (count == next_prime - 2):
                index += 1
                list_primes.append(next_prime)
                yield list_primes[index]
        count = 0
        next_prime += 1
