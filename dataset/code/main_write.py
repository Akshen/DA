import psycopg2
import csv
import pandas as pd
from sqlalchemy import create_engine

#Read data from csv 
#apvf = pd.read_csv('Asteroids_Potential_Value.csv')
#loea = pd.read_csv('loea_largest_by_diameter.csv')
rnv = pd.read_csv('asteroid_result.csv')

#Connectivity to DB
engine = create_engine('postgresql://akshen:da@123@127.0.0.1:5432/asteroids')
# Creating of DataFrame
#apvfdf = pd.DataFrame(apvf)
#loeadf = pd.DataFrame(loea)
rnvdf = pd.DataFrame(rnv)

#Writing to DB
#apvfdf.to_sql('asteroids_potential_value', engine)
#loeadf.to_sql('loea_largest_by_diameter', engine)
rnvdf.to_sql('asteroid_data', engine)