# README

## Descrizione dello Script
Questo script Python converte file di testo contenenti annotazioni di libri in file Markdown strutturati.
Nello specifico puoi esportare tutte le annotazioni da un libro letto in **NeoReader su un e-ink Onyx Boox** da e caricare il markdown su **Obsidian**!

### Funzionalità Principali
1. **Parsing dei Metadati:**
   - Estrae metadati come autore, titolo completo e categoria.
2. **Gestione delle Sezioni:**
   - Supporta tag gerarchici come `.h1`, `.h2`, `.h3`, `.h4` e li converte in titoli Markdown.
3. **Raggruppamento dei Contenuti:**
   - Raccoglie i contenuti che appartengono alla stessa sezione in un unico blocco.
4. **Compatibilità Markdown:**
   - Genera un file ben strutturato pronto per essere utilizzato in qualsiasi strumento di gestione Markdown.

---

## Requisiti
- Python 3.7 o superiore.
- Sistema operativo compatibile con Python (Windows, macOS, Linux).

---

## Installazione
1. Clona il repository:
   ```bash
   git clone https://github.com/tuo-username/repository-name.git
   cd repository-name
   ```

2. Assicurati di avere Python installato. Puoi verificarlo con:
   ```bash
   python --version
   ```

---

## Utilizzo

1. Esegui lo script:
   ```bash
   python script_name.py
   ```

2. Segui le istruzioni per:
   - Inserire il percorso del file di input (ad esempio: `annotazioni.txt`).
   - Specificare il percorso e il nome del file di output (ad esempio: `output.md`).

3. Lo script genererà un file Markdown con una struttura leggibile e ben organizzata.

---

## Formato Atteso del File di Input
- Il file deve essere un file di testo `.txt`.
- Deve includere tag come `【Nota】`, `【Nota】.h1`, ecc.
- Esempio:

```
Titolo: Il titolo del libro
Autore: Nome dell'autore

----------------------
Un esempio di contenuto
【Nota】.h1
Altro contenuto
----------------------
```

---

## Output
Il file di output sarà in formato Markdown con la seguente struttura:

```
## Metadata
- Author: Nome dell'autore
- Full Title: Il titolo del libro
- Category: #books

---

# Titolo Sezione 1
- Contenuto della sezione 1

## Sottosezione
- Contenuto della sottosezione
```

---

## Personalizzazioni
Per adattare lo script a formati di input diversi, puoi modificare le espressioni regolari o la logica di parsing all'interno della funzione `parse_highlights()`.

---

## Contribuzione
1. Forka il repository.
2. Crea un branch per la tua feature:
   ```bash
   git checkout -b feature-nome
   ```
3. Fai il commit delle tue modifiche:
   ```bash
   git commit -m "Descrizione della feature"
   ```
4. Push sul tuo branch:
   ```bash
   git push origin feature-nome
   ```
5. Apri una Pull Request.

---

## Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file `LICENSE` per maggiori dettagli.

