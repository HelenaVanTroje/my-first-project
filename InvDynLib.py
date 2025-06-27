# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 15:55:17 2025

@author: hfaber
"""

import numpy as np

# Maak een parabool met op de x-as nt tijdstippen van 0 t/m te en op de y-as
# hoeken van phi0 t/m phiEnd. De hoeksnelheid op t=0 is 0
def trajectHoek(phi0, phiEnd, nt, te):
    t = np.linspace(0,te,nt)
    return ((phiEnd-phi0)/te**2)*t**2+phi0

# afgeleiden van trajectHoek:
def trajectHoeksnelheid(phi0, phiEnd, nt, te):
    t = np.linspace(0, te, nt)
    return (2*(phiEnd-phi0)/te**2)*t

# afgeleiden van trajectHoeksnelheid:
def trajectHoekversnelling(phi0, phiEnd, nt, te):
    return 2*(phiEnd-phi0)/te**2

# bereken gewrichtsmomenten in ideale situatie:
def InvDynTopDown(L,d,m,g,Fendx,Fendy,Mend,phi,phid,phidd,nt,te):
# L: segmentlengtes
# d: zwaartepuntafstanden
# m: segmentmassa's
# g: zwaartekrachtversnelling
# Fendx: horizontale kracht op uiteinde
# Fendy: verticale kracht op uiteinde
# Mend: moment op uiteinde
# phi: hoeken segmenten
# phid: hoeksnelheden segmenten
# phidd: hoekversnellingen segmenten
# nt: aantal tijdstippen
# te: laatste tijdstip
# aantal segmenten:    
    nSeg = len(L)
# versnelling gewrichtposities in x- en y-richting tov vorige gewricht,
# preallocatie:    
    xJLokdd = np.zeros(nSeg+1)
    yJLokdd = np.zeros(nSeg+1)
# versnelling gewrichtposities in x- en y-richting globaal,
# preallocatie:    
    xJdd = np.zeros(nSeg+1)
    yJdd = np.zeros(nSeg+1)
# versnelling deelzwaartepunten in x- en y-richting, preallocatie:    
    xzdd = np.zeros(nSeg)
    yzdd = np.zeros(nSeg)
# ga alle tijdstippen af:    
    for i in range(nt):
# ga alle segmenten af om versnellingen xJLokdd van gewrichten tov vorige
# gewricht in x-richting te bepalen:
        p1x = -phidd[:,i]*np.sin(phi[:,i])
        p2x = -phid[:,i]**2*np.cos(phi[:,i])
        part1x = p1x*L
        part2x = p2x*L
        xJLokdd[1:nSeg+1] = part1x+part2x
# versnellingen yJLokdd gewrichten tov voorgaande gewricht in y-richting:
        p1y = phidd[:,i]*np.cos(phi[:,i])
        p2y = -phid[:,i]**2*np.sin(phi[:,i])
        part1y = p1y*L
        part2y = p2y*L
        yJLokdd[1:nSeg+1] = part1y+part2y
# versnellingen xJdd gewrichten globaal in x-richting:
        xJdd = np.cumsum(xJLokdd)
# versnellingen yJdd gewrichten globaal in y-richting:
        yJdd = np.cumsum(yJLokdd)
# bepaal de versnellingen van de zwaartepunten, globaal, x-richting:
        part1xz = p1x*d
        part2xz = p2x*d
        xzdd = xJdd[0:nSeg]+part1xz+part2xz
# bepaal de versnellingen van de zwaartepunten, globaal y-richting:
        part1yz = p1y*d
        part2yz = p2y*d
        yzdd = yJdd[0:nSeg]+part1yz+part2yz
# traagheidskrachten in x-richting:        
        Fmx = m*xzdd
# traagheidskrachten in y-richting:        
        Fmy = m*yzdd
# zwaartekrachten:
        Fz = m*g        
# gewrichtskrachten in x-richting:
        FxJ = np.zeros(nSeg+1)
        FxJ[nSeg] = -Fendx[i]
        FxJ[0:nSeg] = np.flip(np.cumsum(np.flip(Fmx-Fendx[i])))
# gewrichtskrachten in x-richting:
        FyJ = np.flip(np.cumsum(np.flip(Fmy+m*g-Fendy[i])))
        
        
            
            