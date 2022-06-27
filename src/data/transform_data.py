def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import os
    import pandas as pd
    import subprocess


    subprocess.call(["pip", "install", "openpyxl"])
    subprocess.call(["pip", "install", "xlrd"])


    archivoslanding = []
    for files in os.listdir("data_lake/landing/"):
        if files.endswith(".xls") or files.endswith(".xlsx"):
            archivoslanding.append("data_lake/landing/" + files)

    print (archivoslanding)

    for archivo in archivoslanding:
        df = pd.read_excel(archivo,index_col=None, header=None)
        indexDF = df.index[df.iloc[:, 0] == 'Fecha'].tolist()
        dffinal = df.iloc[indexDF[0]+1:,0:25]
        dffinal.columns = ["Fecha","H00","H01","H02","H03","H04","H05","H06","H07","H08","H09","H10","H11","H12","H13","H14","H15","H16","H17","H18","H19","H20","H21","H22","H23"]
        dffinal['Fecha'] =  dffinal[['Fecha']].apply(pd.to_datetime)
        dffinal['Fecha'] = dffinal['Fecha'].dt.date
        nombreExtension = archivo.split("/")[-1]
        nombreCSV = nombreExtension.split(".")[0] + ".csv"
        df.to_csv("data_lake/raw/" + nombreCSV, index=False)

    #raise NotImplementedError("Implementar esta función")

 
if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
    
    