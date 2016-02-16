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
    # t_axis = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500]
    t_axis = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800]
    # fnames = ['football', 'lfr_0.1', 'lfr_0.3', 'lfr_0.6']
    fnames = ['lfr_0.8']
    for fname in fnames : 
        print 'fname :', fname
        original_g = read('../noise_data/'+str(fname)+'_network.txt')
        original_g.to_undirected()

        
        for t in t_axis:
            sim = 10
            while sim > 0:
                sim -=1
                print sim
                noise = t / 1000.0
                g = original_g.copy()
                rem_edges = 1.0 * noise * len(g.es)
                print 'Removed :', rem_edges, 'edges from ', len(g.es)
                while rem_edges >= 1.0:
                    vertex_degree = []
                    vseq = g.vs
                    for i in range(len(vseq)):
                        vertex_degree.append( ( vseq[i] ,  vseq[i].degree() ) )
                    vertex_degree.sort(key=lambda x: x[1], reverse = True)
                    # print vertex_degree
                    if vertex_degree[0][1] <= 1:
                        print 'CANNOT DO CENSORING ANYMORE WITHOUT DISCONNECTING NETWORK'
                        break
                    else:
                        ok = 1
                        while ok == 1:
                            for vertex in vertex_degree:
                                neigbours = vertex[0].neighbors()
                                random.shuffle(neigbours)
                                for n in neigbours:
                                    # print "neighbours : ", vertex[0] , ": ", n
                                    e = (vertex[0] , n)
                                    g.delete_edges([e])
                                    if g.is_connected():
                                        ok = 0
                                        break
                                    g.add_edges([e])
                                if ok == 0:
                                    break
                    rem_edges -=1
                out = open("../noise_data/censored_noise/noisy_network/"+fname+"_"+str(t)+"_"+str(sim)+".txt", "w")
                print "Left edges : ", len(g.es)
                for e in g.es:
                    out.write(str(e.tuple[0]) + "\t" + str(e.tuple[1]) + "\n")
                    out.write(str(e.tuple[1]) + "\t" + str(e.tuple[0]) + "\n")
                out.close()

    

if  __name__ =='__main__':main()