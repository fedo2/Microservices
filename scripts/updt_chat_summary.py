import os

FILE_PATH = "docs/chat_summary.md"

def read_chat_summary(file_path):
    """Načte obsah souboru chat_summary.md."""
    if not os.path.exists(file_path):
        print(f"Soubor {file_path} neexistuje, bude vytvořen nový.")
        return "# Souhrn chatů projektu Hugo72 – Microservices\n\n"
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def write_chat_summary(file_path, content):
    """Zapíše aktualizovaný souhrn zpět do souboru."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Zajistí, že složka existuje
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    print("Spouštím skript...")
    current_content = read_chat_summary(FILE_PATH)
    print("Současný obsah:")
    print(current_content)

    NEW_CHAT_ENTRY = "#### **Chat 011 – 2025-01-06**\n- Debugging chyb v GitHub Actions\n\n"
    
    updated_content = current_content + NEW_CHAT_ENTRY
    write_chat_summary(FILE_PATH, updated_content)

    print("Souhrn chatů byl aktualizován.")
