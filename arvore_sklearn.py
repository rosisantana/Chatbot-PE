import pandas as pd
from sklearn import tree
import graphviz

#Gerando árvore de decisão
df_casa = pd.read_csv('Dados/discretized_data.csv')
df_preco = df_casa[['new_price']]
df_casa.drop(['new_price'], axis='columns', inplace=True)

clf = tree.DecisionTreeClassifier(min_samples_leaf=6, min_impurity_decrease=0.002) #<- TUDO DE BOM 
clf = clf.fit(df_casa, df_preco)

dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names=df_casa.columns,  
                                    impurity=True,
                                    filled=True, rounded=True,  
                                    class_names = ['Abaixo','Na média', 'Acima'],
                                    special_characters=True)
graph = graphviz.Source(dot_data) 
graph.render("arvore_decisao_final") 

