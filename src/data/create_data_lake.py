"""
    Funcion crea el directorio correspondiente
"""
# pylint: disable=import-outside-toplevel


import os

def create_data_lake():
    """
    Cree el data lake con sus capas.
    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:
        ```
        .
        |
        ___data_lake/
            |___ landing/
            |___raw/
            |___cleansed/
            ___ business/
                |___ reports/
                |    |___ figures/
                |___ features/
                |___ forecasts/
        ```
    """
    folders = [
        "landing",
        "raw",
        "cleansed",
        "business",
        "business/reports",
        "business/reports/figures",
        "business/features",
        "business/forecasts",
    ]
    # Se crea la carpeta padre 
    os.mkdir("data_lake")

    # Se crea cada una de las tareas
    for folder in folders:
        os.mkdir(os.path.join("data_lake", folder))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    create_data_lake()