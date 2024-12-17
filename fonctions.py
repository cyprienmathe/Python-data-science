import pandas as pd
import matplotlib.pyplot as plt
import requests

# A function that transforms a call of the api into a usable panda file 
def call_api(api_url):
    req = requests.get(api_url)
    wb = req.json()
    print(wb.keys())

    df = pd.DataFrame(wb['results'])
    return(df)

#Cette fonction mange directement le lien que sort l''interface de l'api donc pas besoin de le modifier, elle rend un panda directement
#Il sert à obtenir des tableaux plus grands sans la limite de 100
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

