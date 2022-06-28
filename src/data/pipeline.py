"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import ingest_data
import transform_data
import clean_data
import compute_daily_prices
import compute_monthly_prices
import luigi
from luigi import Task, LocalTarget


class TareasRealizadasPrograma(Task):
    def output(self):
        return LocalTarget("data_lake/cleansed/precios-horarios.csv")

    def run(self):
        ingest_data.ingest_data()
        transform_data.transform_data()
        clean_data.clean_data()


class Resultados(Task):
    def requires(self):
        return TareasRealizadasPrograma()

    def output(self):
        return LocalTarget(
            [
                "data_lake/business/precios-diarios.csv",
                "data_lake/business/precios-mensuales.csv",
            ]
        )

    def run(self):
        compute_daily_prices.compute_daily_prices()
        compute_monthly_prices.compute_monthly_prices()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    luigi.run(["Resultados", "--local-scheduler"])

