import streamlit as st
import pandas as pd 
st.markdown("<h1 style='text-align: center; color: blue;'>🚔 Police Incident Reports from 2018 to 2020 in San Francisco 🚓</h1>", unsafe_allow_html=True)
df= pd.read_csv("Policev1.csv")
st.markdown ('The data shown below belongs to incident reports in the city of San Francisco from the year 2018 to 2020 with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution ')
mapa=pd.DataFrame()
mapa['Date']=df['Incident Date']
mapa['Day']=df['Incident Day of Week']
mapa['Polica District']=df['Police District']
mapa['Neighborhood']=df['Analysis Neighborhood']
mapa['Incident Category']=df['Incident Category']
mapa['Resolution']=df['Resolution']
mapa['lat']=df['Latitude']
mapa['lon']=df['Longitude']
mapa=mapa.dropna()

df

