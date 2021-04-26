import pandas as pd
#mport mpu
from geopy.distance import geodesic
pd.options.mode.chained_assignment = None  # default='warn'

def cargarcsv(filename):
    df = pd.read_csv(filename)
    #print(dfOD.shape)
    #dfOD.to_sql('Trips', con, if_exists='replace')
    return df


def guardar(df, con):
    df.to_sql('Trips', con, if_exists='replace')


def distancia (row):
    #return mpu.haversine_distance((row['start_lat'], row['start_lon']), (row['end_lat'], row['end_lon']))
    return geodesic((row['start_lat'], row['start_lon']), (row['end_lat'], row['end_lon'])).kilometers


def velocidad (row):
    return row['distance']/row['duration_sec']*3600


def viajespopulares(dftrips, top):
    df1 = dftrips[['start_station_code', 'end_station_code']].groupby(['start_station_code', 'end_station_code']) \
                                                             .size() \
                                                             .reset_index(name='viajes')
    df1.sort_values('viajes', ascending=False, inplace=True)
    #df1.to_csv('sample.csv')
    return df1.head(top)


def utilizacion(pinicial, pfinal, dftripsIni, dftripsFin):
    years = []
    numviajes = []
    tiempotot = []
    years.append(pinicial)
    numviajes.append(dftripsIni.shape[0])
    tiempotot.append(dftripsIni['duration_sec'].sum())
    years.append(pfinal)
    numviajes.append(dftripsFin.shape[0])
    tiempotot.append(dftripsFin['duration_sec'].sum())
    dfutilizacion = pd.DataFrame({
                                'year': years,
                                'cantidad_viajes': numviajes,
                                'tiempo_utilizacion': tiempotot
                                })
    return dfutilizacion


def velocidadPromedio(dftrips, dfStations):
    dfSt1 = dfStations[['code', 'latitude', 'longitude']]
    dfSt2 = dfStations[['code', 'latitude', 'longitude']]
    #dfTrp1 = dftrips[['start_station_code', 'end_station_code', 'duration_sec']]
    dfTrp1 = dftrips[['start_station_code', 'end_station_code', 'duration_sec']].sample(n=20000)
    df1 = dfTrp1.set_index('start_station_code').join(dfSt1.set_index('code'))
    df1.rename(columns={'latitude': 'start_lat'}, inplace=True)
    df1.rename(columns={'longitude': 'start_lon'}, inplace=True)
    df2 = df1.set_index('end_station_code').join(dfSt2.set_index('code'))
    df2.rename(columns={'latitude': 'end_lat'}, inplace=True)
    df2.rename(columns={'longitude': 'end_lon'}, inplace=True)
    df2['distance'] = df2.apply(lambda row: distancia(row), axis=1)
    df2['speed'] = df2.apply(lambda row: velocidad(row), axis=1)
    return round(df2['speed'].mean(), 2)


def totalViajes(dfViajes, momento):
    df1 = dfViajes[['start_date', 'end_date']]
    df1['start_date_b'] = pd.to_numeric(df1['start_date'].str.replace(r'\D+', ''))
    df1['end_date_b'] = pd.to_numeric(df1['end_date'].str.replace(r'\D+', ''))
    df2 = df1[(df1['end_date_b'] >= momento) & (df1['start_date_b'] <= momento)]
    return df2.shape[0]

