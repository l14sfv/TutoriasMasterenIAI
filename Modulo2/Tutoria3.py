import matplotlib.pyplot as plt

# DATOS = TIEMPO EN MINUTOS

datos = { 5,7,8,12,20,50,40,30,20,5,3,6,9,10}

# HISTOGRAMA

# plt.hist(datos, bins=5, edgecolor="black")

# plt.title("Histograma de ejemplo")
# plt.xlabel("tiempo")
# plt.ylabel("frecuencia")

# plt.show()

# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Datos con observaciones

# data = {
#     "variable": ["A"] * 20 + ["B"] * 20 + ["C"] *20,
#     "valor": [
#         #A
#         10,12,11,13,14,10,12,11,13,11,
#         10,12,11,13,14,10,12,11,13,11,
#         #B
#         20,22,21,23,24,20,22,21,23,21,
#         20,22,21,23,24,20,22,21,23,21,
#         #C
#         15,17,16,18,19,15,18,17,16,15,
#         15,17,16,18,19,15,18,17,16,15
#     ]
# }

# df = pd.DataFrame(data)

# #Bloxplot 
# fig = px.box(df, x="variable", y="valor", title="Bloxplot por la media")

# #Promedios
# promedios = df.groupby("variable", as_index=False) ["valor"].mean()

# # vista

# for _, row in promedios.iterrows():
#     var = row["variable"]
#     media = row["valor"]
#     fig.add_hline(
#         y = media,
#         line_color="yellow",
#         line_dash="dash",
#         opacity = 1,
#     )

# fig.update_layout(showlegend=True)
# fig.write_image("ejemplo1.png")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Lenovo\Documents\DEV_SENIOR\IA C7\Modulo2\Housing_Price_Data.csv")

df_largo = df.melt(
    value_vars=["bathrooms", "bedrooms"],
    var_name = "variable",
    value_name = "valor"
)

fig, axes = plt.subplots(figsize=(12,5))
color = ["yellow", "darkred"]

for i, col in enumerate(["bathrooms", "bedrooms"]):
    df_largo[df_largo["variable"] == col]["valor"].plot(
        kind="hist",
        ax=axes[i],
        color=color[i],
        edgecolor = "white"
    )
    
    axes[i].set_title(f"{col}\nRango: [{df[col].min():.1f}, {df[col].max():.1f}]"),
    axes[i].set_ylabel("Numero"),
    axes[i].set_xlabel("Frecuencia"),
    
plt.tight_layout()
plt.show()
