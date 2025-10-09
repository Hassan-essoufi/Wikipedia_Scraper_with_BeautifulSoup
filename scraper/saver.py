import os 
import json

def save_raw_html(html_doc,filname):
    os.makedirs("data/raw",exist_ok=True)
    filepath = os.path.join("data", "raw", filname)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(html_doc)
    print(f"Fichier sauvegardé : {filepath}")


def save_processed_html(html_proc, filename):
    os.makedirs("data/processed", exist_ok=True)
    filepath = os.path.join("data", "processed", filename.replace(".html", ".json"))
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(html_proc, file, ensure_ascii=False, indent=4)
    print(f"Données structurées sauvegardées : {filepath}")
