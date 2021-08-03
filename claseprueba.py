import pandas as pd
df=pd.read_csv('C:/Users/lenovo/Documents/APython/canciones-2018.csv')
#print(df.head(5))
#print(df.tail())
#print(df.shape)

#can=df.loc[df['duration_ms']==df['duration_ms'].min(),['name','artists','duration_ms']]
#print(df.sort_values('duration_ms',ascending=True))
df=df.sort_values('duration_ms',ascending=False)
can=df.loc[((df['artists']=='Post Malone') | (df['artists']=='Drake') ),('name','artists','duration_s')]
print(can)

