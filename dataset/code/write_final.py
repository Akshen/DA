from cassandra.cluster import Cluster
import pandas as pd

#default connection localhost
cluster = Cluster()
keyspace_name = 'your_keyspace_name'
session = cluster.connect(keyspace_name)

#Queries
#NOTE Column-name and type should be similar to that of data to be written
#session.execute('CREATE TABLE your_tablename (column name and datatype, PRIMARY KEY(name of pks));') #Create table for file

session.execute('CREATE TABLE asteroid (row int,full_name text, neo text, moid_jupiter text, moid text, producer text, rot_per int, PRIMARY KEY(row, neo));') #Create table for file
session.execute('CREATE TABLE mars (doy int, sol int, dew_point text,\
                relative_humidity text, relative_humidity_m text,\
                solar_longitude_ls text, surface_air_temp text, surface_pressure text,\
                vapour_pressure text, water_partial_pressure text, PRIMARY \
                KEY(doy, sol));')
session.execute('CREATE TABLE exoplanets (loc_rowid int, pl_hostname text, pl_letter  text,\
                pl_discmethod text, pl_controvflag int, pl_pnum int,  pl_orbper  float, pl_orbsmax  float, pl_orbeccen  float,\
                pl_orbincl  float, pl_bmassj  float, pl_radj  float, pl_dens  float, pl_ttvflag  int,\
                pl_kepflag  int, pl_k2flag  int, ra float, dec  float, st_dist  float, st_optmag  float,\
                st_optband text, st_teff float,st_mass float, st_rad float, rowupdate date, pl_facility text,\
                fst_logg float, PRIMARY KEY(loc_rowid, pl_letter));')

# CQL CMD works in CSQLSH ONLY
session.execute('COPY your_tablename (columns names) from path_to_file and HEADER=TRUE') #Write data from file to table

query = "SELECT * from mars;"
df = pd.DataFrame(list(session.execute(query)))
print(df.head(5))
print('Done')