import streamlit as st
import pandas as pd 

# Título con emoji y estilo
st.markdown("<h1 style='text-align: center; color: blue;'>🚔 Police Incident Reports from 2018 to 2020 in San Francisco 🚓</h1>", unsafe_allow_html=True)

# Cargar los datos
df = pd.read_csv("Policev1.csv")

# Mostrar una breve descripción con color y emojis
st.markdown("<h3 style='color: gray;'>📅 Datos de incidentes policiales en San Francisco entre 2018 y 2020</h3>", unsafe_allow_html=True)
st.markdown("<p style='color: darkgreen;'>Estos datos contienen información sobre los tipos de incidentes reportados, las ubicaciones y las fechas.</p>", unsafe_allow_html=True)

# Mostrar el DataFrame con estilo
st.dataframe(df.style.set_properties(**{'background-color': 'lavender', 'color': 'black'}))

# Resumen rápido con emojis
st.markdown("**🔍 Resumen de datos:**")
st.write(f"Total de incidentes: {len(df)}")
st.write(f"Columnas en el conjunto de datos: {', '.join(df.columns)}")

