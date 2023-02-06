#Hexagonal graphene sheet

import pybinding as pb
import numpy as np
from pybinding.repository import graphene
import matplotlib.pyplot as plt
from math import pi
import cycler
import time

start = time.time()
plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'figure.dpi': 100})
plt.rcParams['axes.prop_cycle'] = cycler.cycler(color='k')

#hexagon = pb.regular_polygon(num_sides=6, radius=1, angle=pi/6)
#hexagon = pb.regular_polygon(num_sides=6, radius=5, angle=pi/6)
#hexagon = pb.regular_polygon(num_sides=6, radius=10, angle=pi/6)
#hexagon = pb.regular_polygon(num_sides=6, radius=15, angle=pi/6)
#hexagon = pb.regular_polygon(num_sides=6, radius=20, angle=pi/6)
hexagon = pb.regular_polygon(num_sides=6, radius=1, angle=0)
#hexagon = pb.regular_polygon(num_sides=6, radius=5, angle=0)
#hexagon = pb.regular_polygon(num_sides=6, radius=10, angle=0)
#hexagon = pb.regular_polygon(num_sides=6, radius=15, angle=0)
#hexagon = pb.regular_polygon(num_sides=6, radius=20, angle=0)


model = pb.Model(
    graphene.monolayer(),
    hexagon
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

end = time.time()
print(end - start, ' seconds')

plt.show()

data = solver.eigenvalues
a = data.tolist()
with open('eigen.txt', 'w') as fp:
    fp.write('\n'.join(str(a) for a in a))
    print('Done')