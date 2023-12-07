# app.py
import streamlit as st
from data_handler import load_data
from plot_handler import plot_custom_chart
import pandas as pd 

def main():
    st.title("ClimateDiag Like Test")

    # Charger les données en fonction de la ville sélectionnée
    df = pd.read_csv("data/meteo_data.csv")
   

    # Barre de recherche pour sélectionner la ville
    selected_city = st.selectbox("Sélectionnez une ville", list(df["Ville"]))

    selected_alea = st.selectbox("Sélectionnez un aléa", ["Temperature", "Jours_Sans_Pluie", "Volume_Precipitation_Max"])

    data = load_data(selected_city)


    # Sélectionner les colonnes à afficher
    # selected_columns = st.multiselect(
    #     "Sélectionnez les colonnes à afficher", data.columns
    # )

    # Afficher le DataFrame avec les colonnes sélectionnées
    # st.write(data[selected_columns])

    # Tracer un graphique Plotly avec les données
    fig = plot_custom_chart(data, selected_alea)
    st.plotly_chart(fig)

    uploaded_file = st.file_uploader("Téléchargez votre propre fichier CSV", type=["csv"])

if __name__ == "__main__":
    main()
