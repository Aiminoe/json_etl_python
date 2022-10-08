import json
import requests
import matplotlib.pyplot as plt

def fetch():
    response = requests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50')
    json_response = response.json()
    dataset = [{"price": x["price"] , "condition": x["condition"]} for x in json_response["results"] if x["currency_id"] 
    == "ARS"]
    return dataset

def transform(dataset, min, max):
    list_min= [ x for x in dataset if x["price"] < min ]
    min_count= len(list_min)
    list_med= [ x for x in dataset if x["price"] >= min and x["price"] <= max]
    min_max_count= len(list_med)
    list_max= [ x for x in dataset if x["price"] > max ]
    max_count= len(list_max)
    return [min_count, min_max_count, max_count]

def report(data):
    fig = plt.figure()
    fig.suptitle("Rango de precios propiedades", fontsize=16)
    manzanas = [20,10,25,30]
    rangos = ["Menores al $5000","Entre $5000 y $25000","Mayores a $25000"]
    plt.pie(data, labels= rangos)
    plt.show()
    return




if __name__ == "__main__":
    min = 5000
    max = 25000

    dataset = fetch()
    data = transform(dataset, min, max)
    report(data)