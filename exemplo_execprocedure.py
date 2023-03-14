import pyodbc

#Conexão banco de dados SQL
server = 'localhost\SQLEXPRESS' 
database = 'portfolio' 
username = '' 
password = '' 
conectDB = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';')
cursor = conectDB.cursor()

#Executa procedure
try:
    print('Executando dbo.spr_atualiza_dim_calendario')
    qry_proc = 'EXEC dbo.spr_atualiza_dim_calendario'
    cursor.execute(qry_proc)
    cursor.commit()
except:
    print('Erro - Execução Procedure dbo.spr_atualiza_dim_calendario. Verificar!!!')

cursor.close()

print('Procedure executada com sucesso!!!')