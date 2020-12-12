import csv
import re

pathCsv = 'data/'

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