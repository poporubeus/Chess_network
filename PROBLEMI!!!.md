### Problema

Il problema che per ora ci sta bloccando è il seguente: abbimao creato una prima funzione che scorre all'interno di urls in diverse pagine html, bene,
in questo modo l'idea è fornire a Python una lista di urls e lui ci entrerà e ci mostrerà in un df tutti i tornei.
Successivamente abbiamo generato un'altra funzione che scorre nelle pagine di quel torneo (se è molto grande) e ci ritorna tutti i rounds già messi nello stesso df
per quello specifico torneo. Abbiamo provato a far andare e funziona, come si vede dal network (n.b. abbiamo unito solo 3 tornei per ora).
Se però faccimo runnare la funzione con una lista di tornei che non hanno pagine aggiuntive (dunque il numero di pagine da fornire alla nostra funzione è :
lista di 1 lunga quanto il numero di tornei presenti  --> esempio: ho 4 tornei allora gli dico [1,1,1,1]) NON VA: RITORNA UN RISULTATO SBAGLIATO.
COME MAI?

# Altra cosa da capire:
Ho usato l'algoritmo di Lovain per realizzare la community:
```shell
pip install python-louvain
```
Bisogna capire come lui realizza le community: non ho studiato ancora, dunque bisogna essere sicuri di come lui (Python) realizzi le communities: secondo cosa?
Possiamo dirgli noi come fare? Possiamo costruire un NOSTRO algoritmo per fare la detection community?
