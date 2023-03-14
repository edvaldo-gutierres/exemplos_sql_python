#Importa as bibliotecas
import os
from operator import index
import pyodbc
import pandas as pd

#Informe a pasta onde o arquivo .csv se encontram
pasta = 'C:\\Users\\edvaldo.ferreira\\Desktop\\Relatórios\\Projetos\\Projeto Movimentações Salariais\\carga_API\\arquivos\\2022-10-01\\'

#Informe o nome do arquivo .csv
arquivo = 'EmpCompensation1_2022-10-01.csv'

#Lê o arquivo
df = pd.read_csv(pasta + arquivo)
print(df)

#Conexão banco de dados SQL
server = 'localhost\SQLEXPRESS' 
database = 'python_sql' 
username = '' 
password = '' 
conectDB = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';')
cursor = conectDB.cursor()   

#Informa o nome da tabela do banco
tabela = '[dbo].[stg_empcompensation]'
 
# Busca o nome path dos arquivo e insere os dados no banco
try:
    qry = "BULK INSERT " + tabela + " FROM '" + pasta + arquivo + "'  WITH  (CODEPAGE = '65001', FORMAT = 'CSV', FIRSTROW = 2)"
    cursor.execute(qry)
    cursor.commit()
    print('Insert concluído com sucesso!!!')
        
except: 
    print('Erro BULK INSERT - Verificar!')
    
cursor.close()

print('Processo finalizado com sucesso!!!')