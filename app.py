import pandas as pd
import plotly.express as px
import streamlit as st

# Lee el archivo CSV del conjunto de datos en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Visualización de datos de anuncios de coches")


# Opción 1: Botones para construir gráficos
st.subheader("Opciones con botones")
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title="Distribución del Kilometraje")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Creación de un gráfico de dispersión para Precio vs. Kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación Precio vs Kilometraje")
    st.plotly_chart(fig, use_container_width=True)

# Opción 2: Casillas de verificación para construir gráficos
st.subheader("Opciones con casillas de verificación")
build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title="Distribución del Kilometraje")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Creación de un gráfico de dispersión para Precio vs. Kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación Precio vs Kilometraje")
    st.plotly_chart(fig, use_container_width=True)
    