GAS = [i * 100 for i in range(240, 300)]
NUM_RENGLONES = 15
NUM_COLUMNAS = 4

def obtener_indice_unidimensional(renglon, columna):
    return (NUM_COLUMNAS * renglon) + columna

# a) Gasto de producción del departamento de marketing en el mes de noviembre
renglon_noviembre = 10
columna_marketing = 2
indice_marketing_noviembre = obtener_indice_unidimensional(renglon_noviembre, columna_marketing)
gasto_marketing_noviembre = GAS[indice_marketing_noviembre]
print(f"Gasto del departamamento de marketing en noviembre: ${gasto_marketing_noviembre}")

# b) Gasto de producción anual del departamento de contabilidad
columna_contabilidad = 1
gasto_anual_contabilidad = sum(GAS[obtener_indice_unidimensional(renglon, columna_contabilidad)] for renglon in range(NUM_RENGLONES))
print(f"Gasto anual del departamento de contabilidad: ${gasto_anual_contabilidad}")

# c) Gasto total de producción de los cuatro departamentos en el mes de diciembre
renglon_diciembre = 11
gasto_diciembre_total = sum(GAS[obtener_indice_unidimensional(renglon_diciembre, columna)] for columna in range(NUM_COLUMNAS))
print(f"Gasto total en diciembre: ${gasto_diciembre_total}")
