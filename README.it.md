# VideoPath

VideoPath è una semplice utility per migrare con facilità i riferimenti alle risorse, memorizzati nei progetti del software VideoPad Video Editor, da un percorso a un altro.

# Il problema

VideoPad Video Editor, o VideoPad Professional, &egrave; un'applicazione Windows per l'editing del video digitale con un'interfaccia pulita e facile da utilizzare ma la cui semplicità d'uso non deve ingannare: questo editor video è dotato, infatti, di potenti funzioni di montaggio.

![Esempio di come appare VideoPad](docs/videopad-interface.png)

***Figure 1. Un esempio di come appare l'interfaccia principale di VideoPad***

Tuttavia, una volta che un progetto &egrave; stato creato, e che quindi sono stati stabiliti i percorsi nel file system delle risorse cui il progetto fa riferimento, cambiare la posizione di tali risorse &egrave; laborioso.

Nei progetti di VideoPad Video Editor, i percorsi delle risorse linkate sono memorizzati come percorsi assoluti. 
Pertanto, anche se si sposta tutta la cartella contenente sia il progetto sia le risorse, all'avvio del progetto - dal momento che i percorsi assoluti sono cambiati - il software non trover&agrave; le risorse e quindi non potr&agrave; caricarle.
Ci&ograve; generer&agrave; una serie di errori, che verranno mostrati in un'apposita maschera.

![Maschera per risolvere i percorsi delle risorse non trovate](docs/missing-items.png)

***Figura 2. Maschera per l'aggiornamento dei percorsi delle risorse non trovate. Notare, da quanto &egrave; piccola la scrollbar sulla destra, quanti devono essere in questo progetto i files non trovati...***

Agendo sui pulsanti della maschera (bottoni "Risolvi") &egrave; possibile aggiornare il percorso di ogni risorsa ma, soprattutto nei progetti che fanno riferimento a molte risorse (files audio, musica, immagini, spezzoni video etc.), ricaricare ogni singola risorsa nel progetto risulta veramente scocciante.
Non &egrave; possibile, infatti, specificare solo il percorso ma bisogna puntare alla risorsa specifica e ricaricarla; inoltre, in caso di svista, il software non segnala il problema.

&Egrave; anche disponibile un tool di migrazione, ma questo non sposterà il progetto da un percorso all'altro mantenendo i percorsi relativi delle risorse ma appiattirà tutto, file di progetto e files linkati, in un'unica directory.
Inoltre, la migrazione funzionerà solo a partire da un progetto funzionante: se il progetto è stato spostato e dunque le risorse non vengono trovate, non sarà possibile caricarlo e quindi tanto meno migrarlo.

Al di là di questo aspetto, anche se il progetto fosse funzionante, la distruzione dei percorsi relativi delle risorse rispetto al progetto, dovuto alla migrazione, non era ciò che volevo: io desideravo, infatti, poter spostare i progetti riposizionandoli in altre cartelle ma mantenendo le posizioni relative delle risorse rispetto al progetto. 

Stanco di ricaricare a mano tutte le risorse ogni volta che cambiavo idea sulla collocazione di un progetot, ho perciò pensato di sviluppare un'utility che facesse proprio questo.

![Work in progress](docs/work-in-progress.png)

***Work in progress***

## La soluzione

## Esempi