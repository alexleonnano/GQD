#Triangular graphene sheet

from IPython import get_ipython
ipython=get_ipython()
import pybinding as pb
import numpy as np
from pybinding.repository import graphene
import matplotlib.pyplot as plt
from math import pi
import pandas as pd

plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'figure.dpi': 100})


#triangle = pb.regular_polygon(num_sides=3, radius=1, angle=pi/6)
#triangle = pb.regular_polygon(num_sides=3, radius=5, angle=pi/6)
#triangle = pb.regular_polygon(num_sides=3, radius=10, angle=pi/6)
#triangle = pb.regular_polygon(num_sides=3, radius=15, angle=pi/6)
#triangle = pb.regular_polygon(num_sides=3, radius=20, angle=pi/6)
triangle = pb.regular_polygon(num_sides=3, radius=1, angle=0)
#triangle = pb.regular_polygon(num_sides=3, radius=5, angle=0)
#triangle = pb.regular_polygon(num_sides=3, radius=10, angle=0)
#triangle = pb.regular_polygon(num_sides=3, radius=15, angle=0)
#triangle = pb.regular_polygon(num_sides=3, radius=20, angle=0)

model = pb.Model(
    graphene.monolayer(),
    triangle
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


plt.show()

data = solver.eigenvalues
a = data.tolist()
#with open('eigenZ.txt', 'w') as fp:
#    fp.write('\n'.join(str(a) for a in a))
#    print('Data text file done')

degen_states = solver.find_degenerate_states(data, 1e-05)
print(degen_states)

ds = pb.results.Series
dsa = str(ds)
print(dsa)