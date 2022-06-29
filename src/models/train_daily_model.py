def load_data():

    import pandas as pd
    data = pd.read_csv('data_lake/business/features/precios-diarios.csv', sep=",")

    return data


def data_preparation(data):
    import pandas as pd
    df = data.copy()
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d')
    df['year'], df['month'], df['day'] = df['Fecha'].dt.year, df['Fecha'].dt.month, df['Fecha'].dt.day

    y = df["precio"]
    x = df.copy()
    x.pop("precio")
    x.pop("Fecha")
    return x, y


def make_train_test_split(X, y):

    from sklearn.model_selection import train_test_split

    (x_train, x_test, y_train, y_test) = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=12345,
    )
    return x_train, x_test, y_train, y_test


def train_model(x_train, x_test):
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestRegressor

    # Se Define el algoritmo a utilizar
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    # Se establece el Modelo
    model_RF = RandomForestRegressor(n_jobs=-1)

    return model_RF


def save_model(model_RF):

    import pickle

    with open("src/models/precios-diarios.pickle", "wb") as file:
        pickle.dump(model_RF, file,  pickle.HIGHEST_PROTOCOL)


def train_daily_model():

    data = load_data()
    x, y = data_preparation(data)
    x_train, x_test, y_train, y_test = make_train_test_split(x, y)
    model_RF = train_model(x_train, x_test)
    save_model(model_RF)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()