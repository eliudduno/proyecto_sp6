import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('./vehicles_us.csv')

# Encabezado de la aplicacion con streamlit
st.header('Encabezado inicial de la aplicacion')

# creando un boton para iniciar la ejecución
histo_inicio = st.button('Mostrar histograma')

if histo_inicio:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crea un histograma
    fig = px.histogram(car_data, x='odometer',
                       title='Histograma de precios de los vehículos')
    # mostrar un grafico pltoly interactivo
    st.plotly_chart(fig, use_container_width=True)
