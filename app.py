import streamlit as st
import os

# Configuration de la page
st.set_page_config(page_title="Portfolio | Yawo Sylvestre BOCCO", layout="wide")

# --- STYLE PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    .stExpander { border: 1px solid #e6e9ef; border-radius: 5px; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE (PROFIL & LEADERSHIP) ---
with st.sidebar:
    st.markdown("# 👤 Profil")
    st.markdown("### 👨‍💼 Leadership")
    st.write("**Directeur de l'association JCDC TOGO**")
    st.info("Formation en Cartographie & Marketing Digital") #
    
    st.markdown("---")
    st.markdown("### 🛠️ Compétences")
    st.write("✅ **SIG :** QGIS, Inkscape") #
    st.write("✅ **Data :** Python, SQL") #
    st.write("✅ **Web :** Marketing Digital") #
    
    st.markdown("---")
    st.markdown("### 🎓 Formations")
    st.write("- **Master GAED** - Université Paris Cité") #
    st.write("- **Master Aménagement** (Soutenu) - CERViDA / Lomé") #

# --- CORPS DE LA PAGE ---
st.title("🌍 Yawo Sylvestre BOCCO")
st.subheader("Géographe | Aménagiste | Cartographe | Spécialiste Marketing Digital")

st.markdown("---")

# Section Présentation
col_intro1, col_intro2 = st.columns([2, 1])
with col_intro1:
    st.header("📍 Parcours & Expertise")
    st.write("""
    Géographe environnementaliste de formation, j'allie l'analyse spatiale à l'aménagement du territoire. 
    Passionné par l'aéronautique et le développement urbain durable, je mets mes compétences en 
    **cartographie numérique** et en **marketing digital** au service de projets impactants.
    """) #
with col_intro2:
    st.header("🎓 Impact Social")
    st.write("**Directeur de JCDC TOGO**")
    st.write("Je forme les jeunes aux outils SIG et aux stratégies de communication digitale.") #

st.markdown("---")

# --- SECTION RÉALISATIONS (SANS IMAGES) ---
st.header("🚀 Travaux de Recherche & Projets SIG")

# Ligne 1 : Mémoire et Oasis
col1, col2 = st.columns(2)

with col1:
    with st.expander("✈️ MÉMOIRE : Nuisances Sonores (AIGE - Lomé)", expanded=True):
        st.write("**Aéroport International Gnassingbé Eyadéma.**")
        st.write("Étude de l'impact acoustique sur la qualité de vie des riverains.") #
        
        # Système de téléchargement robuste
        docs_folder = "docs"
        if os.path.exists(docs_folder):
            pdfs = [f for f in os.listdir(docs_folder) if f.lower().endswith(".pdf")]
            if pdfs:
                with open(os.path.join(docs_folder, pdfs[0]), "rb") as f:
                    st.download_button("📄 Télécharger le Mémoire Complet", f, file_name="BOCCO_Memoire_Aéroport_Lome.pdf")
            else:
                st.info("💡 Document en cours de mise en ligne.")
        else:
            st.warning("⚠️ Dossier 'docs' introuvable.")

with col2:
    with st.expander("🌴 ÉTUDE : Dynamique des Oasis (Maroc)", expanded=True):
        st.write("**Oasis d'Agdz & Tinzouline.**")
        st.write("Analyse de la santé de la palmeraie par télédétection (Sentinel-2 & NDVI).") #
        st.info("🗺️ Cartographie spatiale en cours d'intégration.")

# Ligne 2 : Togo et Risques
col3, col4 = st.columns(2)

with col3:
    with st.expander("🗳️ PROJET : Élections Municipales Togo", expanded=True):
        st.write("Visualisation des résultats électoraux 2025.")
        st.write("**Outils :** Python, Folium, Pandas.")
        
        # --- LA CARTE DOIT ÊTRE ICI (BIEN ALIGNÉE) ---
        import folium
        from streamlit_folium import st_folium
        
        m = folium.Map(location=[6.1319, 1.2228], zoom_start=11)
        folium.Marker([6.1319, 1.2228], popup="Lomé, Togo").add_to(m)
        
        st_folium(m, width=500, height=300)
with col4:
    with st.expander("🌊 RISQUES : Inondations à Aného", expanded=True):
        st.write("Modélisation automatisée pour l'identification des bâtiments à risque.") #
        st.write("**Outil :** QGIS Graphical Modeler.") #
        st.info("🛠️ Modèle technique en phase de finalisation.")

st.markdown("---")
st.write("📩 **Contactez-moi pour discuter d'aménagement, de cartographie ou de marketing digital !**")
st.header("🛠️ Boîte à Outils Technique")
col_skill1, col_skill2 = st.columns(2)

with col_skill1:
    st.write("**Systèmes d'Information Géographique (SIG)**")
    st.progress(95, text="QGIS & Inkscape")
    st.progress(80, text="Télédétection (Sentinel-2, NDVI)")

with col_skill2:
    st.write("**Analyse de Données & Web**")
    st.progress(75, text="Python (Pandas, Folium)")
    st.progress(85, text="Marketing Digital & SEO")
    st.markdown("---")
st.header("📱 Restons Connectés")
c1, c2, c3 = st.columns(3)
c1.link_button("🤝 Mon LinkedIn", "https://www.linkedin.com/in/sylvestre-bocco-674269317")
c2.link_button("💻 Mon GitHub (Codes)", "https://github.com/sysy1513")
c3.link_button("📢 JCDC TOGO", "https://facebook.com/jcdctogo")
st.markdown("---")
st.header("🖼️ Galerie Cartographique")
st.write("Sélection de mes travaux réalisés sous QGIS et Inkscape.")

# Ligne 1 : Colobane et Statut
col_gal1, col_gal2 = st.columns(2)

with col_gal1:
    st.subheader("📍 Localisation : Colobane")
    # Nom exact du fichier d'après ta capture
    path_colobane = "images/Carte de localisation COLOBANE.png"
    if os.path.exists(path_colobane):
        st.image(path_colobane, caption="Cartographie de localisation - Colobane")
    else:
        st.warning("Fichier 'Carte de localisation COLOBANE.png' non trouvé")

with col_gal2:
    st.subheader("📊 Carte Statut")
    # Nom exact du fichier d'après ta capture
    path_statut = "images/CARTE STATUT.png"
    if os.path.exists(path_statut):
        st.image(path_statut, caption="Analyse thématique - Statut")
    else:
        st.warning("Fichier 'CARTE STATUT.png' non trouvé")

# Ligne 2 : Densité et Pluviométrie
st.markdown("---")
col_gal3, col_gal4 = st.columns(2)

with col_gal3:
    st.subheader("👥 Densité de population")
    path_densite = "images/carte de densité.png"
    if os.path.exists(path_densite):
        st.image(path_densite, caption="Répartition spatiale de la densité")
    else:
        st.info("Fichier 'carte de densité.png' manquant")

with col_gal4:
    st.subheader("🌧️ Pluviométrie Afrique")
    path_pluvio = "images/Carte de la pluviometri moyenne en Afrique(Aout 2023).png"
    if os.path.exists(path_pluvio):
        st.image(path_pluvio, caption="Données pluviométriques moyennes - Août 2023")
    else:
        st.info("Vérifiez le nom de l'image de pluviométrie")

# Ligne 3 : Energie (Zambie et Amérique du Sud)
st.markdown("---")
col_gal5, col_gal6 = st.columns(2)

with col_gal5:
    st.subheader("⚡ Centrales de Zambie")
    path_zambie = "images/Carte des centrales electriques de la Zambie.png"
    if os.path.exists(path_zambie):
        st.image(path_zambie, caption="Cartographie des infrastructures énergétiques")

with col_gal6:
    st.subheader("🌎 Capacité Amérique du Sud")
    path_sud = "images/Cartede la capacité de production électrique en Amerique du sud.png"
    if os.path.exists(path_sud):
        st.image(path_sud, caption="Production électrique - Amérique du Sud")
        st.markdown("---")
st.header("💼 Expériences & Engagements")

with st.container(border=True):
    st.subheader("🚀 Directeur - Association JCDC TOGO")
    st.write(" *Depuis Janvier 2026*")
    st.write("- Pilotage de projets de formation en cartographie numérique.")
    st.write("- Stratégie de marketing digital pour accroître la visibilité des actions sociales.")
    st.write("- Gestion d'équipe et partenariats locaux au Togo.")

with st.container(border=True):
    st.subheader("🎓 Chercheur Master - Université Paris Cité ")
    st.write(" *Projet en cours*")
    st.write("- Étude de la dynamique des oasis au Maroc face au changement climatique.")
    st.write("- Analyse multispectrale via Sentinel-2 pour le suivi du NDVI.")