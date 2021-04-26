La solucion esta hecha en python. Consta de los siguientes modulos:
- main.py 		(programa principal)
- viajes.py 	(funciones aplicadas a los viajes)
- estaciones.py	(funciones aplicadas a las estaciones)
- graficos.py	(funciones graficadoras)
- dbmanager.py	(funciones para acceso a base de datos. Por ahora no se usa)

Librerias necesarias para la ejecucion:
- pandas
- matplotlib
- geopy

IMPORTANTE: copiar los archivos del dataset al directorio de los fuentes para poder ejecutar el programa.
			Son necesarios lo archivos csv de OD, Stations y el archivo json de Stations

Ejecucion desde terminal python ejecutar:
> main.py

Nos muestra un menu de las puntos correspondientes al challenge:
> main.py 
Uso main.py opcion periodo1 [periodo2] [top]
Opciones:
1 - Histograma de tiempos de viaje para un año dado
2 - Listado del Top 5 de estaciones más utilizadas para un año dado
3 - Listado del Top N de viajes más comunes para un año dado
4 - Identificación de horas punta para un año determinado
5 - Pruebas Unitarias. N/A
6 - Comparación de utilización del sistema entre dos años cualesquiera
7 - Capacidad instalada total
8 - Cambio en la capacidad instalada entre dos años puntuales
9 - Ampliación de la cobertura de la red entre dos años puntuales
10 - Comparación de densidad de la red para un par de años puntuales
11 - Velocidad promedio de los ciclistas para un año determinado
12 - Cantidad de bicicletas totales para un momento dado

Ejemplos de ejecucion para cada opcion:
main.py 1 2014
main.py 2 2014
main.py 2 2014 3
main.py 4 2014
main.py 6 2014 2015
main.py 7 2014
main.py 8 2014 2015
main.py 11 2014
main.py 12 2014 201404151315



Me quedaron por falta de tiempo desarrollar los puntos 9 y 10 que aplican calculos de area. Pruebas unitarias fui haciendo con bajadas a sql. Las consultas se pueden ver en el archivo script1.sql
Cualquier duda me consultan.
