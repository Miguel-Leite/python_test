import sqlite3
import pandas as pd


df = pd.read_csv('/home/miguel/Documentos/Teste-Python/graphene-django-x/sam.csv')
df['id'] = df.index
df=df[['id','Segment','Country','Product','Units','Sales','Datesold']]
df.on_sql('gqlapp_productmode', if_exists='replace', index=False)

 
 