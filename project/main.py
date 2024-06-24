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
