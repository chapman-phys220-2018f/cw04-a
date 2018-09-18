#!/usr/bin/env python3

# Royal Cuevas and Abigail Wheaton 
#2285562 and 2299246 
#cueva114@mail.chapman.edu and wheaton@chapman.edu 
#PHYS220 Fall 2018
# CW 04

import math

def eratosthenes(n):
    integers=[]
    primes=[]
    j=1
    for i in range(2,n):
        integers.append(i)
    while integers[0]<=math.sqrt(n):
        primes.append(integers[0])
        for x in integers:
            if (integers[j] % integers[0]) == 0:
                del integers[j]
            j=j+1
    for x in integers:
            primes.append(x)
    return primes
