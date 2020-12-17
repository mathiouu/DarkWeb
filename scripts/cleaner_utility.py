import re


def clean_sub_cat_column(text):
    clean = str(text).replace(' ', '')
    regex = '(Item#.\\d+-)(.+)(-.*)'
    regex1 = '(.*)\\/(.*)'
    clean = re.match(regex, str(clean))
    clean = re.match(regex1, clean.groups()[1])
    res = clean.groups()[0]
    return res


def clean_category_column(text):
    clean = text.strip()
    regex = '(\\W*)(.+)(\\s*)'
    clean = re.match(regex, str(clean))
    res = clean.groups()[1]
    return res


def clean_usd_column(text):
    return str(text).replace(',', '')


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
