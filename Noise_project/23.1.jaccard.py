import os
import sys
from igraph import *
import math
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import scipy.stats

def labelling(g):
 new = {}
 for v in g.vs:
   new[v.index] = v["comm"]

 nw = {}
 for x in new:
  c = new[x]
  if c in nw:
   nw[c].append(x)
  else:
   nw[c] = []
   nw[c].append(x)

 return nw.values()


def reliability_measures(g , comm):
	clus = 0.0
	clos = 0.0
	page = 0.0
	k    = len(comm) * 1.0
	for i in range(len(comm)):
		g1    = g.subgraph(comm[i])
		# clus += np.var([x for x in g1.transitivity_local_undirected() if not math.isnan(x)])
		# # if math.isnan(clus):
		# # 	print g1.transitivity_local_undirected() 
		clos += np.var(g1.closeness())
		page += np.var(g1.pagerank())
	# print 'var : ', np.var(g.transitivity_local_undirected()) , 'k : ', k
	# clu  = ( k / (k-1) ) * (1 - (clus/ np.var(g.transitivity_local_undirected()))) 
	clo  = (1.0 * k / (k-1.0) ) * (1.0 - (1.0 * clos/ np.var(g.closeness()))) 
	pag  = (1.0 * k / (k-1.0) ) * (1.0 - (1.0 * page/ np.var(g.pagerank())))
	return (clo, pag)

def permanence(g, comt):
	total_nodes = 0.0
	total_permanence = 0.0
	comm = comt
	comm_dict = dict()
	for i in range(len(comm)):
		for j in range(len(comm[i])):
			comm_dict[comm[i][j]] = i

	perm_g = []
	for i in range(len(comm)):
		for j in range(len(comm[i])):
			# print comm[i][j]
			n  = g.neighbors(comm[i][j])
			dv = g.degree(comm[i][j])
			inv = []
			exv = []
			for v in n:
				if i == comm_dict[v]:
					inv.append(v)
				else:
					exv.append(comm_dict[v])
			iv = len(inv)
			cin = 0.0
			if iv >= 2:
				cin = (len(g.subgraph(inv).es) * 2.0) / ( iv * (iv-1.0) )

			perma = 0.0
			if iv < dv:
				ev = max(map(exv.count, exv))
				perma = ( (1.0 * iv / ev) * (1.0 / dv) ) - (1.0 - cin)
			else:
				perma = cin

			total_nodes +=1.0
			perm_g.append(perma)
		return perm_g

def conductance(g, cmt):

	comm = [[] for _ in range(max(cmt) + 1)]
	for i in range(len(cmt)):
		comm[cmt[i]].append(i)



	comm_dict = dict()
	for i in range(len(comm)):
		for j in range(len(comm[i])):
			comm_dict[comm[i][j]] = i

	conduct = []
	for i in range(len(comm)):
		ns = len(comm[i])
		if ns > 0:
			ms = len(g.subgraph(comm[i]).es)
			cs = sum(g.degree(comm[i])) - (2*ms)
			conduct.append((1.0* cs) / (2.0 * ms + cs))
		# print i, ns, ms, cs
	return np.mean(conduct)

def cut_ratio(g, cmt):
	comm = [[] for _ in range(max(cmt) + 1)]
	for i in range(len(cmt)):
		comm[cmt[i]].append(i)



	comm_dict = dict()
	for i in range(len(comm)):
		for j in range(len(comm[i])):
			comm_dict[comm[i][j]] = i

	cut = []
	n = len(g.vs)
	for i in range(len(comm)):
		ns = len(comm[i])
		if ns > 0:
			ms = len(g.subgraph(comm[i]).es)
			cs = sum(g.degree(comm[i])) - (2*ms)
			cut.append((1.0* cs) / (1.0 * ns * (n - ns)) )
		# print i, ns, ms, cs
	return np.mean(cut)

def jaccard(ai,bi):
	a = np.argsort(ai)
	b = np.argsort(bi)
	if len(a) != len(b):
		print  'ERROR ', len(a), len(b)
	if len(a) < 10:
		return len(set(a).intersection(set(b))) / float(len(set(a).union(set(b))))

	a = a[-30:]
	b = b[-30:]
	return len(set(a).intersection(set(b))) / float(len(set(a).union(set(b))))


def main():
	n = [0,1.0,2.0,4.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0] 
	fnames = ['football']
	g = Graph()
	for fname in fnames : 
		print 'fname :', fname
		comt = []
		out = open(fname+"_jaccard_uniform.txt", "w")
		out.write(str(  'permanence_truth'+ '\t' + 'closeness'+ '\t' + 'pagerank' + '\n'))
		perm_g = []
		close_g= []
		page_g = []
		samp = 5
		for t in n:
			print("here %f " % t)
			perma = []
			close  = []
			pagerank = []
			if t <= 0:
				print("In If")			
				g = read("football_p.graphml")
				g.to_undirected()
				comt = labelling(g)
				perm_g = permanence(g, comt)
				close_g= g.closeness()
				page_g = g.pagerank()	
				perm_n = permanence(g, comt)
				close_n= g.closeness()
				page_n = g.pagerank()
				perma.append(jaccard(perm_g, perm_n))
				close.append(jaccard(close_g, close_n))
				pagerank.append(jaccard(page_g, page_n))
			else:
				print("In Else")
				perm_n = []
				close_n = []
				page_n = []
	    			for j in range(samp):
						g = read("uniform_noise_railway_perm"+str(t)+str(j)+".graphml")
						g.to_undirected()
						comt = labelling(g)
						perm_n = permanence(g, comt)
						close_n= g.closeness()
						page_n = g.pagerank()			
						perma.append(jaccard(perm_g, perm_n))
						close.append(jaccard(close_g, close_n))
						pagerank.append(jaccard(page_g, page_n))
			out.write('\t'+str(np.mean(perma))+'\t'+str(np.mean(close))+'\t'+str(np.mean(pagerank))+'\n')
	out.close()
	

if  __name__ =='__main__':main()
