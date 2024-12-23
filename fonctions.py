import pandas as pd
import matplotlib.pyplot as plt
import requests
import statsmodels.api as sm


# A function that transforms a call of the api into a usable panda file 
def call_api(api_url):
    req = requests.get(api_url)
    wb = req.json()
    print(wb.keys())

    df = pd.DataFrame(wb['results'])
    return(df)

#Cette fonction mange directement le lien que sort l'interface de l'api donc pas besoin de le modifier, elle rend un panda directement
#Il sert à obtenir des tableaux plus grands sans la limite de 100 (bien mettre limit=-1 dans le lien)

def call_csv(url):

    url = url.replace("records", "exports/csv")
    # Send a GET request to the URL
    response = requests.get(url)

# Ensure the request was successful (status code 200)
    if response.status_code == 200:
    # Save the content to a file
        with open('equipements_ile_de_france.csv', 'wb') as f:
            f.write(response.content)

    # Load the CSV into a pandas DataFrame
        df = pd.read_csv('equipements_ile_de_france.csv', delimiter=';')

    # Display the first few rows of the DataFrame
    else:
        print(f"Failed to retrieve CSV. Status code: {response.status_code}")
    return(df)

def regression(x, y):
    x_reg = sm.add_constant(x)
    y_reg = y.values.ravel()
    return(sm.OLS(y_reg, x_reg).fit(cov_type='HC0'))

import sklearn.metrics 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns

#Une fonction pour faire de la prédiction inspirée pour la forme du projet : 
#"Analyse du réseau ferré de la SNCF: Comment expliquer les retards permanents de la compagnie française ?" 
# sur le site de M. Lino Galiana

def prediction(x, y, afficher = True):
    #séparation des données en 2 échantillon 
    X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
    
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