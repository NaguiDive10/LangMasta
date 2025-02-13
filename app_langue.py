import streamlit as st
import pandas as pd
from gtts import gTTS
import os
import random
from IPython.display import Audio

# Charger le vocabulaire depuis le CSV
def charger_vocabulaire(fichier_csv):
    try:
        return pd.read_csv(fichier_csv)
    except FileNotFoundError:
        st.error("Fichier introuvable. Vérifiez le chemin.")
        return pd.DataFrame(columns=["Word", "Translation"])
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier : {e}")
        return pd.DataFrame(columns=["Word", "Translation"])


# Générer un fichier audio avec gTTS
def generer_audio(texte, langue="fr"):
    tts = gTTS(text=texte, lang=langue, slow=False)
    fichier_audio = f"audio_{texte}.mp3"
    tts.save(fichier_audio)
    return fichier_audio

# Interface Streamlit
def main():
    st.title("📚 Apprentissage de Langue avec IA")
    st.markdown("### Quiz de Vocabulaire + Synthèse Vocale")

    # Charger les données
    vocabulaire = charger_vocabulaire(r"C:\Users\diven\OneDrive\Documents\DATA SCIENCE\ENGLISH 2 lang\english_vocabulary.csv")

    # Initialiser le score et l'index dans le state
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "index" not in st.session_state:
        st.session_state.index = 0
    if "reponse_utilisateur" not in st.session_state:
        st.session_state.reponse_utilisateur = ""

    # Sidebar pour les paramètres
    with st.sidebar:
        st.header("Paramètres")
        langue = st.selectbox("Langue de synthèse vocale", ["en", "fr"])

    # Afficher la question actuelle
    if st.session_state.index < len(vocabulaire):
        mot_actuel = vocabulaire.iloc[st.session_state.index]["Word"]
        traduction_correcte = vocabulaire.iloc[st.session_state.index]["Translation"]

        st.markdown(f"## Mot à traduire : **{mot_actuel}**")

        # Bouton pour écouter la prononciation
        if st.button("🎧 Écouter la prononciation"):
            fichier_audio = generer_audio(mot_actuel, langue=langue)
            st.audio(fichier_audio, format="audio/mp3")
            os.remove(fichier_audio)  # Nettoyer le fichier après lecture

        # Saisie de la réponse
        #reponse = st.text_input("Écris ta traduction ici :")
        st.session_state.reponse_utilisateur = st.text_input("Écris ta traduction ici :", st.session_state.reponse_utilisateur)



        # Vérifier la réponse
        #if reponse:
        if st.button("Valider"):
            #if reponse.strip().lower() == traduction_correcte.lower():
            if st.session_state.reponse_utilisateur.strip().lower() == traduction_correcte.lower():
                st.success("Correct ! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect. La réponse était **{traduction_correcte}**.")

            st.session_state.reponse_utilisateur = ""  # Réinitialiser le champ de texte
            st.session_state.index += 1
            st.rerun()  # Recharge la page pour la prochaine question
    else:
        st.balloons()
        st.markdown(f"## Quiz terminé ! Ton score : {st.session_state.score}/{len(vocabulaire)}")

        # Bouton pour recommencer
        if st.button("🔄 Recommencer"):
            st.session_state.score = 0
            st.session_state.index += 1
            st.session_state.reponse_utilisateur = ""
            st.rerun()

    # Afficher la progression
    st.progress(st.session_state.index / len(vocabulaire))

    # Slidebar pour le score
    st.sidebar.metric("Score actuel", f"{st.session_state.score}/{len(vocabulaire)}")


    # Bouton pour afficher la bonne réponse
    if st.button("😵‍💫 Afficher la réponse"):
        if st.session_state.index < len(vocabulaire):
            rep_corr = vocabulaire.iloc[st.session_state.index]["Translation"]
            st.markdown(f"## Réponse attendue : **{rep_corr}**")

if __name__ == "__main__":
    main()