import pandas as pd
from sklearn import tree
import graphviz

df_casa = pd.read_csv('Dados/casas_98058_tratada.csv')
df_preco = df_casa[['valores_discretizados']]
df_casa.drop(['valores_discretizados','preco_area_construida', 'price'], axis='columns', inplace=True)

clf = tree.DecisionTreeClassifier(min_samples_leaf=7, min_impurity_decrease=0.001)
clf = clf.fit(df_casa, df_preco)

dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names=df_casa.columns,  
                                    impurity=True,
                                    filled=True, rounded=True,  
                                    #class_names = ['Abaixo','Na média', 'Acima'],
                                    special_characters=True)
graph = graphviz.Source(dot_data) 
graph.render("arvore_de_decisao") 

