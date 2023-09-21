from django.shortcuts import render
from django.http import HttpResponse

def recomendacion(request):
    return HttpResponse(
        "<h1>Recomendaciones de viajes</h1> "
        "<h2>Cancún, México</h2>"
        "<p>Cancún es una ciudad de México ubicada en la península de Yucatán que limita con el mar Caribe y que es conocida por sus playas</p>"
        "<h3>Te recomiendo esta actividad</h3>"
        """<a href:"https://www.tripadvisor.cl/Attraction_Review-g1575485-d2304581-Reviews-Museo_Subacuatico_de_Arte-Quintana_Roo_Yucatan_Peninsula.html">Visita el museo subactuatico</a>"""
        "<h2>Roma,Italia</h2>"
        "<p>Roma, la capital de Italia, es una extensa ciudad cosmopolita que tiene a la vista casi 3,000 años de arte, arquitectura y cultura de influencia mundial</p>"
        "<h3>Te recomiendo esta actividad</h3>"
        """<a href:https://www.civitatis.com/es/roma/visita-coliseo-subterraneo?aid=117&cmp=cu&cmpint=47029">Visita el coliseo romano</a>"""
        "<h2>Paris,Francia</h2>"
        "<p>París, la capital de Francia, es una importante ciudad europea y un centro mundial del arte, la moda, la gastronomía y la cultura.</p>"
        "<h3>Te recomiendo esta actividad</h3>"
        """<a href:"https://www.toureiffel.paris/fr">Visita la torre eiffel</a>"""
    )

def informacion(request):
    return HttpResponse(
        "<ul> <li>Vuelo 1 - Destino: Nueva York</li> "
        "<li>Vuelo 2 - Destino: Los Ángeles</li>"
        "<li>Vuelo 3 - Destino: Chicago</li>"
        "<li>Vuelo 4 - Destino: Miami</li>"
        "<li>Vuelo 5 - Destino: San Francisco</li> </ul>"
    )
