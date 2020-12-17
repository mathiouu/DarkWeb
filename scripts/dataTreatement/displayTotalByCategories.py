import csv
import matplotlib.pyplot as plt
import numpy as np
import utility

def read(path) :
    with open(path) as csvfile :
        spamread = csv.reader(csvfile)

        title = utility.formatTitle(path) + ' by categories'
        degree_rotation = 90
        subplot_left = 0.2
        subplot_right = 0.3

        axeX = []
        axeY = []
        cpt = False

        for row in spamread:
            if row == [] or cpt == False :
                cpt = True
                continue

            usd = round(float(row[1]),2)
            axeX.append(row[0])
            axeY.append(usd)

        fig, ax = plt.subplots()
        plt.subplots_adjust(left = subplot_left, bottom = subplot_right)
        plt.bar(axeX, axeY)
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.xticks(rotation = degree_rotation)
        plt.title(title)  

def main() :
    total_path = 'data/totalCategories/'
    files = utility.getFile(total_path)
    
    for treatedFile in files:
        csvFile = total_path + treatedFile 
        read(csvFile)
    plt.show()

main()      