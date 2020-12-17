import pandas as pd
import re
import sys
import cleaner_utility
import os

path_to_datas = 'data/'
path_to_dataSet = path_to_datas + 'dataSet/'

list_duplicates_drop = 'list_duplicates_drop.csv'

path_list_duplicates_drop = path_to_dataSet + list_duplicates_drop

product_list = pd.read_csv(path_list_duplicates_drop, delimiter=";")


total_sub_category_directory = 'data/totalSubCategories/'
total_category_directory = 'data/totalCategories/'


def createDirectory(dirName):
    try:
        os.mkdir(dirName)
        print("Directory ", dirName,  " Created ")
    except FileExistsError:
        print("Directory ", dirName,  " already exists")


def get_totals_by_categories(clean_product_list):

    index = clean_product_list[clean_product_list['USD'] > 1000000].index
    top_categories = clean_product_list.drop(index)
    total_usd_by_categories = top_categories.groupby(
        by="product_category").agg({'USD': 'sum'}).reset_index()
    total_sells_by_categories = top_categories[['product_category', 'USD']].groupby(
        by="product_category").count().reset_index()
    total_sells_by_categories.to_csv(
        path_to_datas+'/totalCategories/total_sells_by_categories.csv', index=False)
    total_usd_by_categories.to_csv(
        path_to_datas+'/totalCategories/total_usd_by_categories.csv', index=False)
    return (total_usd_by_categories, total_sells_by_categories)


def get_totals_by_subcategories(clean_product_list):
    index = clean_product_list[clean_product_list['USD'] > 1000000].index
    clean_product_list = clean_product_list.drop(index)
    all_sub_categories = clean_product_list.dropna()

    all_sub_categories['product_id_subcategory'] = all_sub_categories['product_id_subcategory'].apply(
        cleaner_utility.clean_sub_cat_column)

    total_usd_by_sub_categories = all_sub_categories.groupby(
        by=['product_category', 'product_id_subcategory']).agg({'USD': 'sum'}).reset_index()
    total_sells_by_sub_categories = all_sub_categories[['product_category', 'product_id_subcategory', 'USD']].groupby(
        by=['product_category', 'product_id_subcategory']).count().reset_index()

    total_sells_by_sub_categories = total_sells_by_sub_categories.sort_values(
        by="product_category", ascending=True, inplace=False)
    total_usd_by_sub_categories = total_usd_by_sub_categories.sort_values(
        by="product_category", ascending=True, inplace=False)

    total_sells_by_sub_categories.to_csv(
        path_to_datas+'/totalSubCategories/total_sells_by_sub_categories.csv', index=False)
    total_usd_by_sub_categories.to_csv(
        path_to_datas+'/totalSubCategories/total_usd_by_sub_categories.csv', index=False)

    return (total_usd_by_sub_categories, total_sells_by_sub_categories)


def get_trending_product(dataframe, category):
    if category == "":
        category = "Drugs & Chemicals"
    cat = dataframe.groupby(by="product_category")
    index = cat.get_group(category)['USD'].idxmax(axis="columns")
    trending_product = dataframe.loc[index]
    print(trending_product)
    return trending_product


def main(sells=True, category=""):
    createDirectory(total_sub_category_directory)
    createDirectory(total_category_directory)
    column_to_drop = ['product_url', 'product_views_sales_quantityleft',
                      'vendor', 'vendor_url', 'BTC', 'file', 'crawling_date']
    clean_product_list = product_list.drop(columns=column_to_drop, axis=1)
    clean_product_list['product_category'] = clean_product_list['product_category'].apply(
        cleaner_utility.clean_category_column)
    clean_product_list['USD'] = clean_product_list['USD'].apply(
        cleaner_utility.clean_usd_column)
    clean_product_list['USD'] = clean_product_list['USD'].astype(float)

    (total_usd_by_category, total_sells_by_category) = get_totals_by_categories(
        clean_product_list)
    (total_usd_by_sub_categories,
     total_sells_by_sub_categories) = get_totals_by_subcategories(clean_product_list)

    if(sells):
        get_trending_product(total_sells_by_sub_categories, category)
    else:
        get_trending_product(total_usd_by_sub_categories, category)


if __name__ == '__main__':
    if len(sys.argv) > 3:
        raise ValueError('Wrong arguments')

    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        main(sys.argv[1] == "Sells")
    else:
        main(sys.argv[1] == "Sells", sys.argv[2])
