#!/usr/bin/python

# @Authors:
# Yosbi Antonio Alves Saenz (yosbito@gmail.com)

import random
from random import randint
import math
import sys


def rabinMiller(n):
    s = n - 1
    t = 0
    while s and 1 == 0:
        s = s / 2
        t += 1
    k = 0
    while k < 128:
        a = random.randrange(2, n - 1)
        v = pow(a, s, n)  # (num,exp,mod)
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % n
        k += 2
    return True


def isPrime(n):
    # testing only with rabinMiller
    return rabinMiller(n)


def getPrime(l):
    n = random.getrandbits(l)
    if (n % 2 == 0):
        n = n + 1
    while (not (isPrime(n))):
        n = n + 2
    return n


##  1 < e < phi(n) and gcd(e, phi(n)) = 1
def gete(phiDeN):
    e = 0
    if (phiDeN < 100000):
        e = randint(2, phiDeN // 2)
    else:
        e = randint(2, 100000)
    while True:
        if gcd(e, phiDeN) == 1:
            break
        else:
            e += 1
    return e


# Greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# using extended euclidean algorithm
# d = e^(-1) (mod phi(n))
def getd(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


# Extended greatest common divisor (for extended euclidean algorithm)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def genRSAkey(L):
    l = (L // 2)

    p = getPrime(l)
    if debug:
        print("p generated:")
        print(p)

    q = getPrime(l)
    if debug:
        print("q generated:")
        print(q)

    n = p * q
    if debug:
        print("n generated")
        print(n)

    phiDeN = (p - 1) * (q - 1)
    if debug:
        print("phi of n")
        print(phiDeN)

    e = gete(phiDeN)
    if debug:
        print("e generated:")
        print(e)

    d = d = getd(e, phiDeN)
    if debug:
        print("d generated:")
        print(d)

    return (n, p, q, e, d)

    # test
    # m = 32

    # c = (m**e) % n
    # print "el criptograma:"
    # print c

    # md = (c**d) % n
    # print "desencriptado:"
    # print md


# We can have the size of L either by args or by prompting the user
L = 0
debug = True;
if (len(sys.argv) == 2):
    L = int(sys.argv[1])
else:
    L = int(raw_input("Input the size of l "))

tuplo = genRSAkey(L)

print("result:")
print(tuplo)
