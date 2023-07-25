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


path = "/Users/francescoaldoventurelli/Desktop/codici_CN/chess_data_2020.csv"
path_to_save = "/Users/francescoaldoventurelli/Desktop/nx_saved.jpg"

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

#print(df["Opening"].values)
new_df = save_first3(df)
new_df.dropna()

list_opening = new_df["ECO"].values
unique_opening = [*set(list_opening)]
#print(unique_opening)

#print(len(unique_opening))
#print(new_df)
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
opening_graph = nx.bipartite.weighted_projected_graph(graph, unique_opening, ratio=True)

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
    
plt.show()