import pandas as pd
from geopy.geocoders import Nominatim
import time

df = pd.read_csv(r"D:\Users\Admin\Downloads\bd\BackUp\TrabajoMauri.csv", encoding="latin-1", sep=";")

geolocator = Nominatim(user_agent="my_geocoder", timeout=5)

#Obtengo la latidud y longitud mediante los datos que existan en la bbdd, en caso de un campo estar vacío,
#se tendra en cuenta el otro campo unicamente.

def obtener_latitud_longitud(direccion, localidad, provincia):
    if pd.isnull(localidad) and pd.isnull(provincia):
        ubicacion = direccion
    elif pd.isnull(localidad):
        ubicacion = f"{direccion}, {provincia}"
    elif pd.isnull(provincia):
        ubicacion = f"{direccion}, {localidad}"
    else:
        ubicacion = f"{direccion}, {localidad}, {provincia}"
    
    location = geolocator.geocode(ubicacion)
    if location:
        return round(location.latitude, 6), round(location.longitude, 6)
    else:
        return None, None

#Agrego las coordenadas al df.
for index, row in df.iterrows():
    latitud, longitud = obtener_latitud_longitud(row['Direccion'], row['Localidad'], row['Provincia'])
    df.at[index, 'Latitud'] = latitud
    df.at[index, 'Longitud'] = longitud
    
    time.sleep(2)

