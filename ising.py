import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

SIZE = 200
STEPS = 10**6

def bc(i):
    if i+1 >= SIZE:
        return 0
    elif i-1 < 0:
        return SIZE-1
    else:
        return i

def energy(system, N, M):
    return -1 * system[N,M] * (system[bc(N-1),M] + system[bc(N+1),M] + system[N,bc(M-1)] + system[N,bc(M+1)])

def build_system():
    system = np.random.random_integers(0,1,(SIZE,SIZE))
    system[system==0] =- 1

    return system

def main(T):
    system = build_system()

    for step,x in enumerate(range(STEPS)):
        M = np.random.randint(0,SIZE)
        N = np.random.randint(0,SIZE)

        E = -2. * energy(system, N, M)

        if E <= 0.:
            system[N,M] *= -1
        elif np.exp(-1./T*E) > np.random.rand():
            system[N,M] *= -1

def run():
    print '='*70
    print '\tMonte Carlo for Ising Model'
    print '='*70

    print "Choose temperature for run (0.1-100)"
    T = float(raw_input())
    main(T)

run()
