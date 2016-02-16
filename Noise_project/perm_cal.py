from igraph import *
import numpy as np


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




def permanence(g1):
        print "Inside RAK"
	comm = g1.community_infomap()
	#comm = labelling(g1)
        print "outside RAk"
	print 'there'
	total_nodes = 0.0
	total_permanence = 0.0

	comm_dict = dict()
	for i in range(len(comm)):
		for j in range(len(comm[i])):
			comm_dict[comm[i][j]] = i


	for i in range(len(comm)):
		for j in range(len(comm[i])):
			n  = g1.neighbors(comm[i][j])
			dv = g1.degree(comm[i][j])
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
				cin = (len(g1.subgraph(inv).es) * 2.0) / ( iv * (iv-1.0) )

			perma = 0.0
			if iv < dv:
				ev = max(map(exv.count, exv))
				perma = ( (1.0 * iv / ev) * (1.0 / dv) ) - (1.0 - cin)
			else:
				perma = cin

			total_nodes +=1.0
			g1.vs[comm[i][j]]['perm'] = perma     # to make permanence (0 to 2)

def elais(n):
     sample = 5
     for i in range(sample):
        g1 = read("crawled_football_"+str(n)+'_'+ str(i)+".graphml")
        print "Calculating Permanence %.2f %.2f" %(n,i) 
        permanence(g1)
        g1.write_graphml("crawled_football_perm"+str(n)+str(i)+".graphml")
        p = [ v["perm"] for v in g1.vs]
        print "Perm %f " % np.mean(p)
def main():
   
   #npc = [1.0,2.0,4.0,8.0,16.0,32.0,64.0,70.0,74.0,78.0,82.0,86.0,90.0,92.0,96.0,98.0,99.0,100.0]
   #npc = [1.0,2.0,4.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0]
   npc = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800]
   for n in npc:
     elais(n)
   '''
   g = read("railway_comm.graphml")
   permanence(g)
   p = [ v["perm"] for v in g.vs]
   print "Perm %f " % np.mean(p)
   '''
if __name__=='__main__':
   main()

