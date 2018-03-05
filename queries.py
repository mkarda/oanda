import psycopg2
from psycopg2._psycopg import AsIs

conn = None

def checkSchema(schemaName):
    return f"SELECT * FROM information_schema.schemata WHERE schema_name = '{schemaName}'"

def createSchema(schemaName):
    return "CREATE SCHEMA {} AUTHORIZATION {}".format(schemaName, 'postgres')











