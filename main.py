#!/usr/bin/env python3

import re # regular expressions
import csv
import sys
import time
import random
from celluloid import Camera
#import imageio
import numpy as np # Math Module
import pandas as pd # 
from scraper import SeleniumDriver
from scraper import ScrapElement
from selenium.webdriver.common.by import By

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

URL = 'https://www.intemag.com/magnet-pull-calculations-disc-magnet-with-steel-plate'
driver = SeleniumDriver()
driver.get(URL)

'''
I don't know how to do this better, but this is just so we can give all the
funtions access to the webdriver, without adding another param.
'''
# Decorator? First Class Func?
def Element(by, token): return ScrapElement(by, token, driver)

def randomLoop(diam, length, br, gauss, filewriter):

    for x in range(0, 600):
        diam.value = random.uniform(2, 8)
        length.value = random.uniform(2, 8)
        br.value = random.uniform(5000, 10000)
                
        diam.change_data()
        length.change_data()
        br.change_data().submit()
        # This last .subimt() is hitting <Enter> in the text field

        out_val = float(gauss.get_data().text)

        filewriter.writerow([
            diam.value,
            length.value,
            br.value,
            out_val
        ])

        print(out_val)
        time.sleep(2.5)

def myLoop(diam, length, br, gauss, filewriter):

    for d in range(4, 7):
        diam.value = d + random.uniform(-.7, .7)

        for l in range(4, 7):
            length.value = l + random.uniform(-.7, .7)

            for b in range(8500, 9500, 200):
                br.value = b + random.uniform(-110, 110)
                
                diam.change_data()
                length.change_data()
                br.change_data().submit()
                # This last .subimt() is hitting <Enter> in the text field

                out_val = float(gauss.get_data().text)

                filewriter.writerow([
                    diam.value,
                    length.value,
                    br.value,
                    out_val
                ])

                print(out_val)


def draw_plot_from_csv(csvfile):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    df = pd.read_csv('data.csv')
    print(df)
    x = df['diameter1']
    y = df['length1']
    z = df['br1']
    c = df['gauss1']
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

def openCSV(csvfile):
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
    writer.writerow(['diameter1', 'length1', 'br1', 'gauss1'])
    return writer

def appendCSV(csvfile):
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
    return writer

#def makePlotAnimation():
#    df = pd.read_csv('data.csv')
#    print(df)
#    x = df['diameter1']
#    y = df['length1']
#    t = df['br1']
#    z = df['gauss1']
#
#
#    def plot_for_offset(df, time):
#        # Data for plotting
#        t = np.arange(0.0, 100, 1)
#        s = t**power
#
#        fig, ax = plt.subplots(figsize=(10,5))
#        
#        ax.set_xlabel('diameter')
#        ax.set_ylabel('length')
#        ax.set_zlabel('gauss')
#        ax.set_title('Magnetic Field Calculations')
#        
#        ax.scatter(t, s)
#        ax.grid()
#
#        # IMPORTANT ANIMATION CODE HERE
#        # Used to keep the limits constant
#        ax.set_ylim(0, y_max)
#
#        # Used to return the plot as an image rray
#        fig.canvas.draw()       # draw the canvas, cache the renderer
#        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
#        image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
#
#        return image
#
#    kwargs_write = {'fps':1.0, 'quantizer':'nq'}
#    imageio.mimsave('./powers.gif', [plot_for_offset(i/4, 100) for i in range(10)], fps=1)
#    
#    
#    pass

#def MyAnimation():
#
#    data = pd.read_csv('data.csv')
#    
#    # Transform it to a long format
#    df=data.unstack().reset_index()
#    df.columns=["diameter","length","br"]
#
#    # And transform the old column name in something numeric
#    df['diameter']=pd.Categorical(df['diameter'])
#    df['diameter']=df['diameter'].cat.codes
#
#    # We are going to do 20 plots, for 20 different angles
#    for angle in range(70,210,2):
#
#    # Make the plot
#        fig = plt.figure()
#        ax = fig.gca(projection='3d')
#        ax.plot_trisurf(df['length'], df['diameter'], df['br'], cmap=plt.get_cmap('viridis'), linewidth=0.2)
#
#        ax.view_init(30,angle)
#
#        filename='images/magnatism'+str(angle)+'.png'
#        plt.savefig(filename, dpi=96)
#        plt.gca()
    
def MyAnimation():


    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')

    df = pd.read_csv('data.csv')
    print(df)
    x = df['diameter1']
    y = df['length1']
    #z = df['br1']
    z = df['gauss1']
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
    for i in df['br1']:
        ax.set_title('Magnetic Field Calculations: {} br '.format(int(i)))
        #ax.plot_scatter(df['length'], df['diameter'], df['br'], c='r', linewidth=0.2) #cmap=plt.get_cmap('viridis'), linewidth=0.2)
        img = ax.scatter(x, y, z, c='blue', cmap=plt.hot())
        camera.snap()
    
    animation = camera.animate()
    animation.save('celluloid_minimal.gif', writer = 'imagemagick')


    ## Make the plot
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
    #for i in range(10):
    #    plt.plot([i] * 10)
    #    camera.snap()
    #    
    #animation = camera.animate()
    #animation.save('celluloid_minimal.gif', writer = 'imagemagick')

    
def main(argv):

    # These are declarations of the different html-elements you want to deal with!
    diam = Element(By.NAME, 'diameter1')
    length = Element(By.NAME, 'length1')
    br = Element(By.NAME, 'br1')
    gauss = Element(
        By.XPATH, '//*[@id="bodyContent"]/div[3]/div/form/div/table/tbody/tr[6]/td[2]/p')

    # Open csv file for writing
    mode='a+'
    csvfile =  open('data.csv', mode) 

    # This just allows you to switch from appending to making a new file quickly
    # It just checks the write-mode
    if re.match(r'w.', mode):
        writer = openCSV(csvfile)
    elif re.match(r'a.', mode):
        writer = appendCSV(csvfile)
    
    #randomLoop(diam, length, br, gauss, writer)

    # Close opened file
    csvfile.close()

    # No longer need browser open
    driver.quit()

    # Not needed since matlab is better
    draw_plot_from_csv('data_csv')
    MyAnimation()




if __name__ == "__main__":
    main(sys.argv[1:])
