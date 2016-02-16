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
    # t_axis = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800]
    t_axis = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800]
    fnames = ['football', 'lfr_0.1', 'lfr_0.3', 'lfr_0.6', 'lfr_0.8']
    # fnames = ['lfr_0.8']
    for fname in fnames : 
        print 'fname :', fname
        original_g = read('../noise_data/'+str(fname)+'_network.txt')
        original_g.to_undirected()

        
        for t in t_axis:
            print '\nerror : ' , t, 
            sim = 10
            while sim > 0:
                sim -=1
                print sim, 
                noise = t / 1000.0
                g = original_g.copy()
                lc = g.closeness()
                m = max(lc)
                m_v = []
                for i in range(len(lc)):
                    if lc[i] == m:
                        m_v.append(i)
                start = m_v[random.randint(0,len(m_v)-1)]
                vseq  = g.vs
                crawl_edges =  (1.0 - noise) * len(g.es)
                visited = [False] * len(g.vs)
                visited[start] = True
                queue   = [start]
                c_vertices = [start]
                c_g_e = []
                ok = 1
                # print 'Added : ', start
                while len(queue) > 0 and ok == 1:
                    node = queue.pop(0)
                    neigbours = [int(str(x).split(',')[1]) for x in vseq[node].neighbors()]
                    random.shuffle(neigbours)
                    for n in neigbours:
                        e = (min(node, n), max(node,n))
                        if not visited[n]:
                            queue.append(n)
                            visited[n] = True
                            crawl_edges -= 1
                            c_g_e.append(e)
                            # print n, ": ", len(g.vs)
                            # print 'Added : ', n
                            c_vertices.append(n)
                        else :
                            if e not in c_g_e:
                                c_g_e.append(e)
                                crawl_edges -= 1
                        if crawl_edges < 0:
                            ok = 0
                            break

                c_g        = Graph()
                c_g.add_vertices(len(g.vs))
                c_g.add_edges(c_g_e)
                c_g.to_undirected()
                vt  = []
                for v in c_g.vs:
                    if v.degree() == 0:
                        vt.append(v)
                c_g.delete_vertices(vt)

                id_g = g.induced_subgraph(c_vertices)


                out = open("../noise_data/crawled_noise/noisy_network/noise_"+fname+"_"+str(t)+"_"+str(sim)+".txt", "w")
                # print "Crawled edges : ", len(c_g.es), "Crawled nodes : ", len(c_g.vs)
                for e in c_g.es:
                    out.write(str(e.tuple[0]) + "\t" + str(e.tuple[1]) + "\n")
                    out.write(str(e.tuple[1]) + "\t" + str(e.tuple[0]) + "\n")
                out.close()

                out = open("../noise_data/crawled_noise/noisy_network/induced_"+fname+"_"+str(t)+"_"+str(sim)+".txt", "w")
                # print "Induced edges : ", len(id_g.es), "Induced nodes : ", len(id_g.vs)
                for e in id_g.es:
                    out.write(str(e.tuple[0]) + "\t" + str(e.tuple[1]) + "\n")
                    out.write(str(e.tuple[1]) + "\t" + str(e.tuple[0]) + "\n")
                out.close()

    

if  __name__ =='__main__':main()