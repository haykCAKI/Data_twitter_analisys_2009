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
Análise de Menções de Usuários:

Extrai menções de usuários (@username) dos textos dos tweets usando expressões regulares.
Conta a frequência de cada menção de usuário e visualiza os 20 usuários mais mencionados.
Análise Temporal:

Converte a coluna 'date' para o formato datetime.
Extrai a hora do dia dos timestamps e adiciona como uma nova coluna ('hour').
Análise de Hashtags por Hora:

Agrupa os tweets por hora e extrai hashtags (#hashtag) usando expressões regulares.
Conta a frequência de cada hashtag por hora e imprime os 10 hashtags principais para cada hora.
Saída
O script gera visualizações de frequência de palavras e menções de usuários, além de imprimir as principais hashtags por hora no console.
