import sys
import pandas as pd
import graficos as gf
import viajes as vs
import estaciones as es
#import dbmanager as dbm

maxdisplay = 5
numparam = len(sys.argv) - 1
if numparam not in (2, 3, 4):
    print('Uso main.py opcion periodo1 [periodo2] [top]')
    print('Opciones:')
    print('1 - Histograma de tiempos de viaje para un año dado')
    print('2 - Listado del Top 5 de estaciones más utilizadas para un año dado')
    print('3 - Listado del Top N de viajes más comunes para un año dado')
    print('4 - Identificación de horas punta para un año determinado')
    print('5 - Pruebas Unitarias. N/A')
    print('6 - Comparación de utilización del sistema entre dos años cualesquiera')
    print('7 - Capacidad instalada total')
    print('8 - Cambio en la capacidad instalada entre dos años puntuales')
    print('9 - Ampliación de la cobertura de la red entre dos años puntuales')
    print('10 - Comparación de densidad de la red para un par de años puntuales')
    print('11 - Velocidad promedio de los ciclistas para un año determinado')
    print('12 - Cantidad de bicicletas totales para un momento dado')
    exit(0)

opcion = sys.argv[1]
pinicial = sys.argv[2]
pfinal = None

if pinicial not in ('2014', '2015', '2016', '2017'):
    print('Periodo inicial invalido')
    exit(0)

if opcion in ('6', '8', '9', '10'):
    pfinal = sys.argv[3]
    if pfinal not in ('2014', '2015', '2016', '2017'):
        print('Periodo final invalido')
        exit(0)
    if numparam == 4:
        maxdisplay = int(sys.argv[4])
elif opcion == '12':
    if numparam != 3:
        print('Uso main.py 12 periodo momento(YYYYMMDDHH24MM)')
        exit(0)
    momento = int(sys.argv[3])
    if len(sys.argv[3]) != 12:
        print('Formato Fecha: YYYYMMDDHH24MM')
        exit(0)
    momento = int(sys.argv[3])
else:
    if numparam == 3:
        maxdisplay = int(sys.argv[3])


if opcion == '1':
    dfViajes = vs.cargarcsv('OD_' + pinicial + '.csv')
    dfDuration = dfViajes['duration_sec']
    gf.histograma(dfDuration, 'Tiempos de Viaje', 'Duracion(S)', 'Cant.Viajes')
elif opcion == '2':
    dfViajes = vs.cargarcsv('OD_' + pinicial + '.csv')
    print(es.populares(dfViajes, maxdisplay).to_string())
elif opcion == '3':
    dfViajes = vs.cargarcsv('OD_' + pinicial + '.csv')
    print(vs.viajespopulares(dfViajes, maxdisplay).to_string())
elif opcion == '4':
    dfViajes = vs.cargarcsv('OD_' + pinicial + '.csv')
    dfHoras = dfViajes['start_date'].str[11:13]
    gf.histograma(dfHoras, 'Hora Punta', 'Hora del dia', 'Cant.Viajes')
elif opcion == '5':
    print('No disponible')
elif opcion == '6':
    dfViajesIni = vs.cargarcsv('OD_' + pinicial + '.csv')
    dfViajesFin = vs.cargarcsv('OD_' + pfinal + '.csv')
    print(vs.utilizacion(pinicial, pfinal, dfViajesIni, dfViajesFin).to_string())
elif opcion == '7':
    jsondata = pd.read_json('stations.json')
    dfStationDet = pd.json_normalize(jsondata['stations'])
    dfStations = es.cargarcsv('Stations_' + pinicial + '.csv')
    print('Capacidad total instalada: ' + str(es.capacidadTotal(dfStationDet, dfStations)) + ' bicicletas')
elif opcion == '8':
    jsondata = pd.read_json('stations.json')
    dfStationDet = pd.json_normalize(jsondata['stations'])
    dfStationIni = es.cargarcsv('Stations_' + pinicial + '.csv')
    dfStationFin = es.cargarcsv('Stations_' + pfinal + '.csv')
    print(es.capacidadComparacion(pinicial, pfinal, dfStationDet, dfStationIni, dfStationFin).to_string())
elif opcion == '9':
    print('En construccion')
elif opcion == '10':
    print('En construccion')
elif opcion == '11':
    dfViajes = vs.cargarcsv('OD_' + pinicial + '.csv')
    dfStations = es.cargarcsv('Stations_' + pinicial + '.csv')
    print('Velocidad promedio de viajes: ' + str(vs.velocidadPromedio(dfViajes, dfStations)) + ' km/h')
elif opcion == '12':
    jsondata = pd.read_json('stations.json')
    dfStationDet = pd.json_normalize(jsondata['stations'])
    dfStations = es.cargarcsv('Stations_' + pinicial + '.csv')
    totEstaciones = es.capacidadTotal(dfStationDet, dfStations)
    dfViajes = vs.cargarcsv('OD_' + pinicial + '.csv')
    totViajes = vs.totalViajes(dfViajes, momento)
    totBicis = totEstaciones + totViajes
    print('Bicicletas en estaciones: ' + str(totEstaciones))
    print('Bicicletas en uso: ' + str(totViajes))
    print('Cantidad total de bicicletas: ' + str(totBicis))
else:
    print('Opcion no contemplada')

"""
con = dbm.create_connection('biximtl.db')
es.guardar(dfEstaciones, con)
vs.guardar(dfViajes, con)
dfStationDet.to_sql('StationsDet', con, if_exists='replace')
dfViajes.to_sql('Trips', con, if_exists='replace')
dfStations.to_sql('Stations', con, if_exists='replace')
dfStationIni.to_sql('Stations_' + pinicial, con, if_exists='replace')
dfStationFin.to_sql('Stations_' + pfinal, con, if_exists='replace')
"""

exit(0)






