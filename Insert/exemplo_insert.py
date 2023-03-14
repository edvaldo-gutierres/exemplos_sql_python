
from operator import index
import pyodbc
import pandas as pd

# Diretório
pasta = 'C:\\Users\\edvaldo.ferreira\\Documents\\script_python\\Insert'

# Leitura de arquivo
df = pd.read_excel(pasta + '/base_dados.xlsx')

#Conexão banco de dados SQL
server = 'localhost\SQLEXPRESS' 
database = 'portfolio' 
username = '' 
password = '' 
conectDB = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conectDB.cursor()

# Insert no banco SQL
try:

    for index, row in df.iterrows():
        cursor.execute("INSERT INTO dbo.teste (nome,CPF,data_nascimento) VALUES(?,?,?)", row.Nome, row.CPF, row.Data_Nasc)
    conectDB.commit()

except:
    print('Erro - INSERT INTO dbo.teste. Verificar!!!')

#Fecha conexão banco de dados SQL
cursor.close()  

print('Insert finalizado com sucesso!!!')

