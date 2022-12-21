# Chess_network
A network on chess players

# COSE DA FARE:
Le cose da fare sono contenute nel file.txt.
Il codice qui presente è per fare un pochino di pratica, l'idea però è continuare per portare a termine il punto n° 1 dell'elenco nel .txt
-------
L'idea è costruire una funzione che legga una lista di url corrispondenti ai diversi tornei presenti su Chess365.
Successivamente, tale funzione richiama quella appena creata nel notebook che scorre lungo l'url del torneo e prend i vari round contenuti
in pagine diverse. Altrimenti, invece che fare la funzione che legge la lista di tornei, si richiama tot volte la funzione per andare a leggere i round e BONA.

# Dove reperire i dati:
Chess365

### LIBRERIE DA SCARICARE:
1) numpy;
2) pandas;
3) matplotlib.pyplot;
4) networkx;
5) sklearn (machine learning - decision tree);
6) seaborn;
7) plotly;
8) pyvis.

### Importante:
Assicurati di avere il kernel ipykernel così da sostituire il kernel Python3 che Jupyter ha di default
con quello. In questo modo Jupyter utilizzerà lo stesso Python che avete installato: io uso Python3.10
ma quello di Jupyter è il 3.8 --> non sono compatibili, pertanto i pacchetti installati con 
Python3.10 non saranno visibili da Jupyter.

## Comando per fare questo
```shell
pip install ipykernel
```
e dovrebbe andare; altrimenti guarda qua:
" https://jonathansoma.com/course/foundations-2021/jupyter-module-not-found/ "
