
from __future__ import division


def pv(pmt, rate, nper, fv):
    """
    Compute the present value
    Inputs:
    * pmt as number
    * rate as decimal
    * nper as int
    * fv as number
    output:
    The present value of the stream of payments
    """

    pv = []
    for i in range(1, nper + 1):
        pv.append(pmt / (1 + rate) ** i)
    return sum(pv)


def npv(cfs, rate):
    """
    Compute the present value

    input:
     cfs as list of numbers, the 0 element in the investment amount
     rate as decimal
    """
    npv = []
    for i, cf in enumerate(cfs):
        npv.append(cf / (1 + rate) ** i)
    return sum(npv)


def irr(cfs):
    epsilon = 0.000001
    low = 0.0
    high = 100.0
    ans = (high + low) / 2.0
    while abs(npv(cfs, ans)) >= epsilon:
        if npv(cfs, ans) < 0:
            high = ans
        else:
            low = ans
        ans = (high + low) / 2.0
    return ans
