import numpy as np
from qutip import *
from pylab import *

N = 15
taus = np.linspace(0,10.0,200)
a = destroy(N)
H = 2 * np.pi * a.dag() * a

# collapse operator
G1 = 0.75
n_th = 2.00  # bath temperature in terms of excitation number
c_ops = [np.sqrt(G1 * (1 + n_th)) * a, np.sqrt(G1 * n_th) * a.dag()]

# start with a coherent state
rho0 = coherent_dm(N, 2.0)

# first calculate the occupation number as a function of time
n = mesolve(H, rho0, taus, c_ops, [a.dag() * a]).expect[0]

# calculate the correlation function G1 and normalize with n to obtain g1
G1 = correlation_2op_2t(H, rho0, None, taus, c_ops, a.dag(), a)
g1 = G1 / np.sqrt(n[0] * n)

plot(taus, g1, 'b')
plot(taus, n, 'r')
title('Decay of a coherent state to an incoherent (thermal) state')
xlabel(r'$\tau$')
legend((r'First-order coherence function $g^{(1)}(\tau)$', 
        r'occupation number $n(\tau)$'))
show()
