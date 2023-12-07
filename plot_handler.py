# plot_handler.py
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

def plot_custom_chart(data):
    # Fonction pour afficher un graphique Plotly avec les données
    fig = go.Figure()
    temp_actu = data["Temperature_Actuelle"].iloc[0]
    col = ['Temperature_Future_Moyenne','Temperature_Future_Basse', 'Temperature_Future_Haute']
    temp_futures = data[col].values.flatten().tolist()

    # Ajout de la bulle pour la température actuelle
    fig.add_trace(go.Scatter(
        x=['Température actuelle'],
        y=[temp_actu],
        mode='markers',
        marker=dict(
            size=[temp_actu],
            sizemode='diameter'
        ),
        name='Température actuelle'
    ))

    # Indices x pour les températures futures (toutes sur le même axe vertical)
    indices_x = ['Température future basse', 'Température future moyen', 'Température future elevé']

    # Ajout des bulles pour les températures futures
    for i, temp in enumerate(temp_futures, start=1):
        fig.add_trace(go.Scatter(
            x=["Temperatures futures"],  # Utilisation des indices_x définis précédemment
            y=[temp],
            mode='markers',  # Utilisation de markers+lines pour inclure une ligne
            marker=dict(
                size=[temp],
                sizemode='diameter'
            ),
            name=f'Température future {i}'
        ))

    # Ajout de titres et légendes
    fig.update_layout(
        xaxis_title='Températures',
        yaxis_title='Valeurs',
        legend=dict(
            title='Légende',
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        )
    )

    # Affichage du diagramme
    return fig