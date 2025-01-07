from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
import pandas as pd

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Vytvoří složku, pokud neexistuje

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Uložení souboru
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Načtení Excelu
        df = pd.read_excel(file_path, engine="openpyxl")

        # Ověření, zda soubor není prázdný
        if df.empty:
            raise HTTPException(status_code=400, detail="Excel file is empty or unreadable")

        # Ošetření NaN hodnot (nahrazení "" místo None)
        df = df.fillna("")  

        # Příklad rozdělení na info a user (nutné upravit podle reálných dat)
        json_data = {
            "info": df.iloc[0].to_dict(),  # První řádek jako info
            "user": df.to_dict(orient="records")  # Celá tabulka jako seznam uživatelů
        }

        return json_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
