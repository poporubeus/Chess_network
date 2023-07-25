import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
#from degree_betweenness import *
import pandas as pd
import networkx.algorithms.community as community3
from networkx.algorithms.community import louvain_partitions
import matplotlib.cm as cm
#import community
import community.community_louvain as community_louvain
from networkx.algorithms.community import girvan_newman
import community as cmm
import copy


path = "./chess_data_2020.csv"
path_to_save = "./nx_saved.jpg"

def clean_dataframe(dataframe): #questa funzione pulisce il df eliminando le colonne inutili e droppa i NaN
  df = pd.read_csv(dataframe)
  new_df = pd.DataFrame(df, columns=['White', 'Black', 'Result', 'Date', 'Opening'])
  new_df.dropna()
  return new_df

def create_network_from_dataframe(df, source, target): #ritorna il network creato partendo da un df pulito
   G = nx.from_pandas_edgelist(df, source, target)
   return G

def draw_and_save_network(G,node_size,with_labels,path_to_save): #visualizza e salva in locale un network, prende G, la node-size e un bool se vogliamo mettere o no i labels e il percorso-nome in cui salvare
   fig = nx.draw(G, node_size=node_size, with_labels = with_labels)
   plt.savefig(path_to_save)


df = clean_dataframe(path)
#print(df)

#bip = create_network_from_dataframe(df, )

def save_first3(dataframe):
    new_name = []
    for i in dataframe["Opening"].values:
        
        new_name.append(str(i)[:3])
    
    dataframe = dataframe.drop("Opening", axis=1)
    dataframe.insert(4, "ECO", new_name, False)
    return dataframe



new_df = save_first3(df)
new_df=new_df.dropna()

list_players_white=new_df['White'].values
list_players_black=new_df['Black'].values
list_players_full=list_players_white+list_players_black
unique_players=[]
for i in list_players_white:
    unique_players.append(i)
for i in list_players_black:
    unique_players.append(i)
unique_players=[*set(unique_players)]

graph = nx.Graph()

# Add nodes from the 'white' and 'black' columns
graph.add_nodes_from(new_df['White'], bipartite=0)
graph.add_nodes_from(new_df['Black'], bipartite=1)

# Add edges connecting 'white' and 'opening' nodes
white_opening_edges = [(row['White'], row['ECO']) for _, row in new_df.iterrows()]
graph.add_edges_from(white_opening_edges)

# Add edges connecting 'black' and 'opening' nodes
black_opening_edges = [(row['Black'], row['ECO']) for _, row in new_df.iterrows()]
graph.add_edges_from(black_opening_edges)

# Project the bipartite graph onto the 'opening' nodes
players_graph = nx.bipartite.weighted_projected_graph(graph, unique_players, ratio=True)
print('players graph created')
#pos = nx.spring_layout(players_graph)
#nx.draw(players_graph, pos, with_labels=unique_players, node_color='lightblue', node_size=50, font_size=2, width=0.1)
#plt.axis('off')
#graph_louvain = community3.louvain_communities(players_graph)
#partitions = community_louvain.best_partition(players_graph)
#print(partitions)
k=8
communities=community3.asyn_fluidc(players_graph, k,max_iter=10, seed=None)
fluid_communities=[]
for i in range(k):
    fluid_communities.append(list(next(communities)))


players_dict={}
colors=['sienna','aquamarine','tomato','forestgreen','gold','azure','orchid','plum']
for i in unique_players:
    players_dict[i]=i
plt.figure(figsize=(12,8))
# draw the graph
pos = nx.spring_layout(players_graph)
# color the nodes according to their partition
nx.draw_networkx_edges(players_graph, pos, alpha=0.5,width=0.3)
for com in range(len(fluid_communities)):
    for player in range(len(fluid_communities[com])):
        node=fluid_communities[com][player]
        nx.draw_networkx_nodes(players_graph, pos, [node], node_size=50,
                           node_color=colors[com])
nx.draw_networkx_labels(players_graph,pos,players_dict,font_size=1)
plt.axis('off')
plt.show()
#communities_gn=girvan_newman(players_graph)
#communities_gn=tuple(sorted(c) for c in next(communities_gn))
#print(communities_gn)
#G = nx.path_graph(10)comp = girvan_newman(G)tuple(sorted(c) for c in next(comp))([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])
"""
graph_louvain = community3.louvain_communities(opening_graph)
#print(graph_louvain)

ecos = [i for i in new_df["ECO"].values]

partitions = community_louvain.best_partition(opening_graph)
print(partitions)


# Plot the projected graph
pos = nx.spring_layout(opening_graph)

#pos = nx.spring_layout(graph)
plt.figure(figsize=(8, 6))
#nx.draw(graph, pos, with_labels=ecos, node_color='lightblue', node_size=50, font_size=2, width=0.1)
nx.draw(opening_graph, pos, with_labels=ecos, node_color='lightblue', node_size=50, font_size=2, width=0.1)
plt.title("Projected Bipartite Graph")
plt.axis('off')



#print(df["Opening"].values)


#partition = best_partition(opening_graph)

cmap = cm.get_cmap('viridis', max(partitions.values()) + 1)


plt.figure(figsize=(12,8))
# draw the graph
pos = nx.spring_layout(opening_graph)
# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partitions.values()) + 1)
nx.draw_networkx_edges(opening_graph, pos, alpha=0.5)
for node, color in partitions.items():
    nx.draw_networkx_nodes(opening_graph, pos, [node], node_size=100,
                           node_color=[cmap.colors[color]])
    
plt.show()"""