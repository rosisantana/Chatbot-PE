
import pandas as pd

#Lendo os dados como Dataframe do Pandas
df_casa = pd.read_excel('Dados/house_data.xlsx')

#Filtrando o CEP: 98058
df_casa = df_casa[df_casa['zipcode'] == 98058]

#Deletando as colunas que não serão utilizadas
df_casa.drop(['id', 'date', 'waterfront', 'condition', 'sqft_above', 'sqft_basement' , 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15'], axis='columns', inplace=True)


#Calculando preço por área construída e inserindo como uma nova coluna na tabela
preco_area_construida = df_casa['price'] / df_casa['sqft_living']
df_casa['preco_area_construida'] = preco_area_construida

#criando uma função para determinar valores se saída da discretização
def output(x):  
    if(x<-0.5):
        return 0
    elif(x<0.5):
        return 1
    else:
        return 2

#Calculando a média, desvio padrão e zscore do 'preço por área construída' e utilizando a função output e apply'
media_preco_sqft = df_casa['preco_area_construida'].mean()
desvpad_preco_sqft = df_casa['preco_area_construida'].std()
zscore = (df_casa['preco_area_construida']-media_preco_sqft) / desvpad_preco_sqft 

df_casa['zscore']  = zscore 
df_casa['new_price'] = df_casa['zscore'].apply(output) 

#Calculando a média, desvio padrão e zscore do 'bedrooms' e utilizando a função output e apply  
media_bedrooms = df_casa['bedrooms'].mean() 
desvpad_bedrooms = df_casa['bedrooms'].std()  
zscore_bedrooms = (df_casa['bedrooms']-media_bedrooms) / desvpad_bedrooms

df_casa['zscore_bedrooms']  = zscore_bedrooms
df_casa['new_bedrooms'] = df_casa['zscore_bedrooms'].apply(output)

#Calculando a média, desvio padrão e zscore do 'bathrooms' e utilizando a função output e apply  
media_bathrooms = df_casa['bathrooms'].mean() 
desvpad_bathrooms = df_casa['bathrooms'].std()
zscore_bathrooms = (df_casa['bathrooms']-media_bathrooms) / desvpad_bathrooms

df_casa['zscore_bathrooms']  = zscore_bathrooms
df_casa['new_bathrooms'] = df_casa['zscore_bathrooms'].apply(output)

#Calculando a média, desvio padrão e zscore do 'sqft_living' e utilizando a função output e apply  
media_sqft_living = df_casa['sqft_living'].mean() 
desvpad_sqft_living = df_casa['sqft_living'].std() 
zscore_sqft_living = (df_casa['sqft_living']-media_sqft_living) / desvpad_sqft_living

df_casa['zscore_sqft_living']  = zscore_sqft_living 
df_casa['new_sqft_living'] = df_casa['zscore_sqft_living'].apply(output)

#Calculando a média, desvio padrão e zscore do 'sqft_lot' e utilizando a função output e apply  
media_sqft_lot = df_casa['sqft_lot'].mean()
desvpad_sqft_lot = df_casa['sqft_lot'].std()
zscore_sqft_lot = (df_casa['sqft_lot']-media_sqft_lot) / desvpad_sqft_lot

df_casa['zscore_sqft_lot']  = zscore_sqft_lot
df_casa['new_sqft_lot'] = df_casa['zscore_sqft_lot'].apply(output)

#Calculando a média, desvio padrão e zscore do 'floors' e utilizando a função output e apply  
media_floors = df_casa['floors'].mean()
desvpad_floors = df_casa['floors'].std()
zscore_floors = (df_casa['floors']-media_floors) / desvpad_floors

df_casa['zscore_floors']  = zscore_floors
df_casa['new_floors'] = df_casa['zscore_floors'].apply(output)

#Calculando a média, desvio padrão e zscore do 'View' e utilizando a função output e apply  
media_floors = df_casa['view'].mean()
media_view = df_casa['view'].mean()
desvpad_view = df_casa['view'].std()
zscore_view = (df_casa['view']-media_view) / desvpad_view

df_casa['zscore_view']  = zscore_view
df_casa['new_view'] = df_casa['zscore_view'].apply(output)

#Calculando a média, desvio padrão e zscore do 'grade' e utilizando a função output e apply  
media_grade = df_casa['grade'].mean() 
desvpad_grade = df_casa['grade'].std()
zscore_grade = (df_casa['grade']-media_grade) / desvpad_grade

df_casa['zscore_grade']  = zscore_grade
df_casa['new_grade'] = df_casa['zscore_grade'].apply(output)

#Calculando a média, desvio padrão e zscore do 'yr_built' e utilizando a função output e apply  
media_yr_built = df_casa['yr_built'].mean() 
desvpad_yr_built = df_casa['yr_built'].std()
zscore_yr_built = (df_casa['yr_built']-media_yr_built) / desvpad_yr_built

df_casa['zscore_yr_built']  = zscore_yr_built
df_casa['new_yr_built'] = df_casa['zscore_yr_built'].apply(output)

#Calculando a média, desvio padrão e zscore do 'yr_renovated' e utilizando a função output e apply  
media_yr_renovated = df_casa['yr_renovated'].mean() 
desvpad_yr_renovated = df_casa['yr_renovated'].std()
zscore_yr_renovated = (df_casa['yr_renovated']-media_yr_renovated) / desvpad_yr_renovated

df_casa['zscore_yr_renovated']  = zscore_yr_renovated
df_casa['new_yr_renovated'] = df_casa['zscore_yr_renovated'].apply(output)

#Armazenando as 10 últimas linhas na variável 'dados_avaliação'
dados_autoavaliacao = df_casa.tail(10)

#Eliminando as 10 últimas linhas para que não participem do treinamento do chatbot
df_casa = df_casa[:-10]

#Exportando o arquivo csv para a autoavaliação e retirando as colunas que não serão utilizadas
dados_autoavaliacao.drop(['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'view', 'grade', 'yr_built', 'yr_renovated', 'preco_area_construida', 'zscore', 'zscore_bedrooms'
, 'zscore_bathrooms', 'zscore_sqft_living', 'zscore_sqft_lot', 'zscore_floors', 'zscore_view', 'zscore_grade', 'zscore_yr_built', 'zscore_yr_renovated'], axis='columns', inplace=True)
dados_autoavaliacao.to_csv(r'dados_autoavaliacao.csv', index=False)

#Exportando arquivo para utilizar na geração da arvore de decisão e deletando colunas que não serão utilizadas para isso
df_casa.drop(['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'view', 'grade', 'yr_built', 'yr_renovated', 'preco_area_construida', 'zscore', 'zscore_bedrooms'
, 'zscore_bathrooms', 'zscore_sqft_living', 'zscore_sqft_lot', 'zscore_floors', 'zscore_view', 'zscore_grade', 'zscore_yr_built', 'zscore_yr_renovated'], axis='columns', inplace=True)
df_casa.to_csv(r'Dados/discretized_data.csv', index=False)
