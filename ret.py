import requests
from pprint import pprint
API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Fight_Club"

busqueda = URL + API_KEY + "&t=" + titulo
respuesta = requests.get(busqueda)
dic_peli = respuesta.json()
#pprint(dic_peli)
#print(busqueda)
#print(dic_peli["Director"])

def actores(act):
    titulo = act
    busqueda = URL + API_KEY + "&t=" + titulo
    respuesta = requests.get(busqueda)
    act_peli = respuesta.json()
    print(busqueda)
    print(act_peli["Actors"])
peli = input("Pelicula: ")
actores(peli)
