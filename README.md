# Reporte de problemas ENSU, Ciudad de México

Este proyecto ejecuta un programa que elabora una presentación sobre algunos resultados de la [Encuesta Nacional de Seguridad Pública Urbana (ENSU)](https://www.inegi.org.mx/programas/ensu/#documentacion) y carga la presentación en una carpeta de google drive. Puedes ver un ejemplo finalizado [aquí](https://docs.google.com/presentation/d/18X1CarY2thss_xejGXzYA8d-IzWHnKoQ/edit?usp=sharing&ouid=102821055360325180838&rtpof=true&sd=true)

# Presentación 💡

El objetivo de la presentación es mostrar en un reporte claro y comprensible para personas que quieren conocer:

a. la percepción de inseguridad en donde viven
b. los 5 principales problemas principales que perciben
c. la percepción de efectividad con la que sus gobiernos solucionan esos problemas

## Estructura de la presentación

Se tiene la siguiente estructura en todas las diapositivas con la finalida de que el poducto sea homogéneo y poder reutilizar diversos componentes como iconos y conjuntos de datos.

![alt text](imagenes/diapo_ejemplo.png)


# Estructura del repositorio


├── auxiliares
│   ├── credenciales
│   ├── iconos
│   │   ├── aguas-residuales.png
│   │   ├── ... .png
│   ├── imagenes
│   │   └── image.png
│   └── plantillas
│       └── plantilla-monitoreo-ensu.pptx
├── datos
│   ├── datos_originales
│   └── datos_procesados
├── procesamiento
│   ├── 01_procesa_df.py
│   ├── 02_elabora_ppt.py
│   ├── 03_cargar_ppt.py
│   └── funciones.py
├── README.md
├── requirements.txt
└── salidas

- auxiliares: contiene las carpetas para colocar credenciales .json si se quiere subir la ppt a una carpeta de google drive; carpeta con iconos que se usan en la creación de la PPT, imagenes para el ejemplo del repositorio; plantillas que contiene la plantilla en pptx que utiliza el programa para renderizar cada vez el reporte.
- datos: contiene los datos originales y los datos procesados
- procesamiento: contiene el programa dividido en ejecutables *.py y por separado las funciones
- requirements.txt para levantar un ambiente virtual venv de python
- salidas: guarda la pptx ya renderizada con iconos e información

Los iconos cada uno de ellos tiene derechos de autor citados en la plantilla de la presentación.

## Requerimientos
- [Python (> 12.0)](https://www.python.org/)
- [venv](https://docs.python.org/3/library/venv.html)
- [Presentation](https://python-pptx.readthedocs.io/en/latest/user/presentations.html)  

## Instrucciones de uso

1. Clona el repositorio en el espacio que designes en tu equipo `git clone https://github.com/IsaiasEntropia/reporte-ensu.git`
2. Cambia hacia esa carpeta `cd reporte-ensu`
3. Instala el ambiente virtual

`python3 -m venv .venv`

`source .venv/bin/activate`

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`


4. Carga un csv con los resultados de la ENSU con la siguiente estructura.

![alt text](imagenes/df_ensu.png)

Puedes auxiliarte puedes usar este repositorio de [Entropia](https://github.com/entropiacf/ensu-tabulados)

5. Procesamiento

- `01_procesa_df.py` ejecuta un preprocesamiento de los datos para obtener el top 5 de problemas y dar formato a etiquetas.
- `02_elabora_ppt.py` elabora una presentación con base en la plantilla de las Alcaldías de la Ciudad de México
- `03_cargar_ppt.py` Si lo deseas, puedes cargar la ppt en una carpeta de google drive
- `funciones.py` contiene las funciones como módulos para dar orden y limpieza al proyecto

#### Si quieres cargar la presentación 

Hay al menos dos opciones:

1. Tú o tu organización cuenta con cuenta de gworks puedes generar una unidad compartida e ir por google cloud
2. Tienes la cuenta gratuita y debes realziarlo por medio de una aplicación de google

Caso 1. Puedes generar una cuenta de servicio desde google cloud y generar tus llaves de acceso
Caso 2. (El de este ejemplo) generas una aplicación de escritorio en google cloud y le das permiso a la cuenta desde la que vayas a subir tus archivos como 'tester' para que te permita el acceso a una carpeta de drive. 

Descarga las credenciales en formato *.json y coloca en la ruta `auxiliares/credenciales`, no te preocupes esta carpeta está indicada en el `.gitignore` para que no se suba si modificas algún cambio. Debes tener identificada la carpeta de google drive a la cuál vas a subir tu pptx es algo como https://drive.google.com/drive/u/2/folders/1abcdefg123445 toma la última parte de la cadena y la debes colocar en el archivo .env, te dejo un .env_ejemplo.

# Gracias.