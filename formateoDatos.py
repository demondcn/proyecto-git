import pandas as pd

# Paso 1: Cargar el archivo CSV como texto (sin encabezado explícito)
df = pd.read_csv("clean_df_123.csv", header=None)

# Paso 2: Separar usando punto y coma
df = df[0].str.split(";", expand=True)

# Paso 3: Asignar encabezado desde la primera fila
df.columns = df.iloc[0].str.strip()  # Usar primera fila como encabezado y quitar espacios
df = df[1:]  # Quitar fila de encabezado

# Paso 4: Eliminar filas con EDAD o GENERO vacíos
df = df[(df['EDAD'].str.strip() != '') & (df['GENERO'].str.strip() != '')]

# Paso 5: Eliminar filas con **cualquier** columna vacía
df = df.dropna(how='any')  # Elimina filas con al menos un valor NaN
df = df[(df != '').all(axis=1)]  # También elimina filas con campos vacíos ('') como string

# Paso 6: Eliminar columna 'CODIGO_LOCALIDAD' si existe
if 'CODIGO_LOCALIDAD' in df.columns:
    df = df.drop(columns=['CODIGO_LOCALIDAD'])

# Paso 7: Guardar el archivo limpio
df.to_csv("archivo_limpio.csv", index=False)

print("✅ Archivo limpio guardado como 'archivo_limpio.csv'")
