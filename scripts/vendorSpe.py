from tulip import tlp
import csv

def main(g):
    viewLabel = graph['viewLabel']
    datasPath = "C:/Users/sebas/cours/Master2/Analyse-Reseau/projetDarkWeb/DarkWeb/data"
    viewMetric = graph['viewMetric']
    viewIcon = graph['viewIcon']
    g.clear()
    nodes = {}
    counter = 0
    with open(datasPath+'/r_list_duplicates_drop.csv', newline='', encoding='utf-8') as csvfile:
        drops = csv.DictReader(csvfile, delimiter=';')
        for row in drops:
            product_category = row['product_category'].strip()
            if len(product_category)==0:
                continue
            vendor = row['vendor'].strip()
            node_product_category = tlp.node()
            node_vendor = tlp.node()
            if product_category in nodes:
                node_product_category = nodes[product_category]
            else:
                node_product_category = g.addNode()
                viewIcon[node_product_category] = "md-circle"
                viewLabel[node_product_category]=product_category
                nodes[product_category]=node_product_category
            
            if vendor in nodes:
                node_vendor = nodes[vendor]
            else:
                node_vendor = g.addNode()
                viewIcon[node_vendor] = "md-human"
                viewLabel[node_vendor] = vendor
                nodes[vendor] = node_vendor
            
            e = g.existEdge(node_product_category, node_vendor,True)
            if e.isValid():
                viewMetric[e] +=1
            else:
                e= g.addEdge(node_product_category,node_vendor)

  
