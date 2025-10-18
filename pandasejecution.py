import pandas as pd

# Cargar archivo (ajusta nombre si es distinto)
df = pd.read_csv("clean_df_123.csv", header=None)

# Separar columnas por coma
df = df[0].str.split(";", expand=True)

# Asignar encabezado desde la primera fila
df.columns = df.iloc[0]
df = df[1:]

# 💡 Mostrar nombres de columnas
print("Nombres reales de las columnas:")
print(df.columns.tolist())

# Aquí nos detenemos para revisar
exit()
