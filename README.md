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
- **`validacion_tipologia_v5.py`**: Script en Python que procesa los datos y genera el archivo de salida.
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

3. **Ejecución**:
   - Coloca el archivo UNIDAD_CONSTRUCCION.csv en la misma carpeta que el script.
   - Ejecuta el script con el siguiente comando:
     
   ```bash
   python validacion_tipologia_v5.py
   
- El archivo de salida UNIDAD_CONSTRUCCION_VALIDADO_FINAL.csv se generará en la misma carpeta.
---

## **Columnas del Archivo de Salida**

- El archivo de salida (UNIDAD_CONSTRUCCION_VALIDADO_FINAL.csv) contiene las siguientes columnas adicionales:
- Tipologia_Digitada: La tipología que el usuario digitó originalmente.
- Tipologia_Recalculada: La tipología correcta según los parámetros.
- Conservacion_Digitada: La conservación que el usuario seleccionó.
- Conservacion_Calculada: La conservación correcta según los parámetros.
- Puntaje_Calculado: El puntaje correcto según los parámetros.
- Validacion: True si el puntaje calculado coincide con el original, False si no coincide.
- Puntos_Digitados: Copia exacta de la columna Puntos.

---

## **Ejemplo de Uso**

Entrada:
- Archivo UNIDAD_CONSTRUCCION.csv con las siguientes columnas:
- Tipificacion: Tipología seleccionada por el usuario (ejemplo: 2A).
- Puntos: Puntaje asignado por el usuario (ejemplo: 14).
- Anio Construccion: Año de construcción de la unidad (ejemplo: 2010).

Salida:
Archivo UNIDAD_CONSTRUCCION_VALIDADO_FINAL.csv con las columnas adicionales mencionadas anteriormente.

---

## **Contribuciones**

Si deseas contribuir a este proyecto, ¡eres bienvenido! Puedes:

Reportar errores o sugerir mejoras abriendo un issue.

Enviar un pull request con tus cambios.

---

## **Licencia**

Este proyecto está bajo la licencia MIT. Si usas este código, por favor, menciona este repositorio.

---

## **Contacto**

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Nombre: Alexander Arroyave Zapata

Email: aarroyavez@unal.edu.co

GitHub: https://github.com/aarroyavez

---

¡Gracias por usar este proyecto! 😊





