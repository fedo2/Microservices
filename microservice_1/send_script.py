import requests

API_URL = "http://127.0.0.1:8000/upload"  # Endpoint mikroservisy_1
FILE_PATH = "data.xlsx"  # Cesta k souboru

def send_file():
    """Odešle data.xlsx na mikroservisu_1 a zobrazí uživateli výsledek."""
    try:
        with open(FILE_PATH, "rb") as file:
            response = requests.post(API_URL, files={"file": file})

        if response.status_code == 200:
            print("✅ Data dorazila v pořádku!")
            json_data = response.json()
            print("📊 Přijatá data:", json_data)  # Debug výstup

            # TODO: Poslat json_data dál do mikroservisy_2

        else:
            print(f"❌ Chyba při zpracování: {response.json()['detail']}")

    except Exception as e:
        print(f"❌ Chyba při odesílání souboru: {str(e)}")

if __name__ == "__main__":
    send_file()
