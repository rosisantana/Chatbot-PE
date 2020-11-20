
import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.model_selection import train_test_split


arquivo_novo = pd.read_excel('Dados/casas_98058.xlsx')



def class_output(x):  #criando uma função para agregar os valores do output
    if(x<-0.5):
        return 0
    elif(x<0.5):
        return 1
    else:
        return 2
  
media_preco_sqft = arquivo_novo['preco_area_construida'].mean()#Calculando a média por metro quadrado 
desvpad_preco_sqft = arquivo_novo['preco_area_construida'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore = (arquivo_novo['preco_area_construida']-media_preco_sqft) / desvpad_preco_sqft   #Calculando o zscore
arquivo_novo['zscore']  = zscore #Incluindo zscore no DF backup

arquivo_novo['class'] = arquivo_novo['zscore'].apply(class_output) #Armazenamos os parâmetros do output numa função 'class' e automatizamos o processo com a função apply


#Discretizando Sqft_Living
def class_output_sqft(x):  #criando uma função para agregar os valores do output
    if(x<-0.5):
        return 0
    elif(x<0.5):
        return 1
    else:
        return 2
  
media_sqft_living = arquivo_novo['sqft_living'].mean() #Calculando a média
desvpad_sqft_living = arquivo_novo['sqft_living'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_sqft_living = (arquivo_novo['sqft_living']-media_sqft_living) / desvpad_sqft_living   #Calculando o zscore
arquivo_novo['zscore_sqft_living']  = zscore_sqft_living #Incluindo zscore no DF backup

arquivo_novo['sqft_living_discretizado'] = arquivo_novo['zscore_sqft_living'].apply(class_output_sqft) #Armazenamos os parâmetros do output numa função 'class' e automatizamos o processo com a função apply

#Discretizando Sqft_Lot

media_sqft_lot = arquivo_novo['sqft_lot'].mean() #Calculando a média
desvpad_sqft_lot = arquivo_novo['sqft_lot'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_sqft_lot = (arquivo_novo['sqft_lot']-media_sqft_lot) / desvpad_sqft_lot   #Calculando o zscore
arquivo_novo['zscore_sqft_lot']  = zscore_sqft_lot #Incluindo zscore no DF backup

arquivo_novo['sqft_lot_discretizado'] = arquivo_novo['zscore_sqft_lot'].apply(class_output_sqft) #Armazenamos os parâmetros do output numa função 'class' e automatizamos o processo com a função apply

#Discretizando bedrooms
media_bedrooms = arquivo_novo['bedrooms'].mean() #Calculando a média
desvpad_bedrooms = arquivo_novo['bedrooms'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_bedrooms = (arquivo_novo['bedrooms']-media_bedrooms) / desvpad_bedrooms   #Calculando o zscore
arquivo_novo['zscore_bedrooms']  = zscore_bedrooms #Incluindo zscore no DF backup

arquivo_novo['bedrooms_discretizado'] = arquivo_novo['zscore_bedrooms'].apply(class_output_sqft)

#Discretizando bathrooms

media_bathrooms = arquivo_novo['bathrooms'].mean() #Calculando a média
desvpad_bathrooms = arquivo_novo['bathrooms'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_bathrooms = (arquivo_novo['bathrooms']-media_bathrooms) / desvpad_bathrooms   #Calculando o zscore
arquivo_novo['zscore_bathrooms']  = zscore_bathrooms #Incluindo zscore no DF backup

arquivo_novo['bathrooms_discretizado'] = arquivo_novo['zscore_bathrooms'].apply(class_output_sqft)

#Discretizando floors
media_floors = arquivo_novo['floors'].mean() #Calculando a média
desvpad_floors = arquivo_novo['floors'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_floors = (arquivo_novo['floors']-media_floors) / desvpad_floors   #Calculando o zscore
arquivo_novo['zscore_floors']  = zscore_floors #Incluindo zscore no DF backup

arquivo_novo['floors_discretizado'] = arquivo_novo['zscore_floors'].apply(class_output_sqft)

#Discretizando a View
media_view = arquivo_novo['view'].mean() #Calculando a média
desvpad_view = arquivo_novo['view'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_view = (arquivo_novo['view']-media_view) / desvpad_view   #Calculando o zscore
arquivo_novo['zscore_view']  = zscore_view #Incluindo zscore no DF backup

arquivo_novo['view_discretizado'] = arquivo_novo['zscore_view'].apply(class_output_sqft)

#Discretizando o yr_renovated

media_yr_renovated = arquivo_novo['yr_renovated'].mean() #Calculando a média
desvpad_yr_renovated = arquivo_novo['yr_renovated'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_yr_renovated = (arquivo_novo['yr_renovated']-media_yr_renovated) / desvpad_yr_renovated   #Calculando o zscore
arquivo_novo['zscore_yr_renovated']  = zscore_yr_renovated #Incluindo zscore no DF backup

arquivo_novo['yr_renovated_discretizado'] = arquivo_novo['zscore_yr_renovated'].apply(class_output_sqft)

#Discretizando o grade

media_grade = arquivo_novo['grade'].mean() #Calculando a média
desvpad_grade = arquivo_novo['grade'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_grade = (arquivo_novo['grade']-media_grade) / desvpad_grade   #Calculando o zscore
arquivo_novo['zscore_grade']  = zscore_grade #Incluindo zscore no DF backup

arquivo_novo['grade_discretizado'] = arquivo_novo['zscore_grade'].apply(class_output_sqft)

#Discretizando o yr_built

media_yr_built = arquivo_novo['yr_built'].mean() #Calculando a média
desvpad_yr_built = arquivo_novo['yr_built'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore_yr_built = (arquivo_novo['yr_built']-media_yr_built) / desvpad_yr_built   #Calculando o zscore
arquivo_novo['zscore_yr_built']  = zscore_yr_built #Incluindo zscore no DF backup

arquivo_novo['yr_built_discretizado'] = arquivo_novo['zscore_yr_built'].apply(class_output_sqft)

# Separando as 10 últimas linhas para usar como autoavaliação ao final do desenvolvimento do chatbot
autoavaliacao = arquivo_novo.tail(10)

# Eliminando as 10 ultimas linhas para não serem mais usadas durante a criação do chatbot
arquivo_novo = arquivo_novo[:-10]

# Exportando os dados das casas para processo de construção do chatbot como 'CasasTop.csv'
#arquivo_novo.to_csv(r'CasasTop.csv', index=False)

# Exportando as 10 casas para serem usadas na autoavaliação do chatbot
autoavaliacao.drop(['zscore_sqft_living','zscore_sqft_lot', 'zscore_bedrooms','zscore_bathrooms', 'zscore_floors', 'zscore_view', 'zscore_grade', 'zscore_yr_built', 'zscore_yr_renovated', 'zscore', 'price','bedrooms', 'bathrooms', 'sqft_living','sqft_lot', 'floors','view', 'condition','grade', 'sqft_above', 
'sqft_basement','yr_built','yr_renovated',	'preco_area_construida','zipcode'], axis='columns', inplace=True)
autoavaliacao.to_csv(r'autoavaliacao.csv', index=False)

#Discretizando Sqft_Living
# sqft_livingT=[]

# sqft_living = arquivo_novo['sqft_living'].values

# for sqft in sqft_living:
#   sqft_livingT.append([sqft])
# kmeans_sqft = KMeans(n_clusters=2, random_state=0).fit(sqft_livingT)

# sqft_living_disc=[]
# for sqft in sqft_living:
#   sqft_disc=kmeans_sqft.predict([[sqft]])
#   sqft_living_disc.append(sqft_disc[0])

# arquivo_novo['sqft_discretizado']=sqft_living_disc

#arquivo_novo.to_csv(r'Dados/casas_98058_tratada.csv', index=False)

arquivo_novo.drop(['zscore_sqft_living','zscore_sqft_lot', 'zscore_bedrooms','zscore_bathrooms', 'zscore_floors', 'zscore_view', 'zscore_grade', 'zscore_yr_built', 'zscore_yr_renovated', 'zscore'], axis='columns', inplace=True)

arquivo_novo.to_csv(r'Dados/VAI_DAR_CERTO.csv', index=False)