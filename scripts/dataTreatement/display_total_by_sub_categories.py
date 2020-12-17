import csv
import matplotlib.pyplot as plt
import utility

def read(path) :

    with open(path) as csv_file :
        spamread = csv.reader(csv_file)

        title = utility.formatTitle(path) + ' by sub categories'
        drugs_category = utility.formatTitle(path) + ' Drugs & Chemicals ' + 'by sub categories'
        degree_rotation = 90
        subplot_left = 0.2
        subplot_right = 0.3

        axeX = []
        axeY = []
        axeXDrugs = []
        axeYDrugs = []
        is_first_row = False

        for row in spamread:
            if row == [] or is_first_row == False :
                is_first_row = True
                continue
            
            col_attribute = round(float(row[2]),2)
            if row[0] not in drugs_category: 
                axeX.append(row[0])
                axeY.append(col_attribute)
            else:
                axeXDrugs.append(row[1])
                axeYDrugs.append(col_attribute)

        # All sub categories without Drugs
        fig, ax = plt.subplots()
        plt.subplots_adjust(left = subplot_left, bottom = subplot_right)
        plt.bar(axeX, axeY)
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.xticks(rotation = degree_rotation) 
        plt.title(title)

        # Drugs sub categories
        fig, ax = plt.subplots()
        plt.subplots_adjust(left = subplot_left, bottom = subplot_right)
        plt.bar(axeXDrugs, axeYDrugs)
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.xticks(rotation = degree_rotation) 
        plt.title(drugs_category)

def main() :
    total_path = 'data/totalSubCategories/'
    files = utility.getFile(total_path)
    
    for processed_file in files:
        csv_file = total_path + processed_file 
        read(csv_file)
    plt.show()

main()      