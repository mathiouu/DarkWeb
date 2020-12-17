import csv
import matplotlib.pyplot as plt
import utility

def read(path) :
    with open(path) as csv_file :
        spamread = csv.reader(csv_file)

        title = utility.formatTitle(path) + ' by categories'
        degree_rotation = 90
        subplot_left = 0.2
        subplot_right = 0.3

        axeX = []
        axeY = []
        is_first_row = False

        for row in spamread:
            if row == [] or is_first_row == False :
                is_first_row = True
                continue

            col_attribute = round(float(row[1]),2)
            axeX.append(row[0])
            axeY.append(col_attribute)

        fig, ax = plt.subplots()
        plt.subplots_adjust(left = subplot_left, bottom = subplot_right)
        plt.bar(axeX, axeY)
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.xticks(rotation = degree_rotation)
        plt.title(title)  

def main() :
    total_path = 'data/totalCategories/'
    files = utility.getFile(total_path)
    
    for processed_file in files:
        csv_file = total_path + processed_file
        read(csv_file)
    plt.show()

main()      