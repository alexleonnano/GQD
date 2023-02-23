# Armchair edeged graphene quantum dot
import pybinding as pb
import numpy as np
from pybinding.repository import graphene
import matplotlib.pyplot as plt
import cycler

plt.rcParams.update({'font.size': 15})
plt.rcParams.update({'figure.dpi': 100})
plt.rcParams['axes.prop_cycle'] = cycler.cycler(color='k')

# hexagon = pb.regular_polygon(num_sides=6, radius=1, angle=0)
hexagon = pb.regular_polygon(num_sides=6, radius=5, angle=0)
# hexagon = pb.regular_polygon(num_sides=6, radius=10, angle=0)
# hexagon = pb.regular_polygon(num_sides=6, radius=15, angle=0)
# hexagon = pb.regular_polygon(num_sides=6, radius=20, angle=0)


model = pb.Model(
    graphene.monolayer(),
    hexagon
)

solver = pb.solver.arpack(model, k=20)

plot2 = plt.figure(1)
probability_map = solver.calc_probability(9)
probability_map.plot()

#Center of the GQD
plot1 = plt.figure(2)
eigenvalues = solver.calc_eigenvalues(map_probability_at = [0, 0])
eigenvalues.plot_heatmap(show_indices = True)
pb.pltutils.colorbar()
plt.title('Associated energy levels at site (0, 0)')

# Bottom edge of the GQD
plot3 = plt.figure(3)
eigen_2 = solver.calc_eigenvalues(map_probability_at = [0, -4.5])
eigen_2.plot_heatmap(show_indices = True)
pb.pltutils.colorbar()
plt.title('Associated energy levels at site (0, -4.5)')

# Left side of the GQD
plot3 = plt.figure(4)
eigen_2 = solver.calc_eigenvalues(map_probability_at = [4.3, 0])
eigen_2.plot_heatmap(show_indices = True)
pb.pltutils.colorbar()
plt.title('Associated energy levels at site (4.3, 0)')

plt.show()