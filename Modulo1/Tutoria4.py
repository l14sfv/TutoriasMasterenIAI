#numpy === arrays, y operaciones aritmeticas con arrays

#pandas === dataframes, series, y operaciones con dataframes y series

#scikit-learn === machine learning, algoritmos de aprendizaje supervisado y no supervisado, preprocesamiento de datos, evaluación de modelos, etc.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

datos = {
    'edad': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'salario': [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    'experiencia': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
}

#dataframe
df = pd.DataFrame(datos)
print(df)
print(df.describe())
print(df.head())

#dividir los datos
x = df[['edad', 'experiencia']]
y = df['salario']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f"\n Datos de entrenamiento:\n{x_train}\n{y_train}")
print(f"\n Datos de prueba:\n{x_test}\n{y_test}")


#crear y entrenar modelos
modelo = LinearRegression()
modelo.fit(x_train, y_train)

print(("\n 🤖Modelo entrenado 🧑🏻‍🏫"))
print(f"\n Coeficientes: {modelo.coef_}")
print(f"\n Intercepto: {modelo.intercept_}")

#predecir
y_pred = modelo.predict(x_test)

comparacion = pd.DataFrame({'Actual': y_test, 'Predicho': np.round(y_pred, 2)})

print("\n Comparación entre valores reales y predichos:")
print(comparacion)

#prediccion de un nuevo dato

nuevo_empleado = np.array([[28, 8]])  # edad: 28 años, experiencia: 4 años

salario_predicho = modelo.predict(nuevo_empleado)
print(f"\n Nuevo empleado")
print(f"salario predicho: {salario_predicho[0]:.2f}")

#metricas de evaluacion
mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print(f"\n Métricas de evaluación:")
print("MSE:", mse)
print("R²:", r2)

#graficarlo
plt.figure(figsize=(10, 6))
plt.scatter(df['edad'], df['salario'], color='blue', label='Datos reales')
plt.plot([y_test.min(), y_test.max()], [modelo.predict([[y_test.min(), 0]])[0], modelo.predict([[y_test.max(), 0]])[0]], color='red', label='Línea de regresión')

plt.xlabel('Salario')
plt.ylabel('Edad')
plt.title('Regresión Lineal')
plt.legend()
plt.grid(True)
plt.show()
