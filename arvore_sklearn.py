import pandas as pd
from sklearn import tree
import graphviz

df_casa = pd.read_csv('Dados/VAI_DAR_CERTO.csv')
df_preco = df_casa[['class']]
df_casa.drop(['price','bedrooms', 'bathrooms', 'sqft_living','sqft_lot', 'floors','view', 'condition','grade', 'sqft_above', 
'sqft_basement','yr_built','yr_renovated',	'preco_area_construida','zipcode','zscore', 'class'], axis='columns', inplace=True)

clf = tree.DecisionTreeClassifier(min_samples_leaf=6, min_impurity_decrease=0.002) #<- TUDO DE BOM 
clf = clf.fit(df_casa, df_preco)

# x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2)
# clf.fit(x_train, y_train)
# predictions=clf.predict(x_test)
# print(accuracy_score(y_test,predictions))

dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names=df_casa.columns,  
                                    impurity=True,
                                    filled=True, rounded=True,  
                                    #class_names = ['Abaixo','Na média', 'Acima'],
                                    special_characters=True)
graph = graphviz.Source(dot_data) 
graph.render("arvore_de_decisao1") 

