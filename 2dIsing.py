import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import sys

L=int(sys.argv[1])
T=float(sys.argv[2])
NMCS=int(sys.argv[3])

H = 2 *(np.random.random_integers(L*L,size=(L,L))%2-0.5*np.ones(L*L).reshape(L,L))

nnp= lambda s:s+1-L if s+1 >= L else s+1
nnm= lambda s:s-1+L if s-1 < 0 else s-1

def dE(h,x,y):
    xp,yp,xm,ym = nnp(x),nnp(y),nnm(x),nnm(y)
    return 2.0/T*h[x,y]*(h[x,yp]+h[x,ym]+h[xp,y]+h[xm,y])

def mcs(h):
    for n in range(L*L):
        x,y = np.random.randint(L,size=(2))
        de = dE(h,x,y)
        if de < 0:
            h[x,y]=-h[x,y]

        elif np.random.rand() < np.exp(-de):
            h[x,y]=-h[x,y]

    return h

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

images=ax.imshow(H,cmap=plt.cm.gray, interpolation='gaussian')

def update_progress(amtDone):
    print "\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(amtDone * 50), amtDone * 100),
    sys.stdout.flush()

def updatefig(n):
    images.set_array(mcs(H))
    update_progress(float(n)/NMCS)
    return images,

an = anim.FuncAnimation(fig,updatefig,np.arange(0,NMCS),interval=20,blit=True)
an.save("ising_L_"+str(L)+"_T_"+str(T)+".mp4",fps=30,extra_args=['-vcodec','libx264'])

plt.show()
