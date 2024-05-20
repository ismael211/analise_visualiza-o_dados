import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo .xlsx
file_path = 'Pessoa_custo.xlsx'  # Substitua pelo caminho do seu arquivo
df = pd.read_excel(file_path)

# Convertendo a coluna 'DATA_ATEND' para datetime e formatando para dia/mês
df['DATA_ATEND'] = pd.to_datetime(df['DATA_ATEND'], format='%m/%d/%Y').dt.strftime('%d/%m')

# Calculando a média de custo por dia
mean_cost_per_day = df.groupby('DATA_ATEND')['CUSTO'].mean()

# Dividindo os dados em duas séries: uma para valores acima ou iguais a 200 e outra para valores abaixo de 200
mean_cost_above_200 = mean_cost_per_day[mean_cost_per_day >= 200]
mean_cost_below_200 = mean_cost_per_day[mean_cost_per_day < 200]

# Gráfico da média de custo por dia acima ou igual a 200 reais
plt.figure(figsize=(12, 6))
mean_cost_above_200.plot(kind='bar', color='darkblue')
plt.title('Média de Gasto por Dia acima de 200 R$')
plt.xlabel('Data')
plt.ylabel('Média de Custo (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('media_gasto_por_dia_acima_200.png')
plt.show()

# Gráfico da média de custo por dia abaixo de 200 reais
plt.figure(figsize=(12, 6))
mean_cost_below_200.plot(kind='bar', color='darkred')
plt.title('Média de Gasto por Dia abaixo de 200 R$')
plt.xlabel('Data')
plt.ylabel('Média de Custo (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('media_gasto_por_dia_abaixo_200.png')
plt.show()

# Calculando a média de idade por dia
mean_age_per_day = df.groupby('DATA_ATEND')['IDADE'].mean()

# Gráfico da média de idade por dia
plt.figure(figsize=(12, 6))
mean_age_per_day.plot(kind='bar', color='darkgreen')
plt.title('Média de Idade por Dia')
plt.xlabel('Data')
plt.ylabel('Média de Idade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('media_idade_por_dia.png')
plt.show()

# Selecionando os 15 pacientes que mais gastaram
top_15_patients = df.groupby('NOME')['CUSTO'].sum().nlargest(15)

# Gráfico dos 15 pacientes que mais gastaram durante o mês
plt.figure(figsize=(12, 6))
top_15_patients.sort_values().plot(kind='barh', color='darkorange')
plt.title('Top 15 Pacientes que Mais Gastaram Durante o Mês')
plt.xlabel('Custo Total (R$)')
plt.ylabel('Nome do Paciente')
plt.tight_layout()
plt.savefig('top_15_gasto_por_paciente.png')
plt.show()
