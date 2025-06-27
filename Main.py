# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:53:40 2025

@author: hfaber
"""

import numpy as np
import InvDynLib as id

# segmentlengtes:
L = np.array([0.3, 0.4, 0.45, 0.9])
# aantal segmenten:
nSeg = len(L)
# afstand gewricht-zwaartepunt segment relatief voet richting hoofd:
dRel = np.array([0.6, 0.6, 0.6, 0.5])
# afstand gewricht zwaartepunt segment absoluut:
d = L*dRel
# segmentmassa's:
m = np.array([2, 10, 16, 40])
# zwaartekrachtversnelling:
g = 9.81
# starthoeken:
phi0 = np.deg2rad([160, 45, 135, 50])
# eindhoeken:
phiEnd = np.deg2rad([100, 85, 95, 85])
# aantal tijdstippen:
nt = 20
# laatste tijdstip:
te = 1
# maak segmenthoeken, segment hoeksnelheden en segment hoekversnellingen aan
# voor alle tijdstippen:
phi = np.zeros((nSeg,nt))
phid = np.zeros((nSeg,nt))
phidd = np.zeros((nSeg,nt))
Fendx = np.ones(nt)
Fendy = np.zeros(nt)
Mend = np.zeros(nt)
for i in range(nSeg):
    phi[i,:] = id.trajectHoek(phi0[i],phiEnd[i],nt,te)
    phid[i,:] = id.trajectHoeksnelheid(phi0[i], phiEnd[i], nt, te)
    phidd[i,:] = id.trajectHoekversnelling([i], phiEnd[i], nt, te)
    
M = id.InvDynTopDown(L, d, m, g, Fendx, Fendy, Mend, phi, phid, phidd, nt, te)

    

