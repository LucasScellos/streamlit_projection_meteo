# app.py
import streamlit as st
from data_handler import load_data
from plot_handler import plot_custom_chart

def main():
    st.title("Application Streamlit avec Plotly")

    # Barre de recherche pour sélectionner la ville
    selected_city = st.selectbox("Sélectionnez une ville", ["Paris", "NewYork", "Tokyo"])

    # Charger les données en fonction de la ville sélectionnée
    data = load_data(selected_city)

    # Sélectionner les colonnes à afficher
    # selected_columns = st.multiselect(
    #     "Sélectionnez les colonnes à afficher", data.columns
    # )

    # Afficher le DataFrame avec les colonnes sélectionnées
    # st.write(data[selected_columns])

    # Tracer un graphique Plotly avec les données
    fig = plot_custom_chart(data)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
