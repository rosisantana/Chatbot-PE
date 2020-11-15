import pandas as pd
from sklearn.cluster import KMeans
#from sklearn.model_selection import train_test_split

pricesT=[]

arquivo = pd.read_excel('Dados/casas_98058.xlsx')
prices= arquivo['price'].values

for price in prices:
  pricesT.append([price])
kmeans_price = KMeans(n_clusters=3, random_state=0).fit(pricesT)

prices_disc=[]
for price in prices:
  price_disc=kmeans_price.predict([[price]])
  prices_disc.append(price_disc[0])

arquivo['valores_discretizados']=prices_disc

arquivo.to_csv(r'Dados/casas_98058_tratada.csv', index=False)


