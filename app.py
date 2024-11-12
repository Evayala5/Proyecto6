import pandas as pd 
import plotly.express as px 
import streamlit as st
car_data = pd.read_csv('G:/EVA/CIENCIA DE DATOS TRIPLE TEN/6to Sprint/Documentos vS Code/mi_proyectoseis/Proyecto6/vehicles_env/vehicles_us.csv')

hist_button = st.button('construir histograma')

if hist_button: #al hacer click en el boton 
    st.write('creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    #crear un histograma
    fig = px.histogram(car_data, x="odometer", title= "Histograma de Odometer")
    
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    

hist_secondbutton = st.button('gráfico de dispersión')

if hist_secondbutton: 
    st.write('creación de gráfico de dispersión')
    
    #crear un gráfico de dispersión
    grafico = px.scatter(car_data, x="odometer", y="price", title="Dispersion entre Odometro y Precio")
    
    #mostrar gráfico 
    st.plotly_chart(grafico, use_container_width=True)
    