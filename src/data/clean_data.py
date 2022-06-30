import os
import pandas as pd
    

def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """

    archivosraw = []

    for files in os.listdir("data_lake/raw/"):
        if files.endswith(".csv"):
            archivosraw.append("data_lake/raw/" + files)

    df_resultado = pd.DataFrame(columns = ['Fecha','hora','precio'])

    for archivo in archivosraw:
        df = pd.read_csv(archivo) 
        df_melt = pd.melt(df, id_vars=['Fecha'], value_vars=df.columns[1:], var_name='hora', value_name='precio')
        df_resultado = pd.concat([df_resultado,df_melt], axis=0)

    df_resultado = df_resultado[df_resultado["Fecha"].notnull()]
    df_resultado.columns = ['Fecha', 'hora', 'precio']
    df_resultado.to_csv("data_lake/cleansed/precios-horarios.csv",index=False)

def test_ResultColumns():
    read_file = pd.read_csv(
                'data_lake/cleansed/precios-horarios.csv')
    assert ["Fecha","Hora","Precio"] == list(read_file.columns.values)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
