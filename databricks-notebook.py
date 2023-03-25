# Databricks notebook source
sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list

sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
source ~/.bashrc
# optional: for unixODBC development headers
sudo apt-get install -y unixodbc-dev


apt-get install -y unixodbc-dev

# COMMAND ----------

import pandas as pd
import pyodbc
import traceback
from azure.storage.blob import ContainerClient
from azure.core.exceptions import ResourceExistsError
from fastparquet import write

class ParquetAppender:
    BLOB_CONTAINER_CLIENT = ""

    blobFileName = ""
    blobConnectionParams = {}
    tableToArchive = ""
    dbConnectionParams = {}

    def __init__(self, blobFileName, blobConnectionParams):
        self.blobFileName = blobFileName
        self.blobConnectionParams = blobConnectionParams

    def parquetExists(self):
        # This method checks if the parquet file exists

        try:
          self.BLOB_CONTAINER_CLIENT = ContainerClient.from_connection_string(self.blobConnectionParams['connectionString'], self.blobConnectionParams['container'])
        except Exception as e:
          print(traceback.format_exc())
          return False

        return True

    def downloadParquetFile(self):
        # This method downloads the parquet file
        if not self.parquetExists():
            return False

        with open(self.blobFileName, "wb") as parquet_blob:
            download_stream = self.BLOB_CONTAINER_CLIENT.download_blob(self.blobFileName)
            parquet_blob.write(download_stream.readall())
	   
    def uploadParquetFile(self):
        # This method downloads the parquet file
        if not self.parquetExists():
            return False

        with open(self.blobFileName, "rb") as data:
            self.BLOB_CONTAINER_CLIENT.upload_blob(name=self.blobFileName, data=data, overwrite=True)
        
    def selectRecordsToBeArchived(self, queryToArchive, dbConnectionParams):
        # This method selects records to be archived, and returns a dataframe of the records

        driver = dbConnectionParams['driver']
        server = dbConnectionParams['server']
        port = dbConnectionParams['port']
        database = dbConnectionParams['database']
        username = dbConnectionParams['username']
        password = dbConnectionParams['password']

        driver= '{ODBC Driver 18 for SQL Server}'
        dict = {}

        try:
            with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(queryToArchive)
                    columns = []
                    for column in cursor.description:
                        columns.append(column[0])
                        dict[column[0]] = []
                    rows = cursor.fetchall()
                    for row in rows:
                        i = 0
                        for col in row:
                            dict[columns[i]].append(col)
                            i = i + 1
                    # for row:
                # with conn.cursor() as cursor:
            # with pyodbc.connect:
        except Exception as e:
            print(e)
        df = pd.DataFrame(dict)
        return df

    def archiveToParquet(self, dataframe):
        # This method adds the records to the parquet file

        write(self.blobFileName, dataframe, append=True)
    

blobConn = {}
blobConn['connectionString'] = 'DefaultEndpointsProtocol=https;AccountName=parquetsg;AccountKey=DKJzGunw1kenmDcEZcnUM5fMPduNvuu/FKUEntp+1pgk5fFzw80RMzaKqttXGVMA4kVLInJUenf/+AStaLmYuQ==;EndpointSuffix=core.windows.net'
blobConn['container'] = 'parquet-container'

pAppender = ParquetAppender('pq.parquet', blobConn)
pAppender.downloadParquetFile()

dbConnectionParams = {}
dbConnectionParams['driver'] = '{ODBC Driver 18 for SQL Server}'
dbConnectionParams['server'] = 'azure-sql-3143.database.windows.net'
dbConnectionParams['port'] = '1433'
dbConnectionParams['database'] = 'nyc_trips'
dbConnectionParams['username'] = 'my_user'
dbConnectionParams['password'] = '!@#$%AA1a'

query = 'select * from [dbo].[taxi_zone_lookup]'
df = pAppender.selectRecordsToBeArchived(query, dbConnectionParams)
pAppender.archiveToParquet(df)
pAppender.uploadParquetFile()
