import pandas as pd 
import plotly.express as px 
import streamlit as st
car_data = pd.read_csv('C:/Users/User_01/RESCATE_PROYECTO6/vehicles_us.csv')

hist_button = st.button('Construir histograma')

if hist_button: #al hacer click en el boton 
    st.write('Te presentamos un histograma para el conjunto de datos de anuncios de venta de vehiculos')
    
    #crear un histograma
    fig = px.histogram(car_data, x="odometer", title= "Histograma de kilometraje")
    
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    

hist_secondbutton = st.button('Construir gráfico de dispersión')

if hist_secondbutton: 
    st.write('Conoce a través de un gráfico de dispersión la relación del kilometraje y precios de vehiculos')
    
    #crear un gráfico de dispersión
    grafico = px.scatter(car_data, x="odometer", y="price", title="Dispersion entre Kilomentraje y Precio")
    
    #mostrar gráfico 
    st.plotly_chart(grafico, use_container_width=True)
    