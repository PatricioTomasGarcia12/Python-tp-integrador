import csv
import pycountry
from collections import Counter



def campo_vacio(linea, campo):
    return linea[campo].strip() == ""

def validar_latitud(linea, campo):
    if campo_vacio(linea, campo):
        return False
    try:
        latitud = float(linea[campo])
    except ValueError:
        return False
    return  -90 <= latitud <= 90

def validar_longitud(linea, campo):
    if campo_vacio(linea, campo):
        return False
    try:
        longitud = float(linea[campo])
    except ValueError:
        return False
    return  -180 <= longitud <= 180

def solo_existe_longitud(linea, nombreLatitud, nombreLongitud):
    return campo_vacio(linea, nombreLatitud) and not campo_vacio(linea, nombreLongitud) 

def solo_existe_latitud(linea, nombreLatitud, nombreLongitud):
    return campo_vacio(linea, nombreLongitud) and not campo_vacio(linea, nombreLatitud)

def solo_latitud_o_longitud(linea, nombreLatitud, nombreLongitud):
    return solo_existe_latitud(linea, nombreLatitud, nombreLongitud) ^ solo_existe_longitud(linea, nombreLatitud, nombreLongitud)



def coordenadas_incorrectas(ruta, encoding, separador, nombreLatitud, nombreLongitud):
    with open(ruta, encoding=encoding) as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=separador)
        registros = [row for row in csv_reader if not (validar_latitud(row, nombreLatitud) and validar_longitud(row, nombreLongitud))]
        return len(registros), registros 


def registros_duplicados (ruta, encoding, separador, nombre_id):
    with open(ruta, encoding=encoding) as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=separador)
        contador = Counter(row[nombre_id] for row in csv_reader)
        repetidos = {k: v for k, v in contador.items() if v > 1}
        cantidad = sum(v - 1 for v in repetidos.values())
        return cantidad, repetidos


def valores_no_permitidos (ruta, encoding, separador):
    country_codes = {country.alpha_2 for country in pycountry.countries}
    invalidos = []
    with open(ruta, encoding=encoding) as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=separador)
        for i, row in enumerate(csv_reader, start=2):
            codigo = row.get("countryCode").strip().upper()
            if codigo not in country_codes:
                invalidos.append(codigo)
        return invalidos
    
            
def coordenada_incertidumbre(ruta, encoding, separador, nombreCampo="coordinateUncertaintyInMeters", maximo=100):
    registros_invalidos = []
    with open(ruta, encoding=encoding) as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=separador)
        for i, row in enumerate(csv_reader, start=2):
            valor_crudo = row.get(nombreCampo, "").strip()
            try:
                valor = float(valor_crudo)
            except ValueError:
                registros_invalidos.append({"linea": i, "motivo": "no_numerico", "valor": valor_crudo, "registro": row})
                continue
            if valor < 0:
                registros_invalidos.append({"linea": i, "motivo": "negativo", "valor": valor, "registro": row})
            elif valor > maximo:
                registros_invalidos.append({"linea": i, "motivo": "excesivo", "valor": valor, "registro": row})
    return len(registros_invalidos), registros_invalidos

