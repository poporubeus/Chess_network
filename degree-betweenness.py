import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import collections
import seaborn as sns
import plotly.express as px
from scipy.stats import linregress


def clean_dataframe(dataframe): #questa funzione pulisce il df eliminando le colonne inutili e droppa i NaN
  df = pd.read_csv(dataframe)
  new_df = pd.DataFrame(df, columns=['White', 'Black', 'Result', 'Date', 'Opening'])
  new_df.dropna()
  return new_df


def drop_entries_less_than_n(df, columns, n): #questa è la funzione di Luca che crea un nuovo df togliendo le i nodi che hanno degree<n, l'ho tenuta solo per bellezza xk non credo la useremo
    combined_list = df[columns].values.flatten().tolist()
    count_series = pd.Series(combined_list).value_counts()
    count_df = pd.DataFrame({'Element': count_series.index, 'Count': count_series.values})
    entries_to_drop = count_df[count_df['Count'] < n]['Element'].tolist()
    df = df[~df[columns].apply(lambda x: x[0] in entries_to_drop and x[1] in entries_to_drop, axis=1)]
    return df, count_df

def create_network_from_dataframe(df): #ritorna il network creato partendo da un df pulito
   G = nx.from_pandas_edgelist(df, source='White', target='Black')
   return G

def draw_and_save_network(G,node_size,with_labels,path): #visualizza e salva in locale un network, prende G, la node-size e un bool se vogliamo mettere o no i labels e il percorso-nome in cui salvare
   fig = nx.draw(G, node_size=node_size, with_labels = with_labels)
   plt.savefig(path)
   plt.show()

def plot_histogram_with_vertical_labels(Names_x_axis,observable): #plotta e salva l'istogramma di un'osservabile coi nomi in verticale e.g. degree dei primi 50 giocatori 
   plt.bar(Names_x_axis,observable)
   plt.xticks(rotation='vertical')
   plt.savefig('./histogram_with_vertical_labels.png')
   plt.show()

def network_diameter(G):
   return nx.diameter(G)


def create_connected_components_of_network(G):
   S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
   return S

def central_cluster_of_network(G):
   largest_cc = max(nx.connected_components(G), key=len)
   cc = G.subgraph(largest_cc).copy() 
   return cc

def degree_list(G): #questa ritorna 2 liste: la lista delle degree dei giocatori e la lista dei nomi dei giocatori
   degree = dict(G.degree())
   names_list=list(degree.keys())
   degree_list=list(degree.values())
   return degree_list,names_list

def betweenness_list(G,normalized): #questa prende il network e la bool che dice se vogliamo la betwenness normalizzata o no e ritorna 2 liste: la lista delle betwenness e la lista dei nomi dei giocatori
   bet=dict(nx.betweenness_centrality(G,normalized=normalized))
   names_list=list(bet.keys())
   bet_list=list(bet.values())
   return bet_list,names_list

def raw_sorting_algorithm(list_to_sort,connected_list): #questa ordina 2 liste. list_to_sort è la lista su cui si ha il controllo dell'ordinamento in senso decrescente, connected_list è la lista collaterale che viene ordinata seguendo l'altra, ritorna le liste ordinate
   for i in range(len(list_to_sort)):
      for j in range(len(list_to_sort)-1):
         if list_to_sort[j]<list_to_sort[j+1]:
            var = list_to_sort[j]
            list_to_sort[j]=list_to_sort[j+1]
            list_to_sort[j+1] = var
            var= connected_list[j]
            connected_list[j]=connected_list[j+1]
            connected_list[j+1] = var
   return list_to_sort,connected_list
      
def intersection_of_lists(list1,list2): #ritorna la lista degli elementi in comune tra due liste passate come parametri
   intersection=[]
   for item in list1:
      if item in list2:
         intersection.append(item)
   return intersection   

def create_df_with_names_degree_betweenness(Names,degree,betweenness):#prende le liste con nomi,degree e betweenness e ne crea un df
   d = {'Name': Names, 'Degree':degree,
   'Betweenness':betweenness }
   df= pd.DataFrame(data=d)
   return df

def scatterplot(df,feature1,feature2,labels,color):#fa scatterplot e printa dato il df di partenza, le due colonne che saranno x e y, la colonna dei labels e quella dei colori. Si downloada direttamente, non si salva
   fig = px.scatter(data_frame=df, x=feature1, y=feature2, hover_name=labels, color=color)
   fig.show()

def linear_regression(x,y):#ritorna il coef.angolare, l'intercetta e il coef. di correlazione tra due liste x e y 
   result = linregress(x=x,y=y)
   return result.slope,result.intercept,result.rvalue


df2020 = './chess_data_2020.csv'
df2020 = clean_dataframe(df2020)
G=create_network_from_dataframe(df2020)
draw_and_save_network(G,1,False,'./network')
central_subgraph=central_cluster_of_network(G)
degree_list,names_list=degree_list(G)
betweenness_list=betweenness_list(G,True)[0]
values_df=create_df_with_names_degree_betweenness(names_list,degree_list,betweenness_list)
correl_coefficient=linear_regression(degree_list,betweenness_list)[2]
scatterplot(values_df,'Degree','Betweenness','Name','Degree')
print(correl_coefficient)
