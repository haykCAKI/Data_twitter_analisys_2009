# Data_twitte_analisys

# Análise de Dados do Twitter

## Visão Geral

Este projeto realiza análise de dados de tweets armazenados em um arquivo CSV (`testdata.manual.2009.06.14.csv`). Ele executa várias análises sobre o conteúdo textual dos tweets, focando na frequência de palavras, menções de usuários e hashtags.

## Requisitos

- Python 3.x
- pandas
- matplotlib
- seaborn
- pyarrow

## Instalação

Para executar o script, certifique-se de ter o Python instalado junto com as bibliotecas necessárias. Você pode instalar as dependências usando pip:

```bash
pip install pandas matplotlib seaborn pyarrow
```

## Descrição
O script realiza as seguintes tarefas:

## Carregamento dos Dados:

Lê o arquivo CSV (testdata.manual.2009.06.14.csv) usando pyarrow e converte para um DataFrame do pandas.
#Pré-processamento:

Renomeia colunas para melhor legibilidade.
Converte o texto para minúsculas para uniformidade.
Análise de Frequência de Palavras:

Calcula a frequência de cada palavra nos textos dos tweets usando expressões regulares e Counter.
Visualiza as 20 palavras mais comuns usando um gráfico de barras.
## Análise de Menções de Usuários:

Extrai menções de usuários (@username) dos textos dos tweets usando expressões regulares.
Conta a frequência de cada menção de usuário e visualiza os 20 usuários mais mencionados.
## Análise Temporal:

Converte a coluna 'date' para o formato datetime.
Extrai a hora do dia dos timestamps e adiciona como uma nova coluna ('hour').
## Análise de Hashtags por Hora:

Agrupa os tweets por hora e extrai hashtags (#hashtag) usando expressões regulares.
Conta a frequência de cada hashtag por hora e imprime os 10 hashtags principais para cada hora.
## Saída
O script gera visualizações de frequência de palavras e menções de usuários, além de imprimir as principais hashtags por hora no console.
## código
```python
#Trabalho feito por Herick Akio Yoshii Kumata
#Analise e Desenvolvimento de Sistemas
#Atividade Somativa feita em Big Data

import pyarrow.csv as pv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

file_path = 'testdata.manual.2009.06.14.csv'
table = pv.read_csv(file_path)

df = table.to_pandas()

df.columns = ['target', 'id', 'date', 'flag', 'user', 'text']

df.head()

all_words = ' '.join(df['text']).lower()
words = re.findall(r'\b\w+\b', all_words)
word_freq = Counter(words)

most_common_words = word_freq.most_common(20)
most_common_words_df = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])

plt.figure(figsize=(10,6))
sns.barplot(x='Frequency', y='Word', data=most_common_words_df)
plt.title('20 Palavras Mais Frequentes')
plt.show()

user_mentions = re.findall(r'@\w+', all_words)
user_mentions_freq = Counter(user_mentions)

most_common_mentions = user_mentions_freq.most_common(20)
most_common_mentions_df = pd.DataFrame(most_common_mentions, columns=['User', 'Frequency'])

plt.figure(figsize=(10,6))
sns.barplot(x='Frequency', y='User', data=most_common_mentions_df)
plt.title('20 Usuários Mais Mencionados')
plt.show()

df['date'] = pd.to_datetime(df['date'], errors='coerce')


df['hour'] = df['date'].dt.hour


hashtags_by_hour = df.groupby('hour')['text'].apply(lambda x: ' '.join(x).lower())
hashtags_by_hour = hashtags_by_hour.apply(lambda x: re.findall(r'#\w+', x))
hashtags_by_hour = hashtags_by_hour.apply(lambda x: Counter(x).most_common(10))


print(hashtags_by_hour)

