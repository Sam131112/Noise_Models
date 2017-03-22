#Corelation for All Measures 
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

#m = np.loadtxt("football_measures.txt")
#r = np.loadtxt("uniform_football_metrics.txt")

#m = np.loadtxt("lfr01_measures.txt")
#r = np.loadtxt("uniform_lfr01_metrics.txt")

#m = np.loadtxt("lfr03_measures.txt")
#r = np.loadtxt("uniform_lfr03_metrics.txt")

m = np.loadtxt("railway_measures.txt")
r = np.loadtxt("uniform_rail_metrics.txt")


corels = []

for i in range(1,8,1):
	metric = r[:,i]
	temp = []
	for j in range(1,9,1):
		measures = m[:,j]
		temp.append(st.pearsonr(metric,measures)[0])
	corels.append(temp)


cor = np.array(corels)
np.savetxt('rail_uniform.out', cor, delimiter=' ',fmt='%1.3f')


plt.rc('font',weight='bold')
plt.rc('xtick',labelsize=35)
plt.rc('ytick',labelsize=35)
plt.rc('legend',fontsize=25)
plt.rcParams['axes.linewidth'] = 0.5
fig, ax = plt.subplots(figsize=(20,10))
index = np.arange(8)
bar_width = 0.09
opacity = 0.8
 
rects1 = plt.bar(index, cor[0,:], bar_width,
                 alpha=opacity,
                 color='r',
                 label='Perm',hatch='/')
 
rects2 = plt.bar(index + bar_width, cor[1,:], bar_width,
                 alpha=opacity,
                 color='rosybrown',
                 label='Con',hatch='*')


rects3 = plt.bar(index + 2*bar_width,cor[2,:], bar_width,alpha=opacity,color='b',label='Cut',hatch='\\')
rects4 = plt.bar(index + 3*bar_width,cor[3,:], bar_width,alpha=opacity,color='c',label='Mod',hatch='+')
rects5 = plt.bar(index + 4*bar_width,cor[4,:], bar_width,alpha=opacity,color='purple',label='Close',hatch='X')
rects6 = plt.bar(index + 5*bar_width,cor[5,:], bar_width,alpha=opacity,color='orange',label='Page',hatch='o')
rects7 = plt.bar(index + 6*bar_width,cor[6,:], bar_width,alpha=opacity,color='peru',label='Bet',hatch='.')



plt.xlabel('Measures',fontsize=50,fontweight='bold')
plt.ylabel('Correlation',fontsize=50,fontweight='bold')
plt.title('Railway',fontsize=50,fontweight='bold')
plt.xticks(index + 3.5*bar_width, ('clustering', 'eff_dia', 'dia', 'inter_e','intra_e','inter_intra','diss_deg','avg_path_len'),fontsize=15,rotation=45)

ax.legend(loc='lower right',bbox_to_anchor=(1,0.7))
ax.xaxis.set_tick_params(labelsize=35)
ax.yaxis.set_tick_params(labelsize=35)
plt.grid()
plt.savefig('rail_'+'.eps',bbox_inches='tight')
#plt.tight_layout()
#plt.show()








