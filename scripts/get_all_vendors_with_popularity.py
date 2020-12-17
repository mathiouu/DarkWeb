import pandas as pd
import re

path_to_datas = "C:/Users/sebas/cours/Master2/Analyse-Reseau/projetDarkWeb/DarkWeb/data"


famous_sellers = pd.read_csv(path_to_datas+'/famousSellers.csv')

list_duplicates = pd.read_csv(
    path_to_datas+'/list_duplicates_drop.csv', delimiter=";")

seller_duplicates = pd.read_csv(
    path_to_datas+'/seller_duplicates_drop.csv', delimiter=";")
sellers = pd.read_csv(path_to_datas+'/sellers.csv')


def clean_sales_column(text):
    clean = re.match('\\((.*)\\)', str(text))
    return clean.groups()[0]


def clean_vendor_trst_lvl_columns(text):
    clean = re.match('(.*)(\\d)', str(text))
    return clean.groups()[1]


def clean_subcat_column(text):
    clean = str(text).replace(' ', '')
    clean = re.match('(Item#.\\d+-)(.+)(-.*)', str(clean))
    clean = re.match('(.*)\\/(.*)', clean.groups()[1])
    return clean.groups()[0]


def clean_cat_column(text):
    clean = text.strip()
    clean = re.match('(\\W*)(.+)(\\s*)', str(clean))
    return clean.groups()[1]


def clean_usd_column(text):
    return text.replace(',', '')


def set_new_popularity(row, sales, trust, total):
    current_vendor = row.vendor
    sales_index = sales.index.get_loc(
        sales[sales.vendor == current_vendor].iloc[0].name)
    trust_index = trust.index.get_loc(
        trust[trust.vendor == current_vendor].iloc[0].name)
    total_index = total.index.get_loc(
        total[total.vendor == current_vendor].iloc[0].name)
    return sales_index + trust_index + total_index


def set_sales(row, sales):
    current_vendor = row.vendor
    result = sales[sales.vendor == current_vendor]
    sales_index = sales.index.get_loc(result.iloc[0].name)
    return sales_index


def set_trust(row, trust):
    current_vendor = row.vendor
    result = trust[trust.vendor == current_vendor]
    trust_index = trust.index.get_loc(result.iloc[0].name)
    return trust_index


def set_total(row, total):
    current_vendor = row.vendor
    result = total[total.vendor == current_vendor]
    total_index = total.index.get_loc(result.iloc[0].name)
    return total_index


def set_famous_sellers(dataframe):
    print(dataframe.head())
    sales = dataframe.sort_values(
        by="sales", axis=0, ascending=False).reset_index()
    trust = sellers.sort_values(
        by="trust", axis=0, ascending=False).reset_index()
    total = sellers.sort_values(
        by="total", axis=0, ascending=False).reset_index()

    dataframe['sales_pos'] = dataframe.apply(
        lambda row: set_sales(row, sales), axis=1)
    dataframe['trust_pos'] = dataframe.apply(
        lambda row: set_trust(row, trust), axis=1)
    dataframe['total_pos'] = dataframe.apply(
        lambda row: set_total(row, total), axis=1)
    dataframe['popularity'] = dataframe.apply(
        lambda row: set_new_popularity(row, sales, trust, total), axis=1)
    new_list = dataframe.sort_values(by="popularity", ascending=True)
    print(new_list.keys())
    return new_list

    # def setPopularity(row):
    #     return 0.9*float(row['sales'])+30000000*float(row['trust'])+0.2*float(row['total'])
    # sellers['popularity'] = sellers.apply(
    #     lambda row: setPopularity(row), axis=1)

    # newSellers = sellers.nlargest(258, 'popularity')
    # print(newSellers.sort_values(by='popularity', ascending=False))

    # newSellers.to_csv(r'../data/famousSellers.csv', index=False)


def get_cat_subcat_vendors():
    dataframe = list_duplicates
    colums_to_drop = ['product_url', 'product_title',
                      'product_views_sales_quantityleft', 'vendor_url', 'BTC', 'file', 'crawling_date']
    result = dataframe.dropna()
    result = result.drop(columns=colums_to_drop, axis=1)
    result['product_id_subcategory'] = result['product_id_subcategory'].apply(
        clean_subcat_column)

    result['product_category'] = result['product_category'].apply(
        clean_cat_column)

    products_sells = result.dropna()
    products_sells['USD'] = products_sells['USD'].apply(clean_usd_column)
    products_sells['USD'] = products_sells['USD'].astype(float)
    products_sells = products_sells.groupby(
        ['product_category', 'product_id_subcategory', 'vendor']).agg({'USD': ['sum']}).reset_index()
    return products_sells


def get_seller_popularity():
    dataframe = seller_duplicates
    colums_to_drop = ['fe_allowed', 'percent_posfb',
                      'fb_1Pos', 'fb_6Pos', 'fb_12Pos', 'fb_1Neu', 'fb_6Neu', 'fb_12Neu',
                      'fb_1Neg', 'fb_6Neg', 'fb_12Neg', 'last', 'fb_left',
                      'spendings', 'pgp', 'file', 'crawling_date', 'disputes_orders']

    sellers = dataframe.drop(columns=colums_to_drop, axis=1)
    sellers = sellers.drop(columns=['description'], axis=1)
    sellers = sellers.dropna(subset=['trust'])
    sellers['member_since'] = pd.to_datetime(
        sellers['member_since'], format='%B %d, %Y')
    sellers['lvl'] = sellers['lvl'].apply(clean_vendor_trst_lvl_columns)
    sellers['trust'] = sellers['trust'].apply(clean_vendor_trst_lvl_columns)
    sellers['sales'] = sellers['sales'].apply(clean_sales_column)
    sellers.sales = sellers.sales.astype(int)
    sellers.lvl = sellers.lvl.astype(int)
    sellers.trust = sellers.trust.astype(int)
    sellers.vendor = sellers.vendor.astype(str)

    print(sellers.head())
    return sellers


def set_popularity(row):
    # print(row.vendor)
    return


def compute_popularity(dataframe):
    dataframe['popularity'] = dataframe.apply(
        lambda row: row.vendor in famous_sellers.values, axis=1)
    dataframe = dataframe.sort_values(by='popularity', ascending=False)
    return dataframe


def main():
    vendors_subcat = get_cat_subcat_vendors()
    vendors_info = get_seller_popularity()
    full_info_vendors = vendors_subcat.merge(vendors_info, on='vendor')
    full_info_vendors.columns = ['vendor', 'product_category',
                                 'product_sub_category', 'vendors', 'total_usd', 'sales', 'lvl', 'trust', 'member_since']
    full_info_vendors = full_info_vendors.dropna()
    full_info_vendors = set_famous_sellers(
        full_info_vendors.drop(columns=['vendors'], axis=1))

    full_info_vendors.to_csv(path_to_datas+'/full_info_vendors.csv')


main()
