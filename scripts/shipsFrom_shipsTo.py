# Powered by Python 3.7
# To cancel the modifications performed by the script
# on the current graph, click on the undo button.
# Some useful keyboard shortcuts:
#   * Ctrl + D: comment selected lines.
#   * Ctrl + Shift + D: uncomment selected lines.
#   * Ctrl + I: indent selected lines.
#   * Ctrl + Shift + I: unindent selected lines.
#   * Ctrl + Return: run script.
#   * Ctrl + F: find selected text.
#   * Ctrl + R: replace selected text.
#   * Ctrl + Space: show auto-completion dialog.
from tulip import tlp
import csv
import os

# The updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views
# The pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the
# "Run script " button.
# The runGraphScript(scriptFile, graph) function can be called to launch
# another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call
# (in the form [a-zA-Z0-9_]+.py)
# The main(graph) function must be defined
# to run the script on the current graph
def main(g):
    viewLabel = graph['viewLabel']
    datasPath = "C:/Users/sebas/cours/Master2/Analyse-Reseau/projetDarkWeb/DarkWeb/data"
    viewMetric = graph['viewMetric']
    g.clear()
    nodes = {}
    with open(datasPath+'/ad_duplicates_drop.csv', newline='', encoding='utf-8') as csvfile:
        ad = csv.DictReader(csvfile, delimiter=';')
        for row in ad:
            sfrom = row['ships_from'].strip()
            if len(sfrom)==0:
                continue
            sto = row['ships_to'].split(',')
            sto = [x.strip() for x in sto]
            nfrom = tlp.node()
            nto = tlp.node()
            #always one sender
            if sfrom in nodes:
                nfrom = nodes[sfrom]
            else:
                nfrom = g.addNode()
                viewLabel[nfrom]=sfrom
                nodes[sfrom]=nfrom
 
            for st in sto:
                if st in nodes:
                    nto = nodes[st]
                else:
                    nto = g.addNode()
                    viewLabel[nto]=st
                    nodes[st]=nto
            
                e = g.existEdge(nfrom, nto, True)
                if e.isValid():
                    viewMetric[e] +=1
                else:
                    e = g.addEdge(nfrom, nto)
                    viewMetric[e] = 1

  
