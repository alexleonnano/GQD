#Ciruclar graphene sheet

import pybinding as pb
import numpy as np
from pybinding.repository import graphene
import matplotlib.pyplot as plt
import cycler
import csv

plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'figure.dpi': 100})
plt.rcParams['axes.prop_cycle'] = cycler.cycler(color='k')

def circle(radius):
    def contains(x, y, z):
        return np.sqrt(x**2 + y**2) < radius
    return pb.FreeformShape(contains, width = [2*radius, 2*radius])

model = pb.Model(
    graphene.monolayer(),
   circle(radius = 1)
#    circle(radius = 5)
#    circle(radius = 10)
#    circle(radius = 15)
#    circle(radius = 20)
)

solver = pb.solver.arpack(model, k=20)

plot1 = plt.figure(1)

model.plot()

plot2 = plt.figure(2)
eigenvalues = solver.calc_eigenvalues()
eigenvalues.plot()

plot3 = plt.figure(3)
dos = solver.calc_dos(energies = np.linspace(-1, 1, 200), broadening = 0.05)
plt.rcParams['lines.linewidth'] = 5.0
dos.plot()

plot4 = plt.figure(4)
ldos_map = solver.calc_spatial_ldos(energy=0, broadening=0.05)
ldos_map.plot()
pb.pltutils.colorbar(label="LDOS")

plt.show()

data = solver.eigenvalues
a = data.tolist()
with open('sales.txt', 'w') as fp:
    fp.write('\n'.join(str(a) for a in a))
    print('Done')