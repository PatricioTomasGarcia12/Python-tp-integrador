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
     
def analizar_columna(ruta, nombre_columna, tipo, delimiter=","):
    with open(ruta, 'r', encoding="utf-8") as f_csv:
        reader = csv.DictReader(f_csv, delimiter=delimiter)
        
        # Verifica si la columna existe
        if nombre_columna not in reader.fieldnames:
            print("La columna no existe")
            return
        
        valores = []
        
        for row in reader:
            valor = row[nombre_columna]
            
            # ignorar vacíos
            if valor is None or valor.strip() == "":
                continue
            # agrega a la lista
            valores.append(valor)
        
        if len(valores) == 0:
            print("No hay valores válidos en esa columna")
            return
        
        #si es tipo numerico
        if tipo == "numeric":
         nums = []
    
         for v in valores:
             try:
                num = float(v)
                nums.append(num)
             except:
               continue
         
         if len(nums) == 0:
             print("No hay valores numéricos válidos en la columna")
             return
    
         return min(nums), max(nums), sum(nums)/len(nums)
        


        #si es tipo cordinate
        elif tipo == "coordinate":
            nums = [float(v) for v in valores]
            return min(nums), max(nums)
        
        #si es tipo texto
        elif tipo == "text":
            largos = [len(v) for v in valores]
            return min(largos), max(largos)
        
        else:
            print("tipo no válido")




def columnas_totalmente_vacias(ruta, delimiter=","):
    with open(ruta, 'r', encoding="utf-8") as f_csv:
        reader = csv.DictReader(f_csv, delimiter=delimiter)
        columnas = reader.fieldnames
        
        #primeroasume que son todas vacias
        vacias = {col: True for col in columnas}
        for row in reader:
            for col in columnas:
                valor = row[col]

                if valor is not None and valor.strip() != "":
                    #saca las que no son vacias
                    vacias[col] = False
        
        resultado = []
        for col in vacias:
            if vacias[col]:
                resultado.append(col) 
        return resultado