import pandas as pd


def cargarcsv(filename):
    df = pd.read_csv(filename)
    #print(dfOD.shape)
    #dfOD.to_sql('Trips', con, if_exists='replace')
    return df


def guardar(df, con):
    df.to_sql('Stations', con, if_exists='replace')


def populares(dftrips, top):
    dfstart = dftrips[['start_station_code']]
    dfstart.rename(columns={'start_station_code': 'station_code'}, inplace=True)
    dfend = dftrips[['end_station_code']]
    dfend.rename(columns={'end_station_code': 'station_code'}, inplace=True)
    dfambos = pd.concat([dfstart, dfend])
    dfpopulares = dfambos.groupby(['station_code']).size().reset_index(name='viajes')
    dfpopulares.sort_values('viajes', ascending=False, inplace=True)
    return dfpopulares.head(top)


def capacidadTotal(dfStationDet, dfStation):
    dfStationDet['n'] = pd.to_numeric(dfStationDet['n'])
    df = dfStation.set_index('code').join(dfStationDet.set_index('n'))
    totbicis = int(df['ba'].sum())
    return totbicis


def capacidadComparacion(pinicial, pfinal, dfStationDet, dfStationIni, dfStationFin):
    years = []
    estaciones = []
    bicis = []
    dfStationDet['n'] = pd.to_numeric(dfStationDet['n'])
    dfini = dfStationIni.set_index('code').join(dfStationDet.set_index('n'))
    years.append(pinicial)
    estaciones.append(dfini.shape[0])
    bicis.append(int(dfini['ba'].sum()))
    dffin = dfStationFin.set_index('code').join(dfStationDet.set_index('n'))
    years.append(pfinal)
    estaciones.append(dffin.shape[0])
    bicis.append(int(dffin['ba'].sum()))
    dfcapacidad = pd.DataFrame({
        'year': years,
        'estaciones': estaciones,
        'bicicletas': bicis
        })
    return dfcapacidad

