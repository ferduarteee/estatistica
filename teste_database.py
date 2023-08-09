import psycopg2


conn = psycopg2.connect(
    dbname='nome_do_banco_de_dados',
    user='nome_de_usuario',
    password='senha',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
