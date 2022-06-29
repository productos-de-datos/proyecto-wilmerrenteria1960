
def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.
    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.
    >>> make_monthly_prices_plot()
    """
    import pandas as pd
    import matplotlib.pyplot as plt

    datos = pd.read_csv("data_lake/business/precios-mensuales.csv", index_col=None, sep=',', header=0)
    datos["Fecha"] = pd.to_datetime(datos["Fecha"])
    x = datos.Fecha
    y = datos.precio

    plt.figure(figsize=(15, 5))
    plt.plot(x, y, 'b', label='Precios promedios mensuales')
    plt.title('Precios promedios mensuales')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation="vertical")
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()
    doctest.testmod()
