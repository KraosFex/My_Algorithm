# Script Python de la Siguiente clase adaptado a Power BI

import mysql.connector
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from IPython.display import Image as PImage
from subprocess import check_call
from PIL import Image, ImageDraw, ImageFont
from sklearn.model_selection import train_test_split
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

train, test = train_test_split(dataset, test_size = 0.4, stratify = dataset['Clasificacion'], random_state = 10)

X_train = train[['sexo','source','edad','curso']]
y_train = train.Clasificacion
X_test = test[['sexo','source','edad','curso']]
y_test = test.Clasificacion

mod_dt = DecisionTreeClassifier(max_depth = 3, random_state = 1)
mod_dt.fit(X_train,y_train)
predicción=mod_dt.predict(X_test)
print('La precisión del árbol de decisión es',"{:.3f}".format( metrics.accuracy_score(predicción,y_test)))

mod_dt.feature_importances_
fn=['sexo','source','edad','curso']
cn=['promotores','detractores','pasivos']
plt.figure(figsize = (10,8))
plot_tree(mod_dt, feature_names = fn, class_names = cn, proportion= True, filled = True);

plt.show()
