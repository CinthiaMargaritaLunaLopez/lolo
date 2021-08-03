import numpy as np
import matplotlib.pyplot as plt
 
x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([7,8,8,10,9,8,11,10,8,11])
plt.scatter(x,y)
plt.show()

px=np.mean(x)
py=np.mean(y)

num=np.sum((x-px)*(y-py))
den=np.sum((x-px)*(x-px))

pendiente=num/den

constante=py-pendiente*px

print(pendiente)
print(constante)
print("y={}+{}*x".format(constante,round(pendiente,4)))





#print(pendiente)
#print(constante)
#print("y={}+{}*x".format(constante,round(pendiente,4)))


#print(df.drop('Calificaciones',axis=1))
#df=df.drop('Calificaciones',axis=1)
#print(df)
#print(df.drop(4,axis=0)#NO
#cal=((df['P1']+ df['P2'])/2)

#df['x']=[1,2,3,4,5,6,7,8,9,10]
#df['Promedio']=cal
#print(df)








#cal=((df['P1']+ df['P2'])/2).mean()
#prom=df.loc[(df['P2']+ df['P1'])/2>cal,['Nombre','P1','P2']]
#print(cal)
#print(prom)




#eda=df['Edad']>23
#Nom=input('Pon el nombre: ')
#mat=df.loc[df['Nombre']==Nom,['Edad','Nombre']]

#parcial=df[df['P1']<df['P2']]
#print(parcial)
#Ed=df[[df['Edad']<25] and df['Pais']=='Argentina']


#Ed=df.loc[(df['Edad']<25) & (df['Pais']=='Argentina'),['Nombre']] 
#print(Ed)
#me=df['P1'].mean()
#mi=df['P1'].min()

#edad=df.loc[df['Edad']==df['Edad'].min(),['Pais','Edad']]
#print(edad)
#prom=df.loc[df['P1']<df['P1'].mean(),['P1','Nombre']]










#df=pd.Series(matriz)
#print(matriz.keys())
#print(matriz.values())
#print(df)
#para imprimir columnas 
#columna=df[['Nombre','Genero',]]
#Registro=df.loc[[3,6,7],['Nombre','Genero']]
#print(Registro)












#print (matriz.keys())
