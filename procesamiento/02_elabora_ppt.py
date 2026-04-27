import os 
from funciones import render_slides_for_ids
from pptx import Presentation
import pandas as pd

# Ejecutar el proceso de creación de ppt
pptx_ruta = os.path.join("auxiliares/plantillas/plantilla-monitoreo-ensu.pptx")
prs = Presentation(pptx_ruta)

pptx_salida_ruta = os.path.join("salidas/monitoreo-ensu-cdmx" + "-q1-26" +  ".pptx")

# Df valores
df_ruta = os.path.join("datos/datos_procesados/df_ensu_integra_09_etiq.csv")

# Df top

df_top_ruta = os.path.join("datos/datos_procesados/df_top5.csv")

df = pd.read_csv(df_ruta)
df_top = pd.read_csv(df_top_ruta)

### presentación

render_slides_for_ids(
     prs,
     df,
     df_top,
    id_col= "cd",
    start_slide = 1,
    sort_by_id = False,          # orden de slides contra df_main
    # columnas del longtable
    long_score_col = "porcentaje",
    #long_label_col = "problema",
    long_image_col = "icono",
    top_n= 5,
    top_ascending= False,
    img_dir= None)     # si image en df_long es nombre relativo)

prs.save(pptx_salida_ruta)    
    