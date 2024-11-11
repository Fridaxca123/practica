import streamlit as st
import pandas as pd 

# Título con formato HTML
st.markdown("<h1 style='text-align: center; color: blue;'>🚔 Police Incident Reports from 2018 to 2020 in San Francisco 🚓</h1>", unsafe_allow_html=True)

# Cargar el archivo CSV
df = pd.read_csv("Policev1.csv")

# Descripción de los datos
st.markdown('The data shown below belongs to incident reports in the city of San Francisco from the year 2018 to 2020 with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

# Crear el DataFrame de mapa con las columnas relevantes
mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()

# Filtrado de datos en la barra lateral
police_district_input = st.sidebar.multiselect(
    'Police District',
    mapa['Police District'].unique()
)

# Filtrado por distrito de policía
subset_data = mapa
if len(police_district_input) > 0:
    subset_data = mapa[mapa['Police District'].isin(police_district_input)]

# Filtrado por vecindario
neighborhood_input = st.sidebar.multiselect(
    'Neighborhood',
    subset_data['Neighborhood'].unique()
)

if len(neighborhood_input) > 0:
    subset_data = subset_data[subset_data['Neighborhood'].isin(neighborhood_input)]

# Mostrar el DataFrame filtrado
st.dataframe(subset_data)



