import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

noise = ["uniform","censored","crawled"]
q = ["rail","football","lfr01","lfr03"]

data = q[3]

plt.figure(figsize=(150,35))
plt.subplots_adjust( wspace=0.25)


patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]


for z in range(1,4,1):

			m = np.loadtxt(noise[z-1]+"_"+data+"_robust.txt")
			r = np.loadtxt(noise[z-1]+"_"+data+"_metrics.txt")
			corels = []
			for i in range(1,4,1):
					metric = m[:,i]
					temp = []
					for j in range(1,8,1):
						measures = r[:,j]
						temp.append(st.pearsonr(metric,measures)[0])
					corels.append(temp)
			cor = np.array(corels)
			cor = cor.T
			np.savetxt('dump.out', cor, delimiter=' ',fmt='%1.3f')
			plt.rc('font',weight='bold')
			plt.rc('xtick',labelsize=10)
			plt.rc('ytick',labelsize=10)
			plt.rcParams['axes.linewidth'] = 0.5
			ax = plt.subplot(1,3,z)
			index = np.arange(7)
			bar_width = 0.15
			opacity = 0.4
 
			rects1 = plt.bar(index, cor[:,0], bar_width,
                 alpha=opacity,
                 color='gainsboro',edgecolor='black',
                 label='Algebraic Connectivity',hatch='/')
 
			rects2 = plt.bar(index + bar_width, cor[:,1], bar_width,
                 alpha=opacity,
                 color='lightblue',edgecolor='black',
                 label='Effective Ressistance',hatch='-')


			rects3 = plt.bar(index + 2*bar_width,cor[:,2], bar_width,alpha=opacity,color='pink',edgecolor='black',label='Inv Geodesic',hatch='//')



			plt.xlabel('Measures',fontsize=95,fontweight='bold')
			plt.ylabel('Correlation',fontsize=95,fontweight='bold')
			plt.title(data+" "+noise[z-1],fontsize=105,fontweight='bold')
			plt.xticks(index + 1.5*bar_width, ('perm', 'con', 'cut', 'mod','close','page','betw'),fontsize=10)
			if z==3:
					plt.rc('legend',fontsize=70)
					ax.legend(loc='lower right',bbox_to_anchor=(0.4,0.07),borderaxespad=0)
			ax.xaxis.set_tick_params(labelsize=100)
			ax.yaxis.set_tick_params(labelsize=100)
			plt.grid()

#plt.tight_layout(pad=10,w_pad=10.0,h_pad=15.0,)
plt.savefig(data+'robust'+'.eps',bbox_inches='tight')
#plt.show()
#plt.savefig(data+'robust'+'.eps')
