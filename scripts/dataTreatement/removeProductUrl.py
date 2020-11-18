import csv
import re

pathCsv = 'data/'
'''
def removeProductUrl(pathFile, newFile) :

    with open(newFile, mode='w') as newCsv:
        writer = csv.writer(newCsv)

        with open(pathFile) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')

            isfirstRow = False
            for row in reader :
                
                if row == [] or isfirstRow == False:
                    isfirstRow = True
                    writer.writerow([key for key, value in row.items()])
                    continue
                
                newRow = []
                for key, value in row.items():
                    if key == 'product_url':
                        productUrlSplitted = value.split('/')
                        newProductUrl = productUrlSplitted[1]
                        # newProductUrl += ['/' + productUrlSplitted[val] for val in range(2, len(productUrlSplitted))]
                        for j in range(2, len(productUrlSplitted)):
                            newProductUrl += '/' + productUrlSplitted[j]
                        newRow.append(newProductUrl)
                        continue
                    newRow.append(value)
                writer.writerow(newRow)
'''



def remove_product(line):
    new_line = line
    new_line['product_url']= re.sub(r'^product\/',"",line['product_url'])
    return new_line



def clear_file(file, new_file):
    with open(new_file, mode='w', encoding='utf-8') as new_csv:
        writer = csv.writer(new_csv)
        with open(file, encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file,delimiter=';')
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(new_csv,fieldnames=fieldnames,delimiter=';')
            writer.writeheader()
            for line in reader:
                writer.writerow(remove_product(line))




def main():
    file = 'list_duplicates_drop.csv'
    pathFile = pathCsv + file
    newFile = 'res_' + file
    pathRes = pathCsv + newFile
    clear_file(pathFile, pathRes)

main()