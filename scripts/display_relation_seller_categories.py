from tulip import tlp
import csv


def main(g):
    category = graph['category']
    viewLabel = graph['viewLabel']
    full_info_vendors_path = 'data/full_info_vendors.csv'
    # full_info_vendors_path = 'C:\\Users\\sebas\\cours\\Master2\\Analyse-Reseau\\projetDarkWeb\\DarkWeb\\data\\full_info_vendors.csv'
    # datasPath = "C:/Users/sebas/cours/Master2/Analyse-Reseau/projetDarkWeb/DarkWeb/data"
    viewMetric = graph['viewMetric']
    viewIcon = graph['viewIcon']
    viewColor = graph['viewColor']
    test = graph['test']
    popularity = graph['popularity']
    g.clear()
    nodes = {}
    counter = 0
    with open(full_info_vendors_path, newline='', encoding='utf-8') as csvfile:
        drops = csv.DictReader(csvfile, delimiter=',')
        for row in drops:
            product_subcategory = row['product_sub_category']
            if len(product_subcategory) == 0:
                continue
            vendor = row['vendor']
            node_product_subcategory = tlp.node()
            node_vendor = tlp.node()
            if product_subcategory in nodes:
                node_product_subcategory = nodes[product_subcategory]
            else:
                node_product_subcategory = g.addNode()
                viewIcon[node_product_subcategory] = "md-circle"
                viewLabel[node_product_subcategory] = product_subcategory
                nodes[product_subcategory] = node_product_subcategory
                category[node_product_subcategory] = row['product_category']

            if vendor in nodes:
                node_vendor = nodes[vendor]
            else:
                node_vendor = g.addNode()
                viewIcon[node_vendor] = "md-human"
                viewLabel[node_vendor] = vendor
                nodes[vendor] = node_vendor
                
                popularity[node_vendor] = int(row['popularity']) < 2000

            e = g.existEdge(node_product_subcategory, node_vendor, True)
            if e.isValid():
                viewMetric[e] += 1
            else:
                e = g.addEdge(node_product_subcategory, node_vendor)
