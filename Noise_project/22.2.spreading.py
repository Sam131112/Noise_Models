import os
import sys
from igraph import *
import math
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def write_graph(g , size):
	out = open('./' +str(size)+'_network.txt', 'w')
	for e in g.es:
		out.write(str(e.source) + "\t" + str(e.target) + "\n")
		out.write(str(e.target) + "\t" + str(e.source) + "\n")
	out.close()

def write_comt(comt, size):
	# if len(comt) != size:
	# 	print 'SIZE OF COMT AND SIZE NOT MATCHING', len(comt), size

	out = open('./'+str(size)+'_nodes_groups.txt', 'w')
	for i in range(len(comt)):
		out.write(str(i) + "\t" + str(comt[i]) + "\n")
	out.close()


def main():
	#t_axis = [1,2,4,8,16,32,64]
	n = [2.0,4.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0]
	fnames = ['lfr01']
	typ	   = 'crawled'
	g = Graph()
	for fname in fnames : 
		print 'fname :', fname
		#files = [ f for f in os.listdir("../Dataset/"+fname+"/"+typ) if os.path.isfile(os.path.join("../Dataset/"+fname+"/"+typ,f)) ]
		#files.sort()
		# comt = []
		# f_paper = open('../noise_data/ground_'+str(fname)+'_output.txt', 'r')
		# for line in f_paper:
		# 	comt.append(int(line.split()[1]))
		# f_paper.close()
		#tup = [[] for _ in range(7)]
		out = open(fname+"_"+typ+"_ground_spreading.txt", "w")
		#degree = []
		#perm   = []
		#rand   = []
		#close  = []
		#pagerank= []
		for t in n:
			tup = [[] for _ in range(6)]
			samp = 5
			print t
			degree = []
                	perm   = []
                	rand   = []
               		close  = []
        	        pagerank= []
			for j in range(samp):
					net = "/home/soumya/LFR0.1/crawled/crawl_noise_lfr_perm"+str(t)+str(j)+".graphml"
					print t,j
					g = read(net)
					g.to_undirected()
					size = g.vcount()
					g.write('./' +str(size)+'_network.txt',format = "edgelist")
					g.write('./' +str(size)+'_network.graphml',format="graphml")
					os.system('python 11.1.generate_seed.py '+str(size))
					output = os.popen('java SingleAttackPerm '+str(size)).read()
					print str(output)
					#print float(output.split()[0]), float(output.split()[1]), float(output.split()[2]), float(output.split()[3]), float(output.split()[4])
					degree.append(float(output.split()[0]))
					perm.append(float(output.split()[1]))
					rand.append(float(output.split()[2]))
					pagerank.append(float(output.split()[3]))
					close.append(float(output.split()[4]))
			tup[0].append(t)
			tup[1].append(np.mean(degree))
			tup[2].append(np.mean(perm))
			tup[3].append(np.mean(rand))
			tup[4].append(np.mean(pagerank))
			tup[5].append(np.mean(close))
			out.write(str(t) + '\t' + str(np.mean(degree)) + '\t' + str(np.mean(perm))+ '\t' + str(np.mean(rand)) + '\t' + str(np.mean(pagerank))+ '\t' + str(np.mean(close)) +'\n')			
		out.close()

		# plt.plot(tup[0], tup[1], tup[0], tup[2], tup[0], tup[3] , tup[0], tup[4], tup[0], tup[5] )
		# plt.legend(['degree' , 'permanence', 'random', 'pagerank' , 'close'])
		# plt.savefig('uniform_'+fname+'_spreading.png')
		# plt.clf()

		
	

if  __name__ =='__main__':main()
