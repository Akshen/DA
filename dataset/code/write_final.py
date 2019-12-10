from cassandra.cluster import Cluster

#default connection localhost
cluster = Cluster()
keyspace_name = 'your keyspace name'
session = cluster.connect(keyspace_name)

#Queries
'''
Example
# NOTE Column-name and type should be similar to that of data to be written
session.execute('CREATE TABLE asteroid (row int,full_name text, neo text, moid_jupiter text, moid text, producer text, rot_per int, PRIMARY KEY(row, neo));') #Create table for file
'''
session.execute('CREATE TABLE your_tablename (column name and datatype, PRIMARY KEY(name of pks));') #Create table for file
'''
Example for below
import your csv file, loop over it and write data as per format of table
'''

session.execute('COPY your_tablename (columns names) from path_to_file and HEADER=TRUE') #Write data from file to table
session.execute()
print('Done')

