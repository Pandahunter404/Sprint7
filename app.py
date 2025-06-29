import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
         # encabezado
         st.header('Análisis de distribución de kilometraje en vehículos')

         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)
         
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón de dispersión
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje')
    
    # Crear gráfico de dispersión (precio vs odómetro)
    fig_scatter = px.scatter(car_data, 
                           x="odometer", 
                           y="price", 
                           color="condition",  # Opcional: colorear por condición
                           title="Relación Precio-Kilometraje")
    
    st.plotly_chart(fig_scatter, use_container_width=True)