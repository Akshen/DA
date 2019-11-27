import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import analyze

#Connectivity to DB
engine = create_engine('postgresql://ak:da@123@127.0.0.1:5432/asteroids')
#ndf = pd.read_sql_table('name_asteroids', engine)
apvfdf = pd.read_sql_table('asteroids_potential_value', engine)
#loeadf = pd.read_sql_table('loea_largest_by_diameter', engine)
#rnvdf = pd.read_sql_table('asteroid_data', engine)

analyze.summary(apvfdf)
user_inp = input("Enter Y to proceed or N to Exit\n")
if user_inp=='Y' or user_inp=='y':
    for i in apvfdf.columns:
        (analyze.col_check(apvfdf, i))
else:
    pass


