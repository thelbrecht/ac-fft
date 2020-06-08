'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

class MultidimensionalGraphs:
    def shape_1(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Make data.
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X**2 + Y**2)
        Z = np.sin(R)

        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                            linewidth=0, antialiased=False)

        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()

    def shape_2(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Make data.
        # Create the mesh in polar coordinates and compute corresponding Z.
        r = np.linspace(0, 1.25, 50)
        p = np.linspace(0, 2*np.pi, 50)
        R, P = np.meshgrid(r, p)
        Z = ((R**2 - 1)**2)

        # Express the mesh in the cartesian system.
        X, Y = R*np.cos(P), R*np.sin(P)

        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                            linewidth=0, antialiased=False)

        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()
        

