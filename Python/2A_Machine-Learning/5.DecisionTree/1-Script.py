# Script Python de la siguiente clase

# pip install mysql-connector-python

###### conectamos y extraemos los datos

import mysql.connector
import pandas as pd

# Database connection
mydb = mysql.connector.connect(
    host="xxxxxxx",  #tu host
    user="xxxxxxx",  # tu usuario de base de datos MySQL
    password="xxxxxxxx", #tu contraseña de MySQL
    database="appdaist_test"
)

# SQL Query for the preparation of the data that will later be analyzed by the algorithm
query = '''
    SELECT 
    CASE WHEN T0.genero='femenino' THEN 1 
    WHEN T0.genero='masculino' THEN 2 
    ELSE 3 END as sexo, 
    CASE WHEN T0.origen='udemy' THEN 1 
    WHEN T0.origen='frogames' THEN 2 
    WHEN T0.origen='crehana' THEN 3 
    WHEN T0.origen='facebook' THEN 4 
    WHEN T0.origen='web' THEN 5 
    ELSE 6 END as source,
    T0.edad,T1.corr as curso, 
    CASE WHEN T0.tickmarks <7 THEN 'Detractor' 
    WHEN T0.tickmarks >8 THEN 'Promotor' 
    ELSE 'Pasivo' END as Clasificacion 
    FROM `tb_nps` T0 JOIN curso_nps T1 on T0.producto = T1.idSELECT
'''

df = pd.read_sql(query,mydb)

mydb.close()

######### simplemente exploramos los datos
print(df.info())

print(df)

df.shape

import seaborn as sb
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from IPython.display import Image as PImage
from subprocess import check_call
from PIL import Image, ImageDraw, ImageFont

df.groupby('Clasificacion').size()

sb.factorplot('Clasificacion', data=df,kind='count')

######### separamos los datos - creamos el modelo - entrenamos y testeamos
import numpy as np
from sklearn.model_selection import train_test_split
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

df.groupby('Clasificacion').size()

train, test = train_test_split(df, test_size = 0.4, stratify = df['Clasificacion'], random_state = 10)

X_train = train[['sexo','source','edad','curso']]
y_train = train.Clasificacion
X_test = test[['sexo','source','edad','curso']]
y_test = test.Clasificacion

######### Evaluamos el desempeño
mod_dt = DecisionTreeClassifier(max_depth = 3, random_state = 1)
mod_dt.fit(X_train,y_train)
predicción=mod_dt.predict(X_test)
print('La precisión del árbol de decisión es',"{:.3f}".format( metrics.accuracy_score(predicción,y_test)))

############ creamos la gráfica del árbol
fn=['sexo','source','edad','curso']
cn=['promotores','detractores','pasivos']
plt.figure(figsize = (10,8))
plot_tree(mod_dt, feature_names = fn, class_names = cn, proportion= True, filled = True);

disp = metrics.plot_confusion_matrix(mod_dt, X_test, y_test, display_labels =cn, cmap=plt.cm.Blues, normalize=None)
disp.ax_.set_title('Matriz de confusión del árbol de decisión, sin normalización');

feat_importance = mod_dt.tree_.compute_feature_importances(normalize=True)
print("feat importance = " + str(feat_importance))
