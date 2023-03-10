#Zigzag edged graphene quantum dot
import pybinding as pb
import numpy as np
from pybinding.repository import graphene
import matplotlib.pyplot as plt
import cycler

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
eigenvalues = solver.calc_eigenvalues(map_probability_at = [0, -0.8])
eigenvalues.plot_heatmap(show_indices = True)
pb.pltutils.colorbar()
plt.title('Associated energy levels at site (0, -0.8)')

plot2 = plt.figure(2)
probability_map = solver.calc_probability(9)
probability_map.plot()

plot3 = plt.figure(3)
eigen_2 = solver.calc_eigenvalues(map_probability_at = [0.2, -0.8])
eigen_2.plot_heatmap(show_indices = True)
pb.pltutils.colorbar()
plt.title('Associated energy levels at site (0.2, -0.8)')

plt.show()