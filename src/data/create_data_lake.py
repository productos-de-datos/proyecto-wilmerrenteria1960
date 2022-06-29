def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    import os
    os.mkdir('./data_lake/')

    folders = ['landing', 'raw', 'cleansed', 'business','business/reports','business/reports/figures','business/features','business/forecasts']


    for folder in folders:
        path = os.path.join('data_lake', folder)
        os.mkdir(path)
        print("Directory '%s' created" %folder)




if __name__ == "__main__":
    import doctest

    doctest.testmod()
    create_data_lake()
