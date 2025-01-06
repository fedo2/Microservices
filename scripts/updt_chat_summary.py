import os

def read_chat_summary(file_path):
    """Načte obsah souboru chat_summary.md."""
    if not os.path.exists(file_path):
        return "# Souhrn chatů projektu Hugo72 – Microservices\n\n"
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def update_chat_summary(content, new_chat_entry):
    """Přidá nový záznam do souhrnu chatů."""
    if new_chat_entry in content:
        print("Chat již existuje v souhrnu.")
        return content
    return content + new_chat_entry + "\n"

def write_chat_summary(file_path, content):
    """Zapíše aktualizovaný souhrn zpět do souboru."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    FILE_PATH = "docs/chat_summary.md"
    NEW_CHAT_ENTRY = "#### **Chat 011 – 2025-01-06**\n- Přidána podpora pro automatickou aktualizaci souhrnu chatů pomocí Python skriptu a GitHub Actions.\n\n"
    
    current_content = read_chat_summary(FILE_PATH)
    updated_content = update_chat_summary(current_content, NEW_CHAT_ENTRY)
    write_chat_summary(FILE_PATH, updated_content)
    
    print("Souhrn chatů byl aktualizován.")
