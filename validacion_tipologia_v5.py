## ESTE CODIGO ESTA TOTALMENTE FUNCIONAL ###

import pandas as pd
from datetime import datetime

# Cargar el archivo CSV
df = pd.read_csv('UNIDAD_CONSTRUCCION.csv', encoding='latin1')

# Convertir la columna 'Tipificacion' a tipo str y manejar NaN
df['Tipificacion'] = df['Tipificacion'].astype(str).fillna('DESCONOCIDA')

# Obtener el año actual
current_year = datetime.now().year

# Función para obtener la tipología digitada por el usuario
def tipologia_digitada(tipificacion, puntos):
    if pd.isna(tipificacion) or tipificacion in ['nan', 'DESCONOCIDA']:
        return 'DESCONOCIDA'
    
    # Extraer el número de la tipificación
    numero = tipificacion[0]  # Primera parte (1, 2, 3, etc.)
    letra = tipificacion[-1] if len(tipificacion) > 1 else ''  # Letra (A, B)

    # Determinar la tipología digitada basada en la Tipificacion y los Puntos
    if numero == '1':
        if puntos in [6, 7]:
            return '1A'
        elif puntos in [8, 9, 10]:
            return '1B'
    elif numero == '2':
        if puntos in [11, 14, 17, 19]:
            return '2A'
        elif puntos in [20, 22, 25, 28]:
            return '2B'
    elif numero == '3':
        if puntos in [29, 32, 33, 36]:
            return '3A'
        elif puntos in [37, 40, 43, 46]:
            return '3B'
    elif numero == '4':
        if puntos in [47, 49, 52, 55]:
            return '4A'
        elif puntos in [56, 58, 62, 64]:
            return '4B'
    elif numero == '5':
        if puntos in [0]:  # Ajustar según sea necesario
            return '5A'
        elif puntos in [0]:  # Ajustar según sea necesario
            return '5B'
    elif numero == '6':
        if puntos in [0]:  # Ajustar según sea necesario
            return '6A'
        elif puntos in [0]:  # Ajustar según sea necesario
            return '6B'
    
    return 'DESCONOCIDA'

# Aplicar la función para obtener la tipología digitada por el usuario
df['Tipologia_Digitada'] = df.apply(lambda row: tipologia_digitada(row['Tipificacion'], row['Puntos']), axis=1)

# Función para recalcular la tipología (lo que debería ser)
def recalcular_tipologia(tipificacion, puntos):
    if pd.isna(tipificacion) or tipificacion in ['nan', 'DESCONOCIDA']:
        return 'DESCONOCIDA'
    
    # Extraer el número de la tipificación
    numero = tipificacion[0]  # Primera parte (1, 2, 3, etc.)
    letra = tipificacion[-1] if len(tipificacion) > 1 else ''  # Letra (A, B)

    # Determinar la tipología recalculada basada en la Tipificacion y los Puntos
    if numero == '1':
        if puntos in [6, 7]:
            return '1A'
        elif puntos in [8, 9, 10]:
            return '1B'
    elif numero == '2':
        if puntos in [11, 14, 17, 19]:
            return '2A'
        elif puntos in [20, 22, 25, 28]:
            return '2B'
    elif numero == '3':
        if puntos in [29, 32, 33, 36]:
            return '3A'
        elif puntos in [37, 40, 43, 46]:
            return '3B'
    elif numero == '4':
        if puntos in [47, 49, 52, 55]:
            return '4A'
        elif puntos in [56, 58, 62, 64]:
            return '4B'
    elif numero == '5':
        if puntos in [0]:  # Ajustar según sea necesario
            return '5A'
        elif puntos in [0]:  # Ajustar según sea necesario
            return '5B'
    elif numero == '6':
        if puntos in [0]:  # Ajustar según sea necesario
            return '6A'
        elif puntos in [0]:  # Ajustar según sea necesario
            return '6B'
    
    return 'DESCONOCIDA'

# Aplicar la función para obtener la tipología recalculada
df['Tipologia_Recalculada'] = df.apply(lambda row: recalcular_tipologia(row['Tipificacion'], row['Puntos']), axis=1)

# Función para obtener la conservación digitada por el usuario
def conservacion_digitada(tipologia_digitada, puntos):
    if pd.isna(tipologia_digitada) or tipologia_digitada in ['nan', 'DESCONOCIDA']:
        return 'DESCONOCIDA'
    
    # Determinar la conservación digitada basada en la Tipologia_Digitada y los Puntos
    if tipologia_digitada == '1A':
        if puntos in [6, 7]:
            return 'MALA' if puntos == 6 else 'REGULAR' if puntos == 6 else 'BUENA' if puntos == 7 else 'EXCELENTE'
    elif tipologia_digitada == '1B':
        if puntos in [8, 9, 10]:
            return 'MALA' if puntos == 8 else 'REGULAR' if puntos == 9 else 'BUENA' if puntos == 9 else 'EXCELENTE'
    elif tipologia_digitada == '2A':
        if puntos in [11, 14]:
            return 'MALA' if puntos == 11 else 'REGULAR'
    elif tipologia_digitada == '2B':
        if puntos in [20, 22]:
            return 'MALA' if puntos == 20 else 'REGULAR'
    elif tipologia_digitada == '3A':
        if puntos in [29, 32, 33]:
            return 'MALA' if puntos == 29 else 'REGULAR' if puntos == 32 else 'BUENA'
    elif tipologia_digitada == '3B':
        if puntos in [37, 40, 43]:
            return 'MALA' if puntos == 37 else 'REGULAR' if puntos == 40 else 'BUENA'
    elif tipologia_digitada == '4A':
        if puntos in [47, 49, 52]:
            return 'MALA' if puntos == 47 else 'REGULAR' if puntos == 49 else 'BUENA'
    elif tipologia_digitada == '4B':
        if puntos in [56, 58, 62]:
            return 'MALA' if puntos == 56 else 'REGULAR' if puntos == 58 else 'BUENA'
    elif tipologia_digitada == '5A':
        if puntos in [0]:  # Ajustar según sea necesario
            return 'REGULAR'
    elif tipologia_digitada == '5B':
        if puntos in [0]:  # Ajustar según sea necesario
            return 'REGULAR'
    elif tipologia_digitada == '6A':
        if puntos in [0]:  # Ajustar según sea necesario
            return 'BUENA'
    elif tipologia_digitada == '6B':
        if puntos in [0]:  # Ajustar según sea necesario
            return 'BUENA'
    
    return 'DESCONOCIDA'

# Aplicar la función para obtener la conservación digitada por el usuario
df['Conservacion_Digitada'] = df.apply(lambda row: conservacion_digitada(row['Tipologia_Digitada'], row['Puntos']), axis=1)

# Función para calcular la conservación (recalculada)
def calcular_conservacion(tipologia_recalculada, anio_construccion):
    if not isinstance(anio_construccion, (int, float)) or pd.isna(anio_construccion):
        return 'DESCONOCIDA'
    
    antiguedad = current_year - int(anio_construccion)
    
    if tipologia_recalculada.startswith('1'):
        return 'MALA'
    elif tipologia_recalculada.startswith('2'):
        return 'MALA' if antiguedad >= 15 else 'REGULAR'
    elif tipologia_recalculada.startswith('3'):
        return 'MALA' if antiguedad >= 20 else 'REGULAR' if antiguedad >= 10 else 'BUENA'
    elif tipologia_recalculada.startswith('4'):
        return 'MALA' if antiguedad > 25 else 'REGULAR' if antiguedad >= 15 else 'BUENA'
    elif tipologia_recalculada.startswith('5'):
        return 'REGULAR' if antiguedad >= 20 else 'BUENA' if antiguedad >= 5 else 'EXCELENTE'
    elif tipologia_recalculada.startswith('6'):
        return 'BUENA' if 10 <= antiguedad <= 30 else 'EXCELENTE'
    else:
        return 'DESCONOCIDA'

# Aplicar la función para obtener la conservación calculada
df['Conservacion_Calculada'] = df.apply(lambda row: calcular_conservacion(row['Tipologia_Recalculada'], row['Anio Construccion']), axis=1)

# Función para calcular el puntaje con base en la tipología recalculada y la conservación
def calcular_puntaje(tipologia_recalculada, conservacion):
    if tipologia_recalculada in ['nan', 'DESCONOCIDA'] or pd.isna(conservacion):
        return None

    # Tabla de puntajes inamovible
    puntajes = {
        '1A': {'MALA': 6, 'REGULAR': 6, 'BUENA': 7, 'EXCELENTE': 7},
        '1B': {'MALA': 8, 'REGULAR': 9, 'BUENA': 9, 'EXCELENTE': 10},
        '2A': {'MALA': 11, 'REGULAR': 14},
        '2B': {'MALA': 20, 'REGULAR': 22},
        '3A': {'MALA': 29, 'REGULAR': 32, 'BUENA': 33},
        '3B': {'MALA': 37, 'REGULAR': 40, 'BUENA': 43},
        '4A': {'MALA': 47, 'REGULAR': 49, 'BUENA': 52},
        '4B': {'MALA': 56, 'REGULAR': 58, 'BUENA': 62},
        # Tipologías 5 y 6 no tienen puntajes definidos en la tabla proporcionada
        '5A': {'REGULAR': None, 'BUENA': None, 'EXCELENTE': None},
        '5B': {'REGULAR': None, 'BUENA': None, 'EXCELENTE': None},
        '6A': {'BUENA': None, 'EXCELENTE': None},
        '6B': {'BUENA': None, 'EXCELENTE': None}
    }

    # Obtener el puntaje según la tipología y conservación
    return puntajes.get(tipologia_recalculada, {}).get(conservacion, None)

# Aplicar la función para obtener el puntaje calculado
df['Puntaje_Calculado'] = df.apply(lambda row: calcular_puntaje(row['Tipologia_Recalculada'], row['Conservacion_Calculada']), axis=1)

# Validación del puntaje con la columna original "Puntos"
df['Validacion'] = df['Puntaje_Calculado'] == df['Puntos']

# Copiar la columna "Puntos" tal como está
df['Puntos_Digitados'] = df['Puntos']

# Guardar el resultado
df.to_csv('UNIDAD_CONSTRUCCION_VALIDADO_FINAL_2.csv', index=False)

print("Cálculo finalizado. Revisa el archivo 'UNIDAD_CONSTRUCCION_VALIDADO_FINAL_2.csv'.")