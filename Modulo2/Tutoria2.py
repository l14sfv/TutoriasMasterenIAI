# import deepface
# import face_recognition
# import insightface


# Stable Diffusion
# Pytorch
# TensorFlow

# OpenCV 
# Scikit-image  => Numpy y a SciPy

#Ejemplo con datos aleatorios

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Datos con observaciones

data = {
    "variable": ["A"] * 20 + ["B"] * 20 + ["C"] *20,
    "valor": [
        #A
        10,12,11,13,14,10,12,11,13,11,
        10,12,11,13,14,10,12,11,13,11,
        #B
        20,22,21,23,24,20,22,21,23,21,
        20,22,21,23,24,20,22,21,23,21,
        #C
        15,17,16,18,19,15,18,17,16,15,
        15,17,16,18,19,15,18,17,16,15
    ]
}

df = pd.DataFrame(data)

#Bloxplot 
fig = px.box(df, x="variable", y="valor", title="Bloxplot por la media")

#Promedios
promedios = df.groupby("variable", as_index=False) ["valor"].mean()

# vista

for _, row in promedios.iterrows():
    var = row["variable"]
    media = row["valor"]
    fig.add_hline(
        y=media,
        line=dict(color="green", dash="dash"),
        name=f"Media {var}",
        x0=var,
        x1=var
    )

fig.update_layout(showlegend=True)
fig.write_image("ejemplo.png")