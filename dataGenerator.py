import configparser
import psycopg2
import queries as queries

config = configparser.ConfigParser()
config.read("config.ini")
dbname = config['Postgres']['dbname']
password = config['Postgres']['password']
user = config['Postgres']['user']

conn = psycopg2.connect("dbname={} user={} password={}".format(dbname, user, password))
cursor = conn.cursor()
conn.autocommit = True

print(queries.checkSchema("eur_usd"))
a = cursor.execute(queries.checkSchema("eur_usd"))
# print(a.fetchall())

print(a)
print(a is None)
if a is None:
    print(queries.createSchema("EUR_USD"))
    cursor.execute(queries.createSchema("EUR_USD"))
    conn.commit()
