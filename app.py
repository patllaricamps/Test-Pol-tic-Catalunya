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

st.title("🗳️ Test Polític Català v6.0")
st.write("Aquest test analitza la teva posició en 4 eixos i calcula l'afinitat amb corrents històrics i moderns.")
st.info("Respon amb sinceritat. L'escala va de 'Molt en contra' a 'Molt a favor'.")

# --- BASE DE DADES DE PREGUNTES (75) ---
# (Text, Eix, Directe, Pes)
preguntes = [
    # ECONÒMIC (1-18)
    ("Cal abolir la propietat privada dels mitjans de producció.", 'Econ', False, 1.8),
    ("L'Estat no ha de posar traves a la creació d'empreses i riquesa.", 'Econ', True, 1.4),
    ("Cal expropiar els pisos de bancs i grans tenidors sense indemnització.", 'Econ', False, 1.7),
    ("La lliure competència és l'única forma de progrés econòmic.", 'Econ', True, 1.4),
    ("El parlamentarisme és una eina de la burgesia per mantenir el capitalisme.", 'Econ', False, 1.6),
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
