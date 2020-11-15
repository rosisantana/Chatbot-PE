import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
import graphviz 
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38\bin'

df_casa = pd.read_excel('casas_98058.xlsx')
#df_preco = pd.read_excel('house_data_tratada.xlsx')
df_preco = df_casa[['caro_ou_barato?']]
df_casa.drop(['preco_area_construida', 'caro_ou_barato?'], axis='columns', inplace=True)

clf = tree.DecisionTreeClassifier(min_samples_leaf=8, min_impurity_decrease=0.002)
clf = clf.fit(df_casa, df_preco)

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=df_casa.columns,  
                                filled=True, rounded=True,  
                                special_characters=True)
graph = graphviz.Source(dot_data) 
graph.render("Arvore") 

