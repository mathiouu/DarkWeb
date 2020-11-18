import csv

pathCsv = 'data/'

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

def main():
    file = 'list_duplicates_drop.csv'
    pathFile = pathCsv + file
    newFile = 'res_' + file
    pathRes = pathCsv + newFile
    removeProductUrl(pathFile, pathRes)

main()