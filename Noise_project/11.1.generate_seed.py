import os
import sys
from igraph import *
import math
import numpy as np
import collections
import bisect
import random

def main():
	random.seed()
	size = int(sys.argv[1])
	g = Graph()
	g = read('./'+str(size)+'_network.graphml')
	g.to_undirected()
	
	comm_dict = dict()
	node_perm_dict = dict()
	for v in g.vs:
		node = int(str(v).split(',')[1])
		perm = v['perm']
		if node not in node_perm_dict:
			node_perm_dict[node] = perm
		else:
			node_perm_dict[node] += perm
		if int(v['comm']) not in comm_dict:
			comm_dict[int(v['comm'])] = [node]
		else :
			comm_dict[int(v['comm'])].append(node)

	sims = 1
	#v = g.community_infomap()
	os.system('rm -r ./'+str(size)+'_seeds')
	os.system('mkdir ./'+str(size)+'_seeds')
	for sim in range(sims):
		out1 = open('./'+str(size)+'_seeds/'+str(size)+'_size_random_'+str(sim)+'.txt', 'w')
		out2 = open('./'+str(size)+'_seeds/'+str(size)+'_size_degree_'+str(sim)+'.txt', 'w')
		out3 = open('./'+str(size)+'_seeds/'+str(size)+'_size_perm_'+str(sim)+'.txt', 'w')
		out4 = open('./'+str(size)+'_seeds/'+str(size)+'_size_pagerank_'+str(sim)+'.txt', 'w')
		out5 = open('./'+str(size)+'_seeds/'+str(size)+'_size_close_'+str(sim)+'.txt', 'w')
		for comm, nodes in comm_dict.iteritems():
			ls = nodes[:]
			random.shuffle(ls)
			out1.write(str(ls[0])+"\n")
			m_p   = -2.0
			m_d   = -2.0
			m_pg  = -2.0
			m_cl  = 0
			m_p_i = -1
			m_d_i = -1
			m_pg_i = -1
			m_cl_i = -1
						

			for l in ls:
				if node_perm_dict[l] > m_p:
					m_p = node_perm_dict[l]
					m_p_i = l
				if g.degree(l) > m_d:
					m_d = g.degree(l)
					m_d_i = l
				if g.pagerank(l) > m_pg:
					m_pg = g.pagerank(l)
					m_pg_i = l
				if g.closeness(l) > m_cl:
					m_cl = g.closeness(l)
					m_cl_i = l
			out2.write(str(m_d_i)+"\n")
			out3.write(str(m_p_i)+"\n")
			out4.write(str(m_pg_i)+"\n")
			out5.write(str(m_cl_i)+"\n")
		out1.close()
		out2.close()
		out3.close()
		out4.close()
		out5.close()

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return 1
    return 0


if  __name__ =='__main__':
	main()

