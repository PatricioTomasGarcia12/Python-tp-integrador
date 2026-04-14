import csv

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

def coordenadas_incorrectas(ruta, encoding, separador, nombreLatitud, nombreLongitud):
    with open(ruta, encoding=encoding) as archivo:
        csv_reader = csv.DictReader(archivo, delimiter=separador)
        registros = [row for row in csv_reader if not (validar_latitud(row, nombreLatitud) and validar_longitud(row, nombreLongitud))]
        return len(registros), registros 
