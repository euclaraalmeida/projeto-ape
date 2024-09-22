import pandas as pd

# Lendo os arquivos CSV
arq1_df = pd.read_csv('proejtoape-main/minhaparte/escolaridade.csv')
arq2_df = pd.read_csv('proejtoape-main/minhaparte/estadocivil.csv')
arq3_df = pd.read_csv('proejtoape-main/minhaparte/genero.csv')
arq4_df = pd.read_csv('proejtoape-main/minhaparte/cargos.csv')

# Concatenando os DataFrames ao longo do eixo das colunas (axis=1)
arquivo_junto2_df = pd.concat([arq1_df, arq2_df, arq3_df, arq4_df], axis=1)

# Salvando o resultado em um novo arquivo CSV, separado por ponto e vírgula (;)
arquivo_junto2_df.to_csv('proejtoape-main/minhaparte/arquivo_junto2.csv', sep=';', index=False)