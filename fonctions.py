import pandas as pd
import matplotlib.pyplot as plt
import requests
import statsmodels.api as sm
from urllib.parse import urlencode


# A function that transforms a call of the api into a usable panda file 
def call_api(api_url):
    req = requests.get(api_url)
    wb = req.json()
    print(wb.keys())

    df = pd.DataFrame(wb['results'])
    return(df)

#Cette fonction mange directement le lien que sort l'interface de l'api donc pas besoin de le modifier, elle rend un panda directement
#Il sert à obtenir des tableaux plus grands sans la limite de 100 (bien mettre limit=-1 dans le lien)

def creer_url_api(colonnes, limit=-1):
    """
    Crée une URL de requête pour sélectionner les colonnes demandées.
    """
    if not colonnes:
        raise ValueError("La liste des colonnes ne peut pas être vide.")

    parametres = {
        "select": ",".join(colonnes),
        "limit": limit
    }

    base_url = (
        "https://equipements.sports.gouv.fr/"
        "api/explore/v2.1/catalog/datasets/data-es/records"
    )

    return f"{base_url}?{urlencode(parametres)}"

def call_csv(url):
    csv_url = url.replace("records", "exports/csv")

    response = requests.get(csv_url)

    if response.status_code != 200:
        raise RuntimeError(
            f"Erreur lors de la récupération du CSV "
            f"(HTTP {response.status_code}) :\n{response.text}"
        )

    with open("equipements_ile_de_france.csv", "wb") as f:
        f.write(response.content)

    return pd.read_csv(
        "equipements_ile_de_france.csv",
        delimiter=";"
    )

def regression(x, y):
    x_reg = sm.add_constant(x)
    y_reg = y.values.ravel()
    return(sm.OLS(y_reg, x_reg).fit(cov_type='HC0'))

from sklearn.linear_model import LinearRegression
import sklearn.metrics 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns

#Une fonction pour faire de la prédiction inspirée pour la forme du projet : 
#"Analyse du réseau ferré de la SNCF: Comment expliquer les retards permanents de la compagnie française ?" 
# sur le site de M. Lino Galiana

def prediction(x, y, afficher = True):
    #séparation des données en 2 échantillon 
    #X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=1)
    X_train, X_test, y_train, y_test = x,x,y,y

    #régression et prédiction
    ols = LinearRegression().fit(X_train, y_train)
    y_pred = ols.predict(X_test)
    
    #calcul des métriques
    rmse = sklearn.metrics.mean_squared_error(y_test, y_pred)
    rsq = sklearn.metrics.r2_score(y_test, y_pred) 
    
    #nuage de points des valeurs observées
    tempdf = pd.DataFrame({"prediction": y_pred, "observed": y_test,
                           "error": y_test - y_pred})
    
    if afficher == True : 
        print("intercept : ",ols.intercept_)
        print("coeffs : ", ols.coef_)
        print("rsq : ", rsq)
        print("rmse : ", rmse)

        fig = plt.figure()
        g = sns.scatterplot(data = tempdf, x = "observed", y = "error")
        g.axhline(0, color = "red")

    return tempdf