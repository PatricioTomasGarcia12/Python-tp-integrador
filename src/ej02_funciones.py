import csv
from collections import Counter

def imprimir_1ras_10filas(ruta, delimiter = ","):
    with open(ruta, 'r', encoding = "UTF-8") as f_csv:
        csv_reader = csv.DictReader(f_csv, delimiter = delimiter)
        #Imprimir 1ras 10 filas:
        for i, row in enumerate(csv_reader):
            if i == 10:
                break
            else:
                print(row)
def imprimir_columnas(ruta, delimiter = ","):
        with open(ruta, 'r', encoding = "UTF-8") as f_csv:
            csv_reader = csv.DictReader(f_csv, delimiter = delimiter)
            print(csv_reader.fieldnames)

def retornar_indice_columna(ruta, delimiter = ","):
        with open(ruta, 'r', encoding = "UTF-8") as f_csv:
            csv_reader = csv.DictReader(f_csv, delimiter = delimiter)
        #Retornar indice de cada columna:
            for i, field in enumerate(csv_reader.fieldnames):
                print(f"{i}: {field}")

def cant_total_registros(ruta, delimiter = ","):
        with open(ruta, 'r', encoding = "UTF-8") as f_csv:
            csv_reader = csv.DictReader(f_csv, delimiter = delimiter)
            #Retornar cantidad total de registros:
            count = 0
            for row in csv_reader:
                 count +=1
        return count

def columnas_vacias(ruta, delimiter = ","):
     with open(ruta, 'r', encoding = "UTF-8") as f_csv:
        csv_reader = csv.DictReader(f_csv, delimiter = delimiter)
        #Retornar cantidad de columnas vacias:
        lista_columnas_vacias = []
        for row in csv_reader:
            for columna in row:
                if row[columna].strip() == "" or row[columna] is None:
                    if columna not in lista_columnas_vacias:
                        lista_columnas_vacias.append(columna)
     return lista_columnas_vacias

def porcentaje_columnas_nulas(ruta, delimiter = ","):
     with open(ruta, 'r', encoding = "UTF-8") as f_csv:
        csv_reader = csv.DictReader(f_csv, delimiter = delimiter)
        #Retornar porcentaje de columnas nulas:
        conteo = {}
        for row in csv_reader:
            for columna in row:
                if columna not in conteo:
                    conteo[columna] = {"total": 0, "nulos": 0}
                conteo[columna]["total"] += 1
                if row[columna].strip() == "" or row[columna] is None:
                        conteo[columna]["nulos"] += 1
        resultado = {}
        for columna in conteo:
             resultado[columna] = f"{conteo[columna]['nulos'] / conteo[columna]['total'] * 100:.5f}"
     return resultado
        
def dado_nombre_columna(ruta, nombre_columna = "Cualquiera", delimiter = ","):
     with open(ruta, 'r', encoding = "UTF-8") as f_csv:
        csv_reader = csv.DictReader(f_csv, delimiter = delimiter)
        #Dado el nombre de una columna, retornar cantidad de valores distintos:
        if nombre_columna not in csv_reader.fieldnames:
            print("La columna no existe.")
            return
        else:
             valores_distintos = set()
             for row in csv_reader:
                  valores_distintos.add(row[nombre_columna])
             return len(valores_distintos)

def frecuencia_columna(ruta, nombre_columna, delimiter = ","):
     with open(ruta, 'r', encoding = "UTF-8") as f_csv:
        csv_reader = csv.DictReader(f_csv, delimiter = delimiter)
        #Dado el nombre de una columna, retornar frecuencia de cada valor distinto:
        return Counter(row[nombre_columna] for row in csv_reader)