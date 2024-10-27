from sklearn.datasets import load_breast_cancer

breas_cancer = load_breast_cancer()
# print(dir(breas_cancer))
X = breas_cancer.data
Y = breas_cancer.feature_names
Z = breas_cancer.target

import pandas as pd

data_frame = pd.DataFrame(X, columns=Y)

# Dividimos el conjunto de datos

from sklearn.model_selection import train_test_split

X_train, X_trest, Z_train, Z_test = train_test_split(data_frame, Z, stratify=Z)

print("Tamaño del conjunto de datos de entrenamiento: ", len(X_train))
print("Tamaño del conjunto de datos de pruebas: ", len(Z_test))