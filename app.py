import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Configuració
st.set_page_config(page_title="POLITIC-CAT v7.0", layout="centered")

# Estils millorats
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #e63946;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 3.5em;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🗳️ Test Política Catalana v7.0")
st.write("Analitza la teva posició en els 4 eixos clau. Versió optimitzada sense repeticions.")

# --- BASE DE DADES OPTIMITZADA ---
# Hem separat preguntes dobles i eliminat les que mesuraven el mateix
preguntes = [
    # --- EIX ECONÒMIC ---
    ("S'ha d'abolir la propietat privada dels mitjans de producció.", 'Econ', False, 1.0),
    ("La baixada d'impostos a empreses és la millor via per crear feina.", 'Econ', True, 1.0),
    ("Cal expropiar habitatges buits de grans tenidors sense indemnitzar.", 'Econ', False, 1.0),
    ("El lliure mercat és el sistema més eficient per progressar.", 'Econ', True, 1.0),
    ("L'Estat hauria de garantir una Renda Bàsica Universal a tothom.", 'Econ', False, 1.0),
    ("S'han de privatitzar empreses públiques que generin pèrdues.", 'Econ', True, 1.0),
    ("Els serveis bàsics (aigua, llum) han de ser 100% públics.", 'Econ', False, 1.0),
    ("L'SMI hauria de ser de 1.500€ o més immediatament.", 'Econ', False, 1.0),
    ("L'herència s'ha de gravar amb impostos molt alts.", 'Econ', False, 1.0),
    ("El capitalisme és un sistema inherentment injust.", 'Econ', False, 1.0),

    # --- EIX NACIONAL ---
    ("Catalunya ha de ser un Estat independent i separat d'Espanya.", 'Nac', False, 1.0),
    ("La unitat d'Espanya és indiscutible i s'ha de protegir.", 'Nac', True, 1.0),
    ("Catalunya ha de tenir el control total de les seves fronteres.", 'Nac', False, 1.0),
    ("L'autonomia actual ja ha anat massa lluny i cal recentralitzar.", 'Nac', True, 1.0),
    ("S'ha de permetre un referèndum d'autodeterminació pactat.", 'Nac', False, 1.0),
    ("L'exèrcit hauria d'intervenir si es declara la independència.", 'Nac', True, 1.0),
    ("El català ha de ser l'única llengua oficial a Catalunya.", 'Nac', False, 1.0),
    ("Em sento exclusivament espanyol.", 'Nac', True, 1.0),
    ("Els Països Catalans són la meva nació.", 'Nac', False, 1.0),
    ("Espanya és un Estat plurinacional.", 'Nac', False, 1.0),

    # --- EIX AUTORITAT ---
    ("La policia hauria de tenir més poders i menys traves legals.", 'Auth', True, 1.0),
    ("Cal abolir les presons i buscar alternatives comunitàries.", 'Auth', False, 1.0),
    ("L'ordre i la seguretat són més importants que les llibertats individuals.", 'Auth', True, 1.0),
    ("La desobediència civil és una eina legítima de protesta.", 'Auth', False, 1.0),
    ("S'hauria d'imposar la cadena perpètua per a delictes greus.", 'Auth', True, 1.0),
    ("L'Estat no ha d'intervenir en la vida privada dels ciutadans.", 'Auth', False, 1.0),
    ("Cal un control facial per càmeres a totes les ciutats.", 'Auth', True, 1.0),
    ("El dret a portar armes per defensa pròpia hauria de ser legal.", 'Auth', False, 1.0),
    ("Els 'okupes' han de ser expulsats en poques hores sense judici.", 'Auth', True, 1.0),
    ("Un govern fort és millor que un parlament dividit.", 'Auth', True, 1.0),

    # --- EIX CULTURAL ---
    ("L'avortament hauria de ser il·legal o molt restringit.", 'Cult', True, 1.0),
    ("El matrimoni homosexual és un dret que cal protegir.", 'Cult', False, 1.0),
    ("La immigració massiva posa en risc la nostra identitat.", 'Cult', True, 1.0),
    ("S'ha d'eliminar qualsevol subvenció a l'Església.", 'Cult', False, 1.0),
    ("La família tradicional (pare i mare) és la base de la societat.", 'Cult', True, 1.0),
    ("L'eutanàsia és un dret humà fonamental.", 'Cult', False, 1.0),
    ("Cal prioritzar els ajuts socials als nascuts aquí.", 'Cult', True, 1.0),
    ("La tauromàquia s'hauria de prohibir totalment.", 'Cult', False, 1.0),
    ("L'educació sexual a les escoles és necessària.", 'Cult', False, 1.0),
    ("Cal tancar centres de culte que no respectin els valors occidentals.", 'Cult', True, 1.0),
]

respostes = {}
for i, (text, eix, directe, pes) in enumerate(preguntes):
    st.markdown(f"**{i+1}. {text}**")
    respostes[i] = st.radio(f"Selecciona per a {i}", 
                            ["Molt en contra", "En contra", "Neutral", "A favor", "Molt a favor"], 
                            index=2, key=f"q_{i}", label_visibility="collapsed")
    st.divider()

if st.button("CALCULAR RESULTATS"):
    valors_map = {"Molt en contra": 1, "En contra": 2, "Neutral": 3, "A favor": 4, "Molt a favor": 5}
    puntuacions = {'Econ': 0, 'Nac': 0, 'Auth': 0, 'Cult': 0}
    max_possibles = {'Econ': 0, 'Nac': 0, 'Auth': 0, 'Cult': 0}

    for i, (text, eix, directe, pes) in enumerate(preguntes):
        v = valors_map[respostes[i]]
        final_v = v if directe else (6 - v)
        puntuacions[eix] += (final_v - 3) * pes # Escala -2 a +2
        max_possibles[eix] += 2 * pes

    # Normalització real per arribar al 10 (abs(puntuacio) / max * 10)
    r = {eix: (puntuacions[eix] / max_possibles[eix]) * 10 for eix in puntuacions}

    st.header("🔍 El teu Perfil Polític")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Afinitat amb ideologies")
        ideologies = [
            ("Aliança Catalana", 6, 7, -10, 9),
            ("Moviment Socialista / OJS", -10, 7, -8, -9),
            ("CUP / Poble Lliure", -9, -5, -10, -9),
            ("ERC", -5, -2, -9, -7),
            ("Junts", 4, 3, -9, 4),
            ("VOX", 8, 9, 10, 10),
            ("PP", 8, 4, 9, 5),
            ("PSC", -4, 2, 5, -4),
            ("Comuns", -8, -4, 4, -9),
            ("Anarcosindicalisme", -10, -10, -2, -9)
        ]
        
        results_list = []
        for nom, ie, ia, in_nac, ic in ideologies:
            # Distància sobre 20 (de -10 a 10 hi ha 20 punts)
            dist = np.sqrt((r['Econ']-ie)**2 + (r['Auth']-ia)**2 + (r['Nac']-in_nac)**2 + (r['Cult']-ic)**2)
            p = max(0, 100 - (dist / 35 * 100))
            results_list.append((nom, p))
        
        results_list.sort(key=lambda x: x[1], reverse=True)
        for nom, p in results_list:
            st.write(f"**{nom}**: {round(p,1)}%")
            st.progress(p/100)

    with col2:
        st.subheader("Mapa Visual")
        fig, ax = plt.subplots(2, 1, figsize=(6, 10))
        
        # Gràfic 1: Econ/Auth (Social)
        ax[0].set_xlim(-11, 11); ax[0].set_ylim(-11, 11)
        ax[0].axhline(0, color='black', lw=1); ax[0].axvline(0, color='black', lw=1)
        ax[0].add_patch(patches.Rectangle((-11, 0), 11, 11, color='red', alpha=0.1)) # Auth-Esq
        ax[0].add_patch(patches.Rectangle((0, 0), 11, 11, color='blue', alpha=0.1))   # Auth-Dre
        ax[0].scatter(r['Econ'], r['Auth'], s=250, c='black', edgecolor='white', zorder=10)
        ax[0].set_title("EIX SOCIAL")
        ax[0].set_xlabel("← Esquerra | Dreta →")
        ax[0].set_ylabel("← Llibertat | Autoritat →")

        # Gràfic 2: Nac/Cult (Identitat)
        ax[1].set_xlim(-11, 11); ax[1].set_ylim(-11, 11)
        ax[1].axhline(0, color='black', lw=1); ax[1].axvline(0, color='black', lw=1)
        ax[1].add_patch(patches.Rectangle((-11, -11), 11, 22, color='#FFD700', alpha=0.15)) # Zona Catalana
        ax[1].add_patch(patches.Rectangle((0, -11), 11, 22, color='#000080', alpha=0.1)) # Zona Espanyola
        ax[1].scatter(r['Nac'], r['Cult'], s=250, c='black', edgecolor='white', zorder=10)
        ax[1].set_title("EIX IDENTITARI")
        ax[1].set_xlabel("← Sobiranisme | Unionisme →")
        ax[1].set_ylabel("← Progressisme | Tradició →")
        
        plt.tight_layout()
        st.pyplot(fig)

    st.success("Test finalitzat. Comparteix el tuit que hem preparat!")
