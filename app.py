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

    st.success("Test finalitzat. Comparteix el tuit que hem preparat!")    ("El parlamentarisme és una eina de la burgesia per mantenir el capitalisme.", 'Econ', False, 1.6),
    ("S'ha de reduir la pressió fiscal per atreure inversió estrangera.", 'Econ', True, 1.5),
    ("La gestió dels recursos ha d'estar en mans de consells obrers.", 'Econ', False, 1.7),
    ("S'han d'eliminar les subvencions a entitats ideològiques i sindicats.", 'Econ', True, 1.5),
    ("El sistema de lliure mercat és inherentment injust.", 'Econ', False, 1.5),
    ("Cal un control total dels preus dels productes bàsics.", 'Econ', False, 1.4),
    ("L'Estat ha de privatitzar les empreses que generen pèrdues.", 'Econ', True, 1.3),
    ("El treball assalariat és una forma d'esclavitud moderna.", 'Econ', False, 1.6),
    ("Cal afavorir el producte nacional davant les importacions barates.", 'Econ', True, 1.3),
    ("Els impostos haurien de ser lineals i molt baixos.", 'Econ', True, 1.5),
    ("L'economia ha de servir a la nació, no als interessos globals.", 'Econ', True, 1.4),
    ("S'ha de nacionalitzar tota la banca privada.", 'Econ', False, 1.6),
    ("La meritocràcia és l'única forma justa de repartir càrrecs.", 'Econ', True, 1.2),
    ("Cal un salari màxim per limitar la riquesa obscena.", 'Econ', False, 1.5),

    # NACIONAL (19-37)
    ("Independència total: sense negociació amb l'Estat espanyol.", 'Nac', False, 1.9),
    ("Catalunya és una regió d'Espanya i punt.", 'Nac', True, 1.9),
    ("L'islamisme és incompatible amb els valors de Catalunya.", 'Nac', False, 1.8),
    ("Cal un control estricte de les fronteres catalanes.", 'Nac', False, 1.7),
    ("La nació catalana té arrels ètniques que cal protegir.", 'Nac', False, 1.7),
    ("El conflicte es resoldrà amb una República Federal Ibèrica.", 'Nac', False, 1.4),
    ("L'Estat espanyol és una presó de pobles.", 'Nac', False, 1.6),
    ("El castellà ha de ser la llengua principal de tota Espanya.", 'Nac', True, 1.7),
    ("La Generalitat ha de recuperar totes les competències en seguretat.", 'Nac', False, 1.5),
    ("L'exèrcit espanyol ha de garantir la unitat territorial.", 'Nac', True, 1.8),
    ("Catalunya ha de ser un motor d'Europa, no un llast d'Espanya.", 'Nac', False, 1.3),
    ("Els Països Catalans són la meva autèntica nació.", 'Nac', False, 1.6),
    ("S'ha de suprimir l'Art. 155 de la Constitució per sempre.", 'Nac', False, 1.5),
    ("Espanya ha de ser una monarquia centralitzada.", 'Nac', True, 1.6),
    ("Cal expulsar els immigrants que cometin delictes multireincidents.", 'Nac', True, 1.7),
    ("La sobirania nacional resideix en el poble espanyol en conjunt.", 'Nac', True, 1.8),
    ("El nacionalisme català és egoisme solidari.", 'Nac', True, 1.5),
    ("Vull la independència per fer un Estat Socialista.", 'Nac', False, 1.6),
    ("Cal recuperar la dignitat nacional catalana davant de tot.", 'Nac', False, 1.7),

    # AUTORITAT (38-56)
    ("La dictadura del proletariat és necessària per a la revolució.", 'Auth', True, 1.8),
    ("L'anarquia és l'ordre més alt; cal destruir l'Estat.", 'Auth', False, 1.9),
    ("Més autoritat policial i menys 'bonisme' judicial.", 'Auth', True, 1.7),
    ("Totes les decisions s'han de prendre per assemblea popular.", 'Auth', False, 1.7),
    ("L'ordre públic és la prioritat absoluta del govern.", 'Auth', True, 1.6),
    ("Cal una justícia més dura, incloent la cadena perpètua.", 'Auth', True, 1.6),
    ("L'Estat no ha d'existir; la societat s'ha d'organitzar voluntàriament.", 'Auth', False, 1.8),
    ("El govern ha de poder intervenir comunicacions per seguretat.", 'Auth', True, 1.5),
    ("La policia de proximitat ha de ser substituïda per un control rígid.", 'Auth', True, 1.6),
    ("Tinc dret a portar armes per defensar la meva propietat.", 'Auth', False, 1.4),
    ("La disciplina militar és positiva per a la joventut.", 'Auth', True, 1.4),
    ("L'Estat és un monstre que cal desmantellar.", 'Auth', False, 1.7),
    ("Cal prohibir els partits que atemptin contra la democràcia.", 'Auth', True, 1.5),
    ("El dret a la vaga hauria de ser molt més limitat.", 'Auth', True, 1.5),
    ("Els 'okupes' han de ser desallotjats en menys de 24 hores.", 'Auth', True, 1.7),
    ("Cal una revolució integral que canviï totes les estructures.", 'Auth', True, 1.5),
    ("L'Estat ha de ser laic i no interferir en la vida privada.", 'Auth', False, 1.4),
    ("Un líder carismàtic és millor que cent polítics indecisos.", 'Auth', True, 1.6),
    ("S'ha de respectar la jerarquia natural de les coses.", 'Auth', True, 1.4),

    # CULTURAL (57-75)
    ("La tradició catalana i el cristianisme són el pilar de la nació.", 'Cult', True, 1.8),
    ("El gènere és una opció personal i lliure.", 'Cult', False, 1.8),
    ("L'avortament és un dret fonamental i gratuït.", 'Cult', False, 1.8),
    ("Cal prioritzar els ajuts socials als 'de casa' primer.", 'Cult', True, 1.8),
    ("El feminisme actual és necessari per destruir el patriarcat.", 'Cult', False, 1.7),
    ("Occident s'està suïcidant per culpa de la immigració massiva.", 'Cult', True, 1.8),
    ("Cal eliminar la cultura de la cancel·lació.", 'Cult', True, 1.4),
    ("La llengua catalana ha de ser l'única oficial.", 'Cult', True, 1.4),
    ("S'ha de permetre el matrimoni entre qualsevol persona.", 'Cult', False, 1.6),
    ("Cal protegir les curses de braus o festes amb bous.", 'Cult', True, 1.6),
    ("El multiculturalisme és un fracàs que fragmenta la societat.", 'Cult', True, 1.7),
    ("La família tradicional és la cèl·lula bàsica de la societat.", 'Cult', True, 1.7),
    ("L'eutanàsia és un dret irrenunciable.", 'Cult', False, 1.6),
    ("Cal defensar la identitat catalana davant de tot.", 'Cult', True, 1.5),
    ("L'Estat ha d'imposar quotes de gènere.", 'Cult', False, 1.5),
    ("La religió és l'opi del poble.", 'Cult', False, 1.7),
    ("El catalanisme ha de ser essencialment progressista.", 'Cult', False, 1.4),
    ("Cal tancar mesquites que prediquin contra els nostres valors.", 'Cult', True, 1.8),
    ("Tota cultura és igual de respectable.", 'Cult', False, 1.6),
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
        ("Independentisme Identitari (Aliança Catalana)", 6, 7, -10, 9),
        ("Moviment Socialista / OJS (Revolucionari)", -10, 6, -8, -9),
        ("Independentisme d'Esquerres (CUP)", -8, -5, -10, -9),
        ("Socialdemocràcia Sobiranista (ERC)", -5, -2, -9, -7),
        ("Noucentisme / Post-Convergència (Junts)", 4, 3, -9, 4),
        ("Anarcosindicalisme (CNT)", -10, -10, -3, -9),
        ("Nacionalisme Espanyol Radical (VOX)", 8, 9, 10, 10),
        ("Federalisme d'Esquerres (Comuns)", -7, -3, 3, -9),
        ("Socialisme Constitucionalista (PSC)", -4, 2, 6, -5),
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
        ax[0].add_patch(patches.Rectangle((-11, 0), 11, 11, color='red', alpha=0.1))
        ax[0].add_patch(patches.Rectangle((0, 0), 11, 11, color='blue', alpha=0.1))
        ax[0].scatter(r['Econ'], r['Auth'], s=200, c='black', zorder=5)
        ax[0].set_title("Econòmic / Autoritat")
        ax[0].set_xlabel("← Esq | Dre →")
        ax[0].set_ylabel("← Lib | Auth →")

        # Gràfic 2: Nac/Cult
        ax[1].set_xlim(-11, 11); ax[1].set_ylim(-11, 11)
        ax[1].axhline(0, color='black', lw=1); ax[1].axvline(0, color='black', lw=1)
        ax[1].add_patch(patches.Rectangle((-11, -11), 11, 11, color='gold', alpha=0.1))
        ax[1].add_patch(patches.Rectangle((0, 0), 11, 11, color='navy', alpha=0.1))
        ax[1].scatter(r['Nac'], r['Cult'], s=200, c='black', zorder=5)
        ax[1].set_title("Nacional / Cultural")
        ax[1].set_xlabel("← Cat | Esp →")
        ax[1].set_ylabel("← Prog | Cons →")
        
        plt.tight_layout()
        st.pyplot(fig)

    st.success("Test completat! Pots compartir la teva URL de Streamlit amb altres persones.")
