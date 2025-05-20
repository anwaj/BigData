# Pour l'activer : streamlit run equipes.py

# Question 1, je vais travailler avec un excel simplifier qui contien des équipes du foot 
# les coupes gagnés et le derniere titre 


# Question 2; le fichier est nomé "equipe.py" le lancement avec "streamlit run equipes.py"
# Question 3: Chargement des libreris necessaires

import streamlit as st
import pandas as pd
import numpy as np

st.title("TP2: Créer une app StreamLit: Équipes de Football et Coupes Gagnées")
st.subheader("Realisé par WAJJARI ANAS le 20/05/2025")


# Question3: demander le nom et saluer 


nom_utilisateur = st.text_input("Entrez votre nom d'utilisateur")

if nom_utilisateur:
    st.session_state['username'] = nom_utilisateur
    st.write(f"Bonjour, {st.session_state['username']} !")

st.title("Équipes de Football et Coupes Gagnées")
st.subheader("Visualisez les titres de trois équipes de football")

# Question 5: Chargement d'un fichier CSV
uploaded_file = st.file_uploader("Téléchargez un fichier CSV avec les données des équipes et des coupes", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Données chargées depuis le fichier :")
    st.dataframe(df)

    
    # Question6: Afficher un graphique à barres avec les données chargées
    if "Équipe" in df.columns and "Coupes Gagnées" in df.columns:
        st.bar_chart(data=df.set_index("Équipe")["Coupes Gagnées"])
    else:
        st.warning("Le fichier CSV doit contenir les colonnes 'Équipe' et 'Coupes Gagnées'.")

else:
    # Afficher un graphique avec les données par défaut
    st.bar_chart(data=df_default.set_index("Équipe")["Coupes Gagnées"])


st.write("Merci d'utiliser l'application des équipes de football.")
