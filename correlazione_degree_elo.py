#from pyvis import Network as net

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import time

#t = time.time()
df2020 = '/Users/francescoaldoventurelli/Desktop/Chess_network/.venv/codici/chess_data_2020.csv'

#df2001 = df_tot[df_tot['Date'] == '2001']


def cut_dfs(dataframe):

  df = pd.read_csv(dataframe)

  new_df = pd.DataFrame(df, columns=['White', 'Black', 'Result', 'Date', 'Opening'])

  return new_df

df2020 = cut_dfs(df2020)
#print(df2020)
#print(len(df2020)) == 20178
df2020 = df2020.dropna()

def drop_entries_less_than_n(df, columns, n):
    combined_list = df[columns].values.flatten().tolist()
    count_series = pd.Series(combined_list).value_counts()
    count_df = pd.DataFrame({'Element': count_series.index, 'Count': count_series.values})
    entries_to_drop = count_df[count_df['Count'] < n]['Element'].tolist()
    df = df[~df[columns].apply(lambda x: x[0] in entries_to_drop and x[1] in entries_to_drop, axis=1)]
    return df, count_df


# Count the number of same elements in the combined list of first two columns and drop rows appearing less than 2 times
n = 5 # degree minima
df, count_df = drop_entries_less_than_n(df2020, ['White', 'Black'], n)
#print(df)
#print(count_df)


G = nx.from_pandas_edgelist(df, source='White', target='Black')
#fig = nx.draw(G, node_size=5, with_labels = True)
#plt.savefig('/Users/francescoaldoventurelli/Desktop/Chess_network/.venv/codici/nx2020CONNOMI_degree_dimuita.png')
#plt.show()

'''import collections
import matplotlib.pyplot as plt
import networkx as nx
G = nx.gnp_random_graph(100, 0.02)
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence",  degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
# draw graph in set
plt.axes([0.4, 0.4, 0.5, 0.5])
#Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True))
Gcc = sorted([G.subgraph(c) for c in nx.connected_components(G)], key=len, reverse=True)[0]
pos = nx.spring_layout(G)
plt.axis('off')
#nx.draw_networkx_nodes(G, pos, node_size=20)
#nx.draw_networkx_edges(G, pos, alpha=0.4)
#plt.show()'''

first_50players = count_df['Element']
first_50degrees=count_df['Count']
first_50players=first_50players[:50]
'''
plt.bar(first_50players[:50], first_50degrees[:50])
plt.xticks(rotation = 'vertical') 
plt.savefig('/Users/francescoaldoventurelli/Desktop/Chess_network/.venv/codici/hist_degree_50players.png')
plt.show()'''


#S = [G.subgraph(c).copy() for c in nx.connected_components(G)]


#for graph in S:
#   print(nx.diameter(graph))
largest_cc = max(nx.connected_components(G), key=len)
#print(len(largest_cc))
blob_central = G.subgraph(largest_cc).copy() 
#nx.draw(b)
#plt.show()

#print(nx.diameter(blob_central))

betweenness = nx.betweenness_centrality(G, normalized=True)
#print(betweenness)


points=list(betweenness.values())
players =list(betweenness.keys())
for i in range(len(points)):
   for j in range(len(points)-1):
      if points[j]<points[j+1]:
         var = points[j]
         points[j]=points[j+1]
         points[j+1] = var
         var= players[j]
         players[j]=players[j+1]
         players[j+1] = var
#print(players)
#print(points)


'''plt.bar(x=players[:50], height=points[:50])
plt.xticks(rotation='vertical')
plt.show()
print('Degreee dei giocatori')
print(first_50players)
print('')
print('Betweenness dei giocatori')
print(players[:50])'''


'''def lists_overlap(a, b):
  sb = set(b)
  return any(el in sb for el in a)

print(lists_overlap(first_50players, players[:50]))'''

list_of_common_players=[]
for player in first_50players:
   if player in players[:50]:
      print(player)
      list_of_common_players.append(player)
print(len(list_of_common_players))