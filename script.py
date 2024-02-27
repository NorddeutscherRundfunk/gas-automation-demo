#%% load libraries
import pandas as pd
from datawrapper import Datawrapper

#global variables
CHART_ID = 'Test'

def get_data():
  df = pd.read_csv('https://www.bundesnetzagentur.de/_tools/SVG/js2/_functions/csv_export.html?view=renderCSV&id=870304',sep=';',decimal =',')
  return df

def process_data(df):
  df.columns = ['Datum','Letztes Jahr','Aktuell','Minimum 2018-2021','Maximum 2018-2021'] #Spaltennamen umbenennen
  df['Datum'] = df['Datum']+'2016' #Platzhalter-Jahreszahl einfügen für Datawrapper
  df['Datum'] = pd.to_datetime(df['Datum'],dayfirst=True)
  df['Datum'] = df['Datum'].apply(lambda x: str(x).replace('2016','2017') if str(x) < '2016-04-01' else x)
  return df

def publish_dw_chart(data, chart_id = CHART_ID):
  dw = Datawrapper()
  dw.add_data(chart_id = chart_id ,data=data)
  dw.publish_chart(chart_id = chart_id)

#%% hier startet das Hauptprogramm

if __name__ == "__main__":
  #hier startet das hauptprogramm
  df = get_data()
  df = process_data(df)
  publish_dw_chart(df, chart_id = CHART_ID)
    
# %%
