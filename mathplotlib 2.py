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
plt.subplot(211)
plt.plot([50,100,150,200], [1,2,3,4], "r--", linewidth=5)
plt.plot([50,100,150,200], [2,3,7,10], "b", linewidth=3)
plt.plot([50,100,150,200], [2,7,9,10], "g", linewidth=10)
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.axis([80, 180, 1, 10])

plt.subplot(212)
plt.plot([50,100,150,200], [1,2,3,15], "r--", linewidth=5)
plt.plot([50,100,150,200], [2,3,7,10], "b", linewidth=3)
plt.plot([50,100,150,200], [2,7,9,10], "g", linewidth=10)
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.axis([80, 180, 1, 10])

plt.show()
def main():
    pass

if __name__ == '__main__':
    main()
