import csv
import os

path_to_datas_sub_categories = 'data/totalSubCategories/'

total_sells_csv = 'total_sells_by_sub_categories.csv'
total_usd_csv = 'total_usd_by_sub_categories.csv'

path_total_sells = path_to_datas_sub_categories + total_sells_csv
path_total_usd = path_to_datas_sub_categories + total_usd_csv

dirName = 'data/averagePrice/'

def createDirectory():
    try :
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError :
        print("Directory " , dirName ,  " already exists")

def get_quality_normal_way():

    with open(path_total_sells) as csv_sells:
        spamread_sells = csv.reader(csv_sells)

        with open(path_total_usd) as csv_usd:
            spamread_usd = csv.reader(csv_usd)

            new_csv = dirName + 'average_price.csv'
            with open(new_csv, mode='w') as new_csv:

                fieldnames = [
                'product_category',
                'product_id_category', 'count', 'usd', 'average_price'
                ]
                write = csv.writer(new_csv)
                write.writerow(fieldnames)

                cpt = False 
                cpt1 = False
                for row_sells in spamread_sells:
                    row = []
                    if row_sells == [] or cpt == False :
                        cpt = True
                        continue
                    for row_usd in spamread_usd:
                        if row_usd == [] or cpt1 == False :
                            cpt1 = True
                            continue

                        product_cat = row_sells[0]
                        product_id_subcat = row_sells[1]
                        
                        product_usd = float(row_usd[2])
                        product_count = float(row_sells[2])

                        product_average_price = product_usd/product_count

                        row.append(product_cat)
                        row.append(product_id_subcat)
                        row.append(product_usd)
                        row.append(product_count)
                        row.append(product_average_price)
                        break
                    write.writerow(row)
               
def main() :
    createDirectory()
    try :
        get_quality_normal_way()
    except Exception as e :
        print(e)

main()