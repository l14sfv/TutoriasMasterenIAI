#procesamiento y calidad de datos
import pandas as pd
import numpy as np
import duckdb

df = pd.read_csv("estudiantes.csv")

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isna().sum())
# print(df.duplicated().sum())

#limpieza de los datos

#1. duplicados
df = df.drop_duplicates()

#2. filtro de valores atípicos
# df = df[df["calificacion"] <= 10]
df = df[(df["edad"] > 15  ) & (df["edad"] < 80)]

#3. corregir notas fuera del rango
df.loc[df["nota_final"] < 0, "nota_final"] = 0
df.loc[df["nota_final"] > 10, "nota_final"] = 10

#4. datos faltantes
df["nota_final"] = df["nota_final"].fillna(df["nota_final"].mean())
df["edad"] = df["edad"].fillna(df["edad"].median())
df["asistencia"] = df["asistencia"].fillna(df["asistencia"].median())

df = df.dropna(subset=["nota_final"])

#5. normalizacion de datos
df["programa"] = df["programa"].str.strip().str.lower()

#6. codificacion de variables categoricas
df = pd.get_dummies(df, columns=["programa"], drop_first=True)

#7. manejo de fechas
df["fecha_inscripcion"] = pd.to_datetime(df["fecha_inscripcion"], errors="coerce")
df["fecha_inscripcion"] = df["fecha_inscripcion"].fillna(df["fecha_inscripcion"].median())

#8. 

#entrenamiento del modelo

df["en riesgo"] = (df["nota_final"] < 6).astype(int)

X = df[["edad", "nota_final", "asistencia"]]
Y = df["en riesgo"]

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#dividr los datos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#procesamiento numerico
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
Y_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, Y_train)

y_pred = model.predict(Y_test_scaled)
procentaje_respuesta = accuracy_score(Y_test, y_pred) * 100
print(f"El porcentaje de respuesta es: {procentaje_respuesta:.2f}%")

#NUMPY
import numpy as np
#PANDAS
import pandas as pd
#POLARS
import matplotlib.pyplot as plt
#PYARROW
import pyarrow as pa
#CUPY
import cupy as cp
#DASK
import dask.dataframe as dd
#DUCKDB
import duckdb

#spacy
tokeninazacion = spacy.load("en_core_web_sm")
POS TAGGING 
#nltk

