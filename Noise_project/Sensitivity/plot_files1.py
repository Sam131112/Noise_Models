import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(200,55))

plt.subplots_adjust( wspace=0.3)


#f = np.loadtxt("fu.txt")
#f = np.loadtxt("l1u.txt")
f = np.loadtxt("l3u.txt")
#f = np.loadtxt("ru.txt")

x = f[:,0]
p = f[:,1]
m = f[:,2]
con = f[:,3]
cut = f[:,4]
cl = f[:,5]
pg = f[:,6]
bt = f[:,7]


plt.rc('font',weight='bold')
plt.rc('xtick',labelsize=150)
plt.rc('ytick',labelsize=150)
plt.rcParams['axes.linewidth'] = 0.5
ax = plt.subplot(1,3,1)
plt.ylim([-0.1,0.75])
plt.plot(x,p,c='r',linewidth=50,marker='o',ms=70,label="perm")
plt.plot(x,m,c='c',linewidth=50,marker='D',ms=70,label="mod")
plt.plot(x,con,c='m',linewidth=50,marker='*',ms=70,label="con")
plt.plot(x,cut,c='y',linewidth=50,marker='d',ms=70,label="cut")
plt.plot(x,cl,c='g',linewidth=50,marker='v',ms=70,label="close")
plt.plot(x,pg,c='k',linewidth=50,marker='^',ms=70,label="page")
plt.plot(x,bt,c='b',linewidth=50,marker='>',ms=70,label="betw")
plt.xlabel("Uniform Noise",fontsize=200,weight='bold')
plt.ylabel("Metrics",fontsize=200,weight='bold')


#f = np.loadtxt("fc.txt")
#f = np.loadtxt("l1c.txt")
f = np.loadtxt("l3c.txt")
#f = np.loadtxt("rc.txt")

x = f[:,0]
p = f[:,1]
m = f[:,2]
con = f[:,3]
cut = f[:,4]
cl = f[:,5]
pg = f[:,6]
bt = f[:,7]


plt.rc('font',weight='bold')
plt.rc('xtick',labelsize=150)
plt.rc('ytick',labelsize=150)
plt.rcParams['axes.linewidth'] = 0.5
plt.subplot(1,3,2)
plt.ylim([-0.1,0.75])
plt.plot(x,p,c='r',linewidth=50,marker='o',ms=70,label="perm")
plt.plot(x,m,c='c',linewidth=50,marker='D',ms=70,label="mod")
plt.plot(x,con,c='m',linewidth=50,marker='*',ms=70,label="con")
plt.plot(x,cut,c='y',linewidth=50,marker='d',ms=70,label="cut")
plt.plot(x,cl,c='g',linewidth=50,marker='v',ms=70,label="close")
plt.plot(x,pg,c='k',linewidth=50,marker='^',ms=70,label="page")
plt.plot(x,bt,c='b',linewidth=50,marker='>',ms=70,label="betw")
plt.xlabel("Censored Noise",fontsize=200,weight='bold')
plt.ylabel("Metrics",fontsize=200,weight='bold')


#f = np.loadtxt("fcw.txt")
#f = np.loadtxt("l1cw.txt")
f = np.loadtxt("l3cw.txt")
#f = np.loadtxt("rcw.txt")

x = f[:,0]
p = f[:,1]
m = f[:,2]
con = f[:,3]
cut = f[:,4]
cl = f[:,5]
pg = f[:,6]
bt = f[:,7]


plt.rc('font',weight='bold')
plt.rc('xtick',labelsize=150)
plt.rc('ytick',labelsize=150)
plt.rc('legend',fontsize=150) # using a named size
plt.rcParams['axes.linewidth'] = 0.5
ax = plt.subplot(1,3,3)
plt.ylim([-0.1,0.75])
plt.plot(x,p,c='r',linewidth=50,marker='o',ms=70,label="perm")
plt.plot(x,m,c='c',linewidth=50,marker='D',ms=70,label="mod")
plt.plot(x,con,c='m',linewidth=50,marker='*',ms=70,label="con")
plt.plot(x,cut,c='y',linewidth=50,marker='d',ms=70,label="cut")
plt.plot(x,cl,c='g',linewidth=50,marker='v',ms=70,label="close")
plt.plot(x,pg,c='k',linewidth=50,marker='^',ms=70,label="page")
plt.plot(x,bt,c='b',linewidth=50,marker='>',ms=70,label="betw")
plt.xlabel("Crawled Noise",fontsize=200,weight='bold')
plt.ylabel("Metrics",fontsize=200,weight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig('lfr03.eps',bbox_inches='tight')







