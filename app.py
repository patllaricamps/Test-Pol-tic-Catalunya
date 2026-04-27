import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Configuració de la pàgina
st.set_page_config(page_title="POLITIC-CAT", layout="centered")

# Estils personalitzats
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🗳️ Test Política Catalana")
st.write("Aquest test analitza la teva posició en 4 eixos i calcula l'afinitat amb corrents històrics i moderns. Fet per @patllaricamps a Twitter.")
st.info("Respon amb sinceritat. L'escala va de 'Molt en contra' a 'Molt a favor'.")

# --- BASE DE DADES DE PREGUNTES (75) ---
# (Text, Eix, Directe, Pes)
preguntes = [
    preguntes = [
    # ECONÒMIC
    ("Cal abolir la propietat privada dels mitjans de producció.", 'Econ', False, 1.8),
    ("L'Estat no ha de posar traves a la creació d'empreses.", 'Econ', True, 1.4),
    ("Cal expropiar pisos de grans tenidors.", 'Econ', False, 1.7),
    ("La lliure competència afavoreix el progrés.", 'Econ', True, 1.4),
    ("Cal reduir impostos per atreure inversió.", 'Econ', True, 1.5),
    ("El sistema de lliure mercat és injust.", 'Econ', False, 1.5),
    ("Cal controlar els preus dels productes bàsics.", 'Econ', False, 1.4),
    ("L'Estat ha de privatitzar empreses deficitàries.", 'Econ', True, 1.3),
    ("Cal afavorir el producte local.", 'Econ', True, 1.3),
    ("Cal un salari màxim per reduir desigualtats.", 'Econ', False, 1.5),

    # NOVES (habitatge, turisme)
    ("Cal limitar el preu del lloguer.", 'Econ', False, 1.8),
    ("Els pisos turístics s'han de restringir fortament.", 'Econ', False, 1.7),
    ("El turisme és essencial per a l'economia catalana.", 'Econ', True, 1.4),

    # NACIONAL
    ("Catalunya ha de ser independent.", 'Nac', False, 1.9),
    ("Catalunya és part d'Espanya.", 'Nac', True, 1.9),
    ("Cal control estricte de la immigració.", 'Nac', True, 1.7),
    ("Els Països Catalans són una nació.", 'Nac', False, 1.6),
    ("La sobirania resideix en el poble espanyol.", 'Nac', True, 1.8),
    ("Cal més autogovern per Catalunya.", 'Nac', False, 1.6),

    # AUTORITAT
    ("Cal més presència policial.", 'Auth', True, 1.7),
    ("Les decisions s'han de prendre en assemblees.", 'Auth', False, 1.7),
    ("L'ordre públic és prioritari.", 'Auth', True, 1.6),
    ("La justícia ha de ser més dura.", 'Auth', True, 1.6),
    ("L'Estat no hauria d'existir.", 'Auth', False, 1.8),
    ("Cal limitar el dret a vaga.", 'Auth', True, 1.5),
    ("Els okupes han de ser desallotjats ràpidament.", 'Auth', True, 1.7),

    # NOVES (seguretat / tecnologia)
    ("El govern ha de poder controlar internet per seguretat.", 'Auth', True, 1.6),
    ("Les càmeres de vigilància milloren la seguretat.", 'Auth', True, 1.5),

    # CULTURAL
    ("La tradició catalana és el pilar de la nació.", 'Cult', True, 1.8),
    ("El cristianisme és el pilar de la nació.", 'Cult', True, 1.6),
    ("El gènere és una elecció personal.", 'Cult', False, 1.8),
    ("L'avortament és un dret.", 'Cult', False, 1.8),
    ("La família tradicional és fonamental.", 'Cult', True, 1.7),
    ("El multiculturalisme és positiu.", 'Cult', False, 1.6),
    ("L'eutanàsia ha de ser legal.", 'Cult', False, 1.6),

    # NOVES (actualitat social)
    ("El transport públic ha de ser gratuït.", 'Econ', False, 1.6),
    ("Cal limitar l'ús del cotxe a les ciutats.", 'Cult', False, 1.5),
    ("Les energies renovables han de ser prioritàries.", 'Cult', False, 1.6),
]

# --- INTERFÍCIE DE PREGUNTES ---
respostes = {}
for i, (text, eix, directe, pes) in enumerate(preguntes):
    st.subheader(f"Pregunta {i+1}")
    respostes[i] = st.select_slider(
        text,
        options=[1, 2, 3, 4, 5],
        value=3,
        format_func=lambda x: {1: "Molt en contra", 2: "En contra", 3: "Neutral", 4: "A favor", 5: "Molt a favor"}[x],
        key=f"p_{i}"
    )
    st.divider()

# --- CÀLCUL I RESULTATS ---
if st.button("VEURE EL MEU PERFIL POLÍTIC"):
    puntuacions = {'Econ': 0, 'Nac': 0, 'Auth': 0, 'Cult': 0}
    pesos = {'Econ': 0, 'Nac': 0, 'Auth': 0, 'Cult': 0}

    for i, (text, eix, directe, pes) in enumerate(preguntes):
        valor = respostes[i] if directe else (6 - respostes[i])
        puntuacions[eix] += valor * pes
        pesos[eix] += pes

    # Normalització -10 a 10
    r = {eix: ((puntuacions[eix] / pesos[eix]) - 3) * 5 for eix in puntuacions}

    # Definició d'ideologies
    ideologies = [
        ("Independentisme Identitari", 6, 7, -10, 9),
        ("Revolucionarisme", -10, 6, -8, -9),
        ("Independentisme d'Esquerres", -8, -5, -10, -9),
        ("Socialdemocràcia Sobiranista", -5, -2, -9, -7),
        ("Noucentisme / Post-Convergència", 4, 3, -9, 4),
        ("Anarcosindicalisme", -10, -10, -3, -9),
        ("Nacionalisme Espanyol Radical", 8, 9, 10, 10),
        ("Federalisme d'Esquerres", -7, -3, 3, -9),
        ("Socialdemocràcia Constitucionalista", -4, 2, 6, -5),
        ("Liberalisme Radical (Anarcocapitalisme)", 10, -10, 0, -3),
        ("Carlisme Huguista", -6, -2, -9, 3),
    ]

    st.header("🔍 El teu perfil")
    
    col1, col2 = st.columns(2)
    
    # Taula d'afinitat
    with col1:
        st.subheader("Afinitat Ideològica")
        afinitats = []
        for nom, ie, ia, in_nac, ic in ideologies:
            dist = np.sqrt((r['Econ']-ie)**2 + (r['Auth']-ia)**2 + (r['Nac']-in_nac)**2 + (r['Cult']-ic)**2)
            p = max(0, 100 - (dist / 32 * 100))
            afinitats.append((nom, p))
        
        afinitats.sort(key=lambda x: x[1], reverse=True)
        for nom, p in afinitats:
            st.write(f"**{nom}**: {round(p, 1)}%")
            st.progress(p / 100)

    # Gràfics
    with col2:
        st.subheader("Mapa Polític")
        fig, ax = plt.subplots(2, 1, figsize=(6, 10))
        
        # Gràfic 1: Econ/Auth
        ax[0].set_xlim(-11, 11); ax[0].set_ylim(-11, 11)
        ax[0].axhline(0, color='black', lw=1); ax[0].axvline(0, color='black', lw=1)
        ax[0].add_patch(patches.Rectangle((-11, 0), 11, 11, color='blue', alpha=0.1))   # Esquerra-Llibertari
        ax[0].add_patch(patches.Rectangle((0, 0), 11, 11, color='red', alpha=0.1))     # Dreta-Autoritari
        ax[0].add_patch(patches.Rectangle((-11, -11), 11, 11, color='green', alpha=0.1)) # Esquerra-Autoritari
        ax[0].add_patch(patches.Rectangle((0, -11), 11, 11, color='yellow', alpha=0.1)) # Dreta-Llibertari
        ax[0].scatter(r['Econ'], r['Auth'], s=200, c='black', zorder=5)
        ax[0].set_title("Econòmic / Autoritat")
        ax[0].set_xlabel("← Esq | Dre →")
        ax[0].set_ylabel("← Lib | Auth →")

        # Gràfic 2: Nac/Cult
        ax[1].set_xlim(-11, 11); ax[1].set_ylim(-11, 11)
        ax[1].axhline(0, color='black', lw=1); ax[1].axvline(0, color='black', lw=1)
        ax[1].add_patch(patches.Rectangle((-11, -11), 11, 11, color='gold', alpha=0.1)) # Català-progressista
        ax[1].add_patch(patches.Rectangle((0, -11), 11, 11, color='pink', alpha=0.1))  # Espanyol-progressista
        ax[1].add_patch(patches.Rectangle((-11, 0), 11, 11, color='purple', alpha=0.1))   # Català-conservador
        ax[1].add_patch(patches.Rectangle((0, 0), 11, 11, color='orange', alpha=0.1))      # Espanyol-conservador
        ax[1].scatter(r['Nac'], r['Cult'], s=200, c='black', zorder=5)
        ax[1].set_title("Nacional / Cultural")
        ax[1].set_xlabel("← Cat | Esp →")
        ax[1].set_ylabel("← Prog | Cons →")
        
        plt.tight_layout()
        st.pyplot(fig)

    st.success("Test completat! Pots compartir la teva URL de Streamlit amb altres persones.")
