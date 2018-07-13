#-*-coding: UTF-8 -*-
import random
import time






def licznosci_count(L):
    licz= {}
    for e in L:
        licz[e]=L.count(e)
    return licz





def licznosci_bezcount(L):
    licz= {}
    for e in L:
        licz[e]=0
    for e in L:
        licz[e]+=1
    return licz


def test():
    L=[]
    for i in  range(20000):
        L.append(random.randint(0,1000))
    start_t=time.time()
    sl=licznosci_count(L)
    end_t=time.time()
    time_=end_t-start_t

    start_t=time.time()
    sl=licznosci_bezcount(L)
    end_t=time.time()
    time_bez=end_t-start_t

    print time_
    print time_bez
