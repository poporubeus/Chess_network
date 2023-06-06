import networkx as nx

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from networkx.algorithms.community.centrality import girvan_newman
#import time

#t = time.time()
df_tot = pd.read_csv('/Users/francescoaldoventurelli/Desktop/Chess_network/.venv/codici/df_tot.csv')

df2001 = df_tot[df_tot['Date'] == '2001']
G = nx.from_pandas_edgelist(df2001, source='White', target='Black')


communities = girvan_newman(G)

node_groups = []
for com in next(communities):
    node_groups.append(list(com))

print(node_groups)

color_map = []
for node in G:
    if node in node_groups[0]:
        color_map.append("red")
    else:
        color_map.append("blue")
nx.draw(G, node_color=color_map, with_labels=False)
plt.show()


