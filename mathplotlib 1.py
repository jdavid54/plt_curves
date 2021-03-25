#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        matplotlib
# Purpose:
#
# Author:      Jean
# http://apprendre-python.com/page-creer-graphiques-scientifiques-python-apprendre
# Created:     23/01/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('Label 1')
plt.show()
#graphe2
plt.title("Danger de la vitesse")
plt.plot([50,100,150,200], [1,2,3,4])
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.show()
#graphe3
plt.plot([50,100,150,200], [1,2,3,4])
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.axis([80, 180, 1, 10])
plt.show()
#graphe4 plusieurs courbes
plt.plot([50,100,150,200], [1,2,3,4])
plt.plot([50,100,150,200], [2,3,7,10])
plt.plot([50,100,150,200], [2,7,9,10])
plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
