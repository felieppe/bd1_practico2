import mysql.connector, os

cnx = mysql.connector.connect(
    host="localhost",
    database="practico2",
    user="root",
    password="password",
    port="3307",
)

cursor = cnx.cursor()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("Inserta una SQL query:")
    sql_query = input("")
    
    cursor.execute(sql_query)
    result = cursor.fetchall()
    print("\n Resultado:")
    for row in result:
        print(row)
    
    print("\n Presiona Enter para continuar o 'q' para salir")
    exit = input("")
    if exit == "q":
        break
    
    clear()