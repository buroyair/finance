
from __future__ import division
import pylab



def pv(pmt, rate, nper, fv):
    pv = []
    for i in range(1, nper + 1):
        pv.append(pmt / (1 + rate) ** i)
    return sum(pv)


def npv(cfs, rate):
    npv = []
    for i, cf in enumerate(cfs):
        npv.append(cf / (1 + rate) ** i)
    return sum(npv)


def irr(cfs):
    epsilon = 0.0001
    numguess = 0
    low = 0.0
    high = 100.0
    ans = (high + low) / 2.0
    while abs(npv(cfs, ans)) >= epsilon:
        #print 'numguess = ', numguess, 'low = ', low, 'high = ', high, 'ans = ', ans
        numguess += 1
        if npv(cfs, ans) < 0:
            high = ans
        else:
            low = ans
        ans = (high + low) / 2.0
    return ans


cfs = [-100000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000,
       10000, 10000, 10000,10000]

print irr(cfs)
