import re

def parse_highlights():
    # Chiede il percorso dei file all'utente
    input_file = input("Inserisci il percorso del file di origine (.txt): ").strip()
    output_file = input("Inserisci il percorso del file di destinazione (.md): ").strip()

    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    markdown_lines = []

    # Sezione dei metadati
    metadata = {
        "Author": None,
        "Full Title": None,
        "Category": "#books"
    }

    # Trova e salva i metadati dinamicamente
    for line in lines:
        if "Autore:" in line:
            metadata["Author"] = line.split(':', 1)[1].strip()
        elif "Titolo:" in line:
            metadata["Full Title"] = line.split(':', 1)[1].strip()

    markdown_lines.append("## Metadata")
    for key, value in metadata.items():
        if value:
            markdown_lines.append(f"- {key}: {value}")
    markdown_lines.append("\n---\n")

    current_section = None

    for i, line in enumerate(lines):
        line = line.strip()

        # Gestione dei tag delle sezioni (h1, h2, ecc.) con contenuto corretto
        if line.endswith('【Nota】.h1'):
            title = lines[i - 1].strip() if i > 0 else ""
            current_section = f"# {title}"
            markdown_lines.append(current_section)
        elif line.endswith('【Nota】.h2'):
            title = lines[i - 1].strip() if i > 0 else ""
            current_section = f"## {title}"
            markdown_lines.append(current_section)
        elif line.endswith('【Nota】.h3'):
            title = lines[i - 1].strip() if i > 0 else ""
            current_section = f"### {title}"
            markdown_lines.append(current_section)
        elif line.endswith('【Nota】.h4'):
            title = lines[i - 1].strip() if i > 0 else ""
            current_section = f"#### {title}"
            markdown_lines.append(current_section)

        # Gestione del tag "【Nota】" senza specifico h1, h2, ecc.
        elif line == '【Nota】':
            paragraph = lines[i - 1].strip() if i > 0 else ""
            if paragraph:
                markdown_lines.append(paragraph)

        # Gestione dei contenuti normali
        elif line and not line.startswith('2024-') and not line.startswith('Pagina Nr.:') and not line.endswith('【Nota】.h1') and not line.endswith('【Nota】.h2') and not line.endswith('【Nota】.h3') and not line.endswith('【Nota】.h4'):
            markdown_lines.append(f"- {line}")

    # Scrive il file markdown
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(markdown_lines))

    print(f"File markdown generato: {output_file}")

# Esegue la conversione
parse_highlights()
