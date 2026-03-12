import pandas as pd
import os
from pathlib import Path


### === Crear el df formato largo para el top 5 === ####
# Leer el csv de datos procesados

# Path al csv
df_ruta = os.path.join("datos/datos_originales/df_ensu_integra_09.csv")
# Path a los iconos

iconos_ruta = os.path.join("auxiliares/iconos/")

df_top = pd.read_csv(df_ruta)

# Eliminar las variables que no necesitamos en el top 
df_long = df_top.copy()
df_long = df_long.drop(columns=["nom_cd",
                                "p_inseg",
                                "p_inseg_cv",
                                "p_inseg_low",
                                "p_inseg_upp",
                                "Muy o algo efectivo",
                                "Poco o nada efectivo",	
                                "periodo"])

# Crear un df con el top 5 de los problemas que queremos mostrar
long_top5 = (
    df_long.melt("cd", var_name="problema", value_name="porcentaje")
          .sort_values(["cd","porcentaje","problema"], ascending=[True, False, True], kind="mergesort")
          .groupby("cd", sort=False).head(5) )

# Redondeamos los valores y agregamos el símbolo de % para las etiquetas
long_top5["porcentaje"] = long_top5["porcentaje"].round(0).astype("int64")
long_top5["porcentaje"] = long_top5["porcentaje"].astype("str") + '%'

# Diccionario  problemas -> iconos

prob_icon = { 
     'alumbrado' : iconos_ruta + 'farola.png',
     'baches' : iconos_ruta + 'bache.png' ,
     'coladeras' : iconos_ruta + 'coladeras.png' ,
     'delincuencia' : iconos_ruta +  'delito.png',
     'drenaje' : iconos_ruta +  'drenaje.png',
     'fallas_agua' : iconos_ruta +  'fallas_agua.png',
     'parque_desc' : iconos_ruta + 'parque.png' ,
     'trafico' : iconos_ruta + 'trafico.png' ,
     'transporte_inef' : iconos_ruta + 'transporte-publico.png' }

# Mapear los iconos
long_top5["icono"] = long_top5["problema"].map(prob_icon)

# Guardar csv de top 5 
long_top5.to_csv(os.path.join("datos/datos_procesados/df_top5.csv"))

### === FIN a crear el df formato largo para el top 5 === ####

# -------------------------------------------------------------------#

### === Crear atributos de etiquetas para el df ancho === ####

# Df valores
df_ruta = os.path.join("datos/datos_originales/df_ensu_integra_09.csv")

df_ensu = pd.read_csv(df_ruta)

# Reondear long top
df_ensu["p_inseg"] = df_ensu["p_inseg"].round(0).astype("int64")
df_ensu["p_inseg"] = df_ensu["p_inseg"].astype("str") + '%'

df_ensu["Muy o algo efectivo"] = df_ensu["Muy o algo efectivo"].round(0).astype("int64")
df_ensu["Muy o algo efectivo"] = df_ensu["Muy o algo efectivo"].astype("str") + '%'

df_ensu["Poco o nada efectivo"] = df_ensu["Poco o nada efectivo"].round(0).astype("int64")
df_ensu["Poco o nada efectivo"] = df_ensu["Poco o nada efectivo"].astype("str") + '%'


# Guardar csv ENSU con etiquetas 
df_ensu.to_csv(os.path.join("datos/datos_procesados/df_ensu_integra_09_etiq.csv"))

### === Fin para crear atributos de etiquetas para el df ancho === ####