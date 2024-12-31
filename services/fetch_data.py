import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Variables de entorno
PAGERDUTY_API_URL = os.getenv("PAGERDUTY_API_URL")
API_TOKEN = os.getenv("API_TOKEN")
DATA_FILE = os.getenv("DATA_FILE", "data/services_data.json")

def fetch_and_set_data():
    headers = {
        "Authorization": f"Token token={API_TOKEN}",
        "Accept": "application/vnd.pagerduty+json;version=2"
    }

    if not DATA_FILE:
        raise ValueError("DATA_FILE no está definido en el archivo .env o como predeterminado.")

    directory = os.path.dirname(DATA_FILE)
    if directory:  
        os.makedirs(directory, exist_ok=True)

    try:
        response = requests.get(PAGERDUTY_API_URL, headers=headers)
        response.raise_for_status()  

        data = response.json()
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("Datos cargados y guardados exitosamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")
