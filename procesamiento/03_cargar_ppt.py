import os
from pathlib import Path
from dotenv import load_dotenv
from funciones import upload_pptx_oauth

load_dotenv()

## Configración de subida y formato
FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

###

pptx_salida_ruta = os.path.join("auxiliares/plantillas/monitoreo-ensu-cdmx.pptx")

resp = upload_pptx_oauth(
     pptx_salida_ruta,
     folder_id=FOLDER_ID,
     client_secret_json="auxiliares/credenciales/client_secret.json",
 )
print("Subido:", resp["name"], resp["id"], resp.get("webViewLink"))