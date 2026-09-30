#PRIMERA PARTE DEMOSTRADA QUE EXISTE UNA CONEXION CON LA BASE DE DATOS
import matplotlib.pyplot as plt
import psycopg2
conn = psycopg2.connect(
dbname="agrobio_db", user="postgres", password="", host="localhost", port="5432"
)
print("Conexión exitosa")


#SEGUNDA PARTE REALIZANDO UNA CONSULTA
cur = conn.cursor()
cur.execute("SELECT SUM(produccion) FROM cultivos")
print("Producción total:", cur.fetchone()[0])

#TERCERA PARTE REALIZANDO UNA CONSULTA TABULADA
import pandas as pd
df = pd.read_sql("SELECT cultivo, rendimiento FROM cultivos", conn)
print(df)


#CUARTA PARTE REALIZANDO LAS GRAFICAS NECESARIAS
df.plot(kind='bar', x='cultivo', y='rendimiento', title='Rendimiento por cultivo')
plt.show()