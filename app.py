import pandas as pd 
import plotly.express as px 
import streamlit as st
car_data = pd.read_csv('C:/Users/User_01/RESCATE_PROYECTO6/vehicles_us.csv')


# Título principal
hist_titulo = st.title('Conoce todo sobre tu próximo vehículo')

# Encabezado
hist_encabezado = st.header('¡Consulta aquí la información necesaria de cada modelo y asegura tu compra!')


hist_button = st.button('Construir histograma por kilometraje')

if hist_button: #al hacer click en el boton 
    st.write('Conoce cuántos modelos están a tu disposición con base al kilometraje de vehículos')
    
    #crear un histograma
    fig = px.histogram(car_data, x="odometer", title= 'Histograma del total de vehículos por kilometraje')
    
    fig.update_layout(
    xaxis_title="Kilometraje",
    yaxis_title="Frecuencia"
)
    
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    

hist_secondbutton = st.button('Construir gráfico de dispersión de precios')

if hist_secondbutton: 
    st.write('Conoce a través de un gráfico de dispersión la relación del kilometraje y precios de vehículos')
    
    #crear un gráfico de dispersión
    grafico = px.scatter(car_data, x="odometer", y="price", title="Dispersión entre Kilomentraje y Precio")
    
    grafico.update_layout(
    xaxis_title="Kilometraje",
    yaxis_title="Costo")
    
    #mostrar gráfico 
    st.plotly_chart(grafico, use_container_width=True)
    

# Casilla de verificacion para construir un histograma nuevo
hist_histogram = st.checkbox('Construir histograma por modelos')

if hist_histogram: 
    st.write('Consulta el rango de precios de nuestros modelos y elige lo que más se adapte a ti')
    
    #crear un histograma
    fig2 = px.histogram(car_data, x="price", y="model", title= 'Histograma del total de vehículos por kilometraje')
    
    fig2.update_layout(
    xaxis_title="Costo",
    yaxis_title="Modelo")
    
    #mostrar un gráfico2 Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)


