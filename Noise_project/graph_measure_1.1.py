from igraph import *
import snap
import os
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



def modularity(g):
   ai = 0
   ei = 0
   m2 = len(g.es) 
   tg = labelling(g)
   for v in tg:
	g1 = g.induced_subgraph(v,implementation="create_from_scratch")
	degs1 = g1.ecount()*1.0
        ei = degs1 + ei
            

   for v in tg:
        degs = g.degree(v)
	g1 = g.induced_subgraph(v,implementation="create_from_scratch")
	degs = sum(degs)/2.0
	degs1 = g1.ecount()*1.0
	degs = degs - degs1
	ai = ai + degs

   ai = ai / m2
   ei = ei / m2
   #print ai
   #print ei     
   #print " Modularity %f " % (ai - ei)
   return (ei,ai)



def inverse_distance(g):
	mat = g.shortest_paths()
	tot = 0.0
	n   = len(mat)
	for i in range(n):
		for j in range(n):
			if i != j:
				tot += (1.0 / mat[i][j])
	return ( tot / (n * (n-1.0)) )


if __name__ == '__main__':
			out = open("uniform_footballs.txt","w")
			g = read("football_p.graphml").as_undirected()
			d_o = inverse_distance(g)
			n = [2.0,4.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0]
                        samp = 5
			for i in n:
				clustering  = []
				effective_dia     = []
				diameter		  = []
				inter_edges		  = []
				intra_edges		  = []
				inter_intra		  = []
				disassort_degree  = []
				disassort_cluster = []
				edge_connectivity = []
				avg_path_length   = []
				robustness        = []
				for j in range(samp):
					g1 = read("uniform_noise_railway_perm"+str(i)+str(j)+".graphml").as_undirected()
					clustering.append(g1.transitivity_undirected())
                                        g1.write("temp.txt",format="edgelist")
                                        G = snap.LoadEdgeList(snap.PUNGraph,"temp.txt",0,1)
                                        effective_dia.append(snap.GetAnfEffDiam(G))
                                        os.system("rm temp.txt")
					diameter.append(g1.diameter())
					disassort_degree.append(g1.assortativity_degree())
					avg_path_length.append(g1.average_path_length())
					original_d = inverse_distance(g1)
					robustness.append( original_d / d_o)
					edge_connectivity.append(g1.edge_connectivity())
					inter_eg = 0.0
 					intra_eg = 0.0
					ii =  modularity(g1)
					inter_edges.append(1.0 * ii[1])
					intra_edges.append(1.0 * ii[0])
					inter_intra.append(1.0 * ii[1]/ii[0])
			
				out.write(str(i) + '\t' + str(np.mean(clustering)) + '\t' + str(np.mean(effective_dia)) + '\t' + str(np.mean(diameter)) + '\t' + str(np.mean(inter_edges))+ '\t' + str(np.mean(intra_edges)) + '\t' + str(np.mean(inter_intra)) + '\t' + str(np.mean(disassort_degree)) + '\t' + str(np.mean(avg_path_length)) + '\t' + str(np.mean(robustness))   +'\n')			
			out.close()
		



							
