import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Analisis de vehiculos Proyecto Sprint 6')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



build_scatter = st.checkbox('Construir un scatter')
 # crear un botón
        
if build_scatter: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un scatterplot para el conjunto de datos de anuncios de venta de coches')
            
    # crear un scatterplot
    fig = px.scatter(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() # crear gráfico de dispersión