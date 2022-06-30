def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd

    df = pd.read_csv("data_lake/cleansed/precios-horarios.csv")
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    df = df.set_index("Fecha").resample("M")["precio"].mean()
    df.to_csv("data_lake/business/precios-mensuales.csv", index=True)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
