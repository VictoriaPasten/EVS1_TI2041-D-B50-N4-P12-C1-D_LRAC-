from django.shortcuts import render
from django.http import HttpResponse

def lista(request):
    return HttpResponse(
        "<h1>Lista de compras</h1>"
        "<h2>Compras mes de: Septiembre</h2>"
        "<li>Azucar</li>"
        "<p>El precio del azucar es de: $890</p>"
        "<li>Sal</li>"
        "<p>El precio de la sal es de: $900</p>"
        "<li>Pan</li>"
        "<p>El precio del kilo de pan  es de: $2000</p>"

    )

def notas(request):
    return HttpResponse(
        "<h1>Notas primer semestre<h1/>"
       """<h2 style="color:red">Notas del Alumno</h1>"""
        """<table border="1">
        <tr>
            <th>Materia</th>
            <th>Nota</th>
        </tr>
        <tr>
            <td>Matemáticas</td>
            <td>4.5</td>
        </tr>
        <tr>
            <td>Ciencias</td>
            <td>7.0</td>
        </tr>
        <tr>
            <td>Lenguaje</td>
            <td>5.2</td>
        </tr>
        <tr>
            <td>Historia</td>
            <td>6.8</td>
        </tr>
        </table>"""
        
        "<footer>Las notas disponibles en esta pagina son privadas y se prohibe su difusion<footer/>"
    )


