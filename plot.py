from matplotlib import pyplot as plt
import numpy as np
import imageio
import os

# Plot a graph of the current iteration
# Parameters are : swarm is the collection of the particles, function is the objective function that is optimised along with its parameters, iteration is the current iteration index


def plotGraphs(swarm, function, function_parameters, iteration):

    # For Rosenbrock works better with low values (e.g -2,2)
    # For Rastrigin, larger are better (e.g -100,100)
    rangex = [-100, 100]
    # For Rosenbrock works better with low values (e.g -1,3)
    # For Rastrigin, larger are better (e.g -100,100)
    rangey = [-100, 100]

    # Set up the graph for the function
    xlist = np.linspace(rangex[0], rangex[1], 100)
    ylist = np.linspace(rangey[0], rangey[1], 100)
    X, Y = np.meshgrid(xlist, ylist)

    Z = []

    # Calculate the results of the function
    for i in range(len(X)):
        Z.append(function([X[i], Y[i]], function_parameters))

    fig, ax = plt.subplots(1, 1)
    cp = ax.contour(X, Y, Z, 100)
    fig.colorbar(cp)
    ax.set_title(function.__name__)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Langtitude")
    ax.set_xlim([rangex[0], rangex[1]])
    ax.set_ylim([rangey[0], rangey[1]])

    # Add the particles on the graph
    for j in range(len(swarm)):
        plt.scatter(swarm[j].particle_pos[0],
                    swarm[j].particle_pos[1], marker='o', color='red')

    # Save the graph as an image
    filename = f'images/Epoch_{iteration}_.png'
    plt.savefig(filename, dpi=96)

    # Cleanup
    plt.close()

    # Return the path to the file
    return filename


def createGif(filenames):

    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    for filename in set(filenames):
        os.remove(filename)