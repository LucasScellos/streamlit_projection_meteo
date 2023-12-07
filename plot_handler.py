# plot_handler.py
import plotly.graph_objects as go

def plot_custom_chart(data, var_name="Temperature"):
    # Fonction pour afficher un graphique Plotly avec les données
    fig = go.Figure()
    temp_actu = data[f"{var_name}_Actuelle"].iloc[0]
    col = [f'{var_name}_Future_Moyenne',f'{var_name}_Future_Basse', f'{var_name}_Future_Haute']
    temp_futures = data[col].values.flatten().tolist()

    # Ajout de la bulle pour la température actuelle
    fig.add_trace(go.Scatter(
        x=["Valeur de référence"],
        y=[temp_actu],
        mode='markers',
        marker=dict(
            size=50
            #size=[temp_actu],
            #sizemode='area'
        ),
        name=f'{var_name} actuelle'
    ))

    # Indices x pour les températures futures (toutes sur le même axe vertical)
    indices_x = ["Valeur Haute 2050", "Valeur Moyenne 2050", "Valeur Basse 2050"]

    # Ajout des bulles pour les températures futures
    for i, temp in enumerate(temp_futures, start=1):
        fig.add_trace(go.Scatter(
            x=[var_name],  # Utilisation des indices_x définis précédemment
            y=[temp],
            mode='markers',  # Utilisation de markers+lines pour inclure une ligne
            marker=dict(
                size=50,
                #sizemode='diameter'
            ),
            name=indices_x[i-1]
        ))

    # Ajout de titres et légendes
    fig.update_layout(
        xaxis_title=var_name,
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