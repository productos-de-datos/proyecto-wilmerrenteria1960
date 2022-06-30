"""
This funtion downloads the information and save it in the same format obtained.
"""
# pylint: disable=consider-using-f-string
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with
# pylint: disable=line-too-long

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.
    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.
    """
from urllib import request

#Años a descargar
anioDescargar = list(range(1995,2022))

for anio in anioDescargar:
    if anio in [2016, 2017]:
        f = open(f"data_lake/landing/{anio}.xls", "wb")
        f.write(
            request.urlopen(
                f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{anio}.xls"
            ).read()
        )
        f.close()
    else:
        f = open(f"data_lake/landing/{anio}.xlsx", "wb")
        f.write(
            request.urlopen(
                f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{anio}.xlsx"
            ).read()
        )
        f.close()

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
