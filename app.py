import streamlit as st
import pandas as pd
# import plotly.express as px
import plotly.express as px


car_data = pd.read_csv('./vehicles_us.csv')

# Encabezado de la aplicacion con streamlit
st.header('Datos de Vehiculos mostrados en Graficos (Histogramas - Dispersión)')

seleccion_histograma = st.checkbox('Grafico Histograma')
seleccion_dispersion = st.checkbox('Graficos Dispersión')

if seleccion_histograma:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crea un histograma
    fig = px.histogram(car_data, x='odometer',
                       title='Cantidad de Vehiculos segun su odometro')

    # mostrar un grafico pltoly interactivo
    st.plotly_chart(fig, use_container_width=True)

if seleccion_dispersion:
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # grafico disperción
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Precio del vehiculo segun la distancia recorrida')

    st.plotly_chart(fig, use_container_width=True)
