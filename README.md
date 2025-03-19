# Procesamiento de Datos de Unidades de Construcción

Este repositorio contiene un script en Python para procesar y validar datos de unidades de construcción a partir de un archivo CSV (`UNIDAD_CONSTRUCCION.csv`). El código realiza cálculos y validaciones basados en las columnas `Tipificacion`, `Puntos`, y `Anio Construccion`.

---

## **Descripción del Proyecto**

El objetivo de este proyecto es:
1. **Recalcular la tipología** de las unidades de construcción basándose en los parámetros proporcionados.
2. **Validar la conservación** y el **puntaje** asignado por el usuario.
3. Generar un archivo CSV con los resultados, incluyendo columnas adicionales para la tipología recalculada, la conservación calculada, el puntaje calculado y la validación.

---

## **Estructura del Repositorio**

- **`UNIDAD_CONSTRUCCION.csv`**: Archivo CSV de entrada que contiene los datos de las unidades de construcción.
- **`validacion_tipologias_v5.py`**: Script en Python que procesa los datos y genera el archivo de salida.
- **`UNIDAD_CONSTRUCCION_VALIDADO_FINAL.csv`**: Archivo CSV de salida con los resultados del procesamiento.
- **`README.md`**: Este archivo, que explica el proyecto.

---

## **Cómo Funciona el Código**

El script realiza los siguientes pasos:

1. **Carga el archivo CSV** y prepara los datos:
   - Convierte la columna `Tipificacion` a tipo string y maneja valores nulos.
   - Obtiene el año actual para calcular la antigüedad de las construcciones.

2. **Calcula la tipología digitada por el usuario**:
   - Basándose en la `Tipificacion` y los `Puntos`, determina la tipología que el usuario seleccionó.

3. **Recalcula la tipología correcta**:
   - Usa la `Tipificacion` y los `Puntos` para determinar lo que **debería ser** la tipología.

4. **Calcula la conservación digitada por el usuario**:
   - Basándose en la `Tipologia_Digitada` y los `Puntos`, determina la conservación que el usuario seleccionó.

5. **Calcula la conservación correcta**:
   - Usa la `Tipologia_Recalculada` y el `Anio Construccion` para determinar la conservación correcta.

6. **Calcula el puntaje correcto**:
   - Usa la `Tipologia_Recalculada` y la `Conservacion_Calculada` para determinar el puntaje correcto.

7. **Valida el puntaje**:
   - Compara el puntaje calculado con el puntaje original (`Puntos`) para identificar discrepancias.

8. **Genera un archivo CSV de salida**:
   - Guarda los resultados en un nuevo archivo CSV (`UNIDAD_CONSTRUCCION_VALIDADO_FINAL.csv`).

---

## **Cómo Ejecutar el Código**

1. **Requisitos**:
   - Python 3.x instalado.
   - Librerías de Python: `pandas`.

2. **Instalación de dependencias**:
   Si no tienes instalada la librería `pandas`, puedes instalarla con el siguiente comando:
   ```bash
   pip install pandas
