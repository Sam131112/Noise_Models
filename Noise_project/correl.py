import numpy as np
net_attr = ['clustering' , 'eff dia' , 'dia' , 'inter/edges ', 'intra/edges' , 'inter/ intra' , 'assort degre' , 'edge connct' , 'avg path len' , 'robust']
out = open("uniform_lfr03_corr.txt","w")
f1 = open("lfr03_sensitivity.txt","r")
f2 = open("lfr03_measures.txt","r")
net = [[] for _ in range(10)]
mes = [[] for _ in range(5)]

clustering  = []
effective_dia     = []
diameter		  = []
inter_edges		  = []
intra_edges		  = []
inter_intra		  = []
disassort_degree  = []
edge_connectivity = []
avg_path_length   = []
robustness        = []
for f in f2:
	f = f.strip("\n\t\r")
	f = f.split("\t")
	for i in range(1,len(f)):
		net[i].append(float(f[i]))

for f in f1:
        f = f.strip("\n\t\r")
        f = f.split("\t")
	print f    
        for i in range(1,len(f)):
                mes[i].append(float(f[i]))

for c in net: 
 print c
 print("\n")

for c in mes:
 print c 
 print("\n")
 
print len(net)
print len(mes)
print('***********************************************')

net1 = []
mes1 = []

for v in mes:
 if len(v) != 0:
   mes1.append(v)

for v in net:
 if len(v) != 0:
   net1.append(v)

print("******************************************************************")

for v in net1:
   print v
print("*************************************************************************")
for v in mes1:
 print v


print("Start Corelations Calculation")


for i in net1:
  for j in mes1:
    out.write(str(np.corrcoef(i,j)[0,1])+'\t')
  out.write("\n")


out.close()
