import os
import sys
from igraph import *
import math
import numpy as np
from collections import Counter
import time
import random

def main():
    random.seed()
    n = [0,1.0,2.0,4.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0]
    fnames = ['railway']
    for fname in fnames : 
        print 'fname :', fname
        original_g = read("railway_p.graphml") # name of the network
        original_g.to_undirected()

        
        for t in n:
            sim = 5
            while sim > 0:
                sim -=1
                print sim
                noise = t/100.0 
                g = original_g.copy()
                rem_edges = 1.0 * noise * len(g.es)
                print 'Removed :', rem_edges, 'edges from ', len(g.es)
                edge_list = []
                for e in g.es:
                    edge_list.append((e.source, e.target))
                random.shuffle(edge_list)
                it = 0
                while rem_edges >= 1 and it < len(edge_list):
                    e = edge_list[it]
                    # print edge_list[it]
                    g.delete_edges([e])
                    if g.is_connected():
                        rem_edges -= 1
                    else:
                        g.add_edges([e])
                    it +=1
                
                g.write_graphml("uniform_noise_railway"+str(t)+str(sim)+".graphml")

    

if  __name__ =='__main__':main()
