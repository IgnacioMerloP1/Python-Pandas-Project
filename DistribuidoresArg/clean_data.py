import pandas as pd

df = pd.read_csv(r'D:\Users\Admin\Downloads\bd\nueva bd.csv', encoding='latin-1', delimiter=',')

if 'suc - loc' in df.columns: #Si la columna 'suc - loc' existe, la elimino del df.
    df.drop(columns=['suc - loc'], inplace=True)

columna_clave = 'Suc-Loc'

columnas_combinar = ['Sucursal','Direccion','Localidad','Provincia','Telefono', 'Email', 'Marca']
df[columnas_combinar] = df[columnas_combinar].fillna(value='')

df_combinado = pd.DataFrame(columns=[columna_clave] + columnas_combinar)


#Itero a través de los valores únicos en la columna 'Suc-Loc' del DataFrame original df.
#Para cada valor único en 'Suc-Loc', creo un grupo que contiene todas las filas con ese valor en 'Suc-Loc'.
for valor_clave in df[columna_clave].unique():
    grupo = df[df[columna_clave] == valor_clave]
    
    registro_combinado = grupo[columnas_combinar].agg(', '.join)
    registro_combinado[columna_clave] = valor_clave
    df_combinado = df_combinado.append(registro_combinado, ignore_index=True)

#df.to_csv(r'D:\Users\Admin\Downloads\bd\FINAL.csv', encoding='latin-1', sep=';')