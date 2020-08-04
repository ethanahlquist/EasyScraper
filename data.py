#!/usr/bin/env python3

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np  # Math Module
import pandas as pd
import math
from celluloid import Camera


def draw_plot_from_csv(csvfile):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    df = pd.read_csv('data.csv')
    print(df)
    x = df['diam']
    y = df['length']
    z = df['br']
    c = df['gauss']
    #x = np.random.standard_normal(100)
    #y = np.random.standard_normal(100)
    #z = np.random.standard_normal(100)
    #c = np.random.standard_normal(100)
    ax.set_xlabel('diameter')
    ax.set_ylabel('length')
    ax.set_zlabel('br')
    ax.set_title('Magnetic Field Calculations')

    img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
    fig.colorbar(img)
    plt.show()


def MyAnimation():

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')

    df = pd.read_csv('data.csv')
    print(df)
    x = df['diam']
    y = df['length']
    #z = df['br1']
    z = df['gauss']
    #x = np.random.standard_normal(100)
    #y = np.random.standard_normal(100)
    #z = np.random.standard_normal(100)
    #c = np.random.standard_normal(100)
    ax.set_xlabel('diameter')
    ax.set_ylabel('length')
    ax.set_zlabel('br')
    ax.set_title('Magnetic Field Calculations')

    #img = ax.scatter(x, y, z, c='blue', cmap=plt.hot())
    camera = Camera(fig)
    for i in df['br']:
        ax.set_title('Magnetic Field Calculations: {} br '.format(int(i)))
        # ax.plot_scatter(df['length'], df['diameter'], df['br'], c='r', linewidth=0.2) #cmap=plt.get_cmap('viridis'), linewidth=0.2)
        img = ax.scatter(x, y, z, c='blue', cmap=plt.hot())
        camera.snap()

    animation = camera.animate()
    animation.save('celluloid_minimal.gif', writer='imagemagick')

    # Make the plot
    #    fig = plt.figure()
    #    ax = fig.gca(projection='3d')
    #    #ax.plot_trisurf(df['length'], df['diameter'], df['br'], cmap=plt.get_cmap('viridis'), linewidth=0.2)
    #    ax.plot_scatter(df['length'], df['diameter'], df['br'], cmap=plt.get_cmap('viridis'), linewidth=0.2)

    #    ax.view_init(30,angle)

    #    filename='images/magnatism'+str(angle)+'.png'
    #    plt.savefig(filename, dpi=96)
    #    plt.gca()
    #
    #
    #fig = plt.figure()
    #camera = Camera(fig)
    # for i in range(10):
    #    plt.plot([i] * 10)
    #    camera.snap()
    #
    #animation = camera.animate()
    #animation.save('celluloid_minimal.gif', writer = 'imagemagick')
