"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re


def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = pd.DataFrame(df)   
    df = df.applymap(lambda s:s.lower() if type(s) == str else s)
    df[['barrio', 'idea_negocio', 'línea_credito']] = df[['barrio', 'idea_negocio', 'línea_credito']].replace(['_', '-'], ' ', regex=True)
    df = df.dropna()
    df = df.drop(df.columns[0], axis=1)
    patron =r'\d{4}'
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: '/'.join(x.split('/')[::-1]) if re.match(patron, x) else x)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio']).dt.strftime('%d/%m/%Y')
   # df['barrio'] = df['barrio'].str.replace('bel¿n', 'belen').str.replace('antonio nari¿o', 'antonio nariño').str.replace('san jose de la cima no. ', 'san jose de la cima no.').str.replace('el salado ', 'el salado')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '').str.replace('.00', '').str.replace(',', '').astype(int)
    df = df.drop_duplicates()
    return df
