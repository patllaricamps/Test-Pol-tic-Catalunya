import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import plotly.graph_objects as go

# ---------------------------
# CONFIGURACIÓ I ESTAT
# ---------------------------
st.set_page_config(page_title="TEST POLÍTIC-CAT", layout="centered")

if "resultats" not in st.session_state:
    st.session_state["resultats"] = None

if "resultats_afinitat" not in st.session_state:
    st.session_state["resultats_afinitat"] = None

if "mostrar_totes" not in st.session_state:
    st.session_state["mostrar_totes"] = False

st.title("🗳️ Test Política Catalana")
st.write("120 preguntes — 4 eixos: Econòmic, Autoritari, Nacional i Cultural.")
st.caption("Fet per: @patllaricamps a Twitter (X). El test és anònim.")

# ---------------------------
# DADES: PREGUNTES (120)
# ---------------------------
preguntes = [
    # ECONÒMIC
    ("Cal limitar el preu del lloguer.", "Econ", False),
    ("Cal reduir els impostos a les grans empreses.", "Econ", True),
    ("El turisme és un sector essencial i no s'ha de posar límits.", "Econ", True),
    ("S'ha de prohibir o restringir dràsticament els pisos turístics.", "Econ", False),
    ("El transport públic hauria de ser gratuït o quasi gratuït.", "Econ", False),
    ("Cal privatitzar les empreses públiques deficitàries.", "Econ", True),
    ("Els sectors estratègics (energia, aigua) han de ser nacionals i públics.", "Econ", False),
    ("La lliure competència és la millor garantia de prosperitat.", "Econ", True),
    ("S'hauria d'establir un salari màxim per llei.", "Econ", False),
    ("Cal protegir el petit comerç local enfront de grans superfícies.", "Econ", False),
    ("Els grans patrimonis i les herències s'han de gravar amb impostos elevats.", "Econ", False),
    ("El mercat s'autoregula millor sense la interventora de l'Estat.", "Econ", True),
    ("La sanitat ha de ser exclusivament de gestió i titularitat pública.", "Econ", False),
    ("L’educació privada fomenta l'excel·lència i s'ha de promoure.", "Econ", True),
    ("L'Estat ha d'intervenir per fixar els preus dels aliments bàsics en crisi.", "Econ", False),
    ("L'arribada de grans multinacionals és sempre positiva per a l'economia.", "Econ", True),
    ("L'economia cooperativa és millor que el capitalisme tradicional.", "Econ", False),
    ("Flexibilitzar el mercat laboral i l'acomiadament redueix l'atur.", "Econ", True),
    ("S'hauria d'implementar una Renda Bàsica Universal per a tothom.", "Econ", False),
    ("L'Estat ha d'actuar com a motor econòmic quant el sector privat falla.", "Econ", False),
    ("L'edat de jubilació s'hauria de retardar per garantir les pensions.", "Econ", True),
    ("Els fons voltor que especulen amb l'habitatge han de ser expulsats.", "Econ", False),
    ("El dret a la propietat privada és absolut i intocable.", "Econ", True),
    ("L'acomiadament dels treballadors hauria de ser lliure i gratuït.", "Econ", True),
    ("Cal reduir la jornada laboral sense reduir el sou.", "Econ", False),
    ("S'hauria d'abolir l'existència de paradisos fiscals a nivell internacional.", "Econ", False),
    ("La desregulació de les criptomonedes és positiva per a l'economia.", "Econ", True),
    ("La creació d'una gran banca pública és innecessària.", "Econ", True),
    ("Els sindicats posen massa traves a la competitivitat de les empreses.", "Econ", True),
    ("Els treballadors haurien de participar en la presa de decisions empresarials.", "Econ", False),

    # NACIONAL
    ("Catalunya ha de ser un Estat independent en forma de República.", "Nac", False),
    ("La unitat d'Espanya és sagrada i indivisible.", "Nac", True),
    ("El conflicte es podria resoldre amb un Estat federal espanyol.", "Nac", True),
    ("L'autodeterminació és un dret legítim que Catalunya, i qualsevol poble, pot exercir unilateralment.", "Nac", False),
    ("L'Estatut d'Autonomia actual és més que suficient.", "Nac", True),
    ("S'ha de suprimir la Generalitat i centralitzar les competències a Madrid.", "Nac", True),
    ("Els Països Catalans formen una única nació històrica i cultural.", "Nac", False),
    ("La immersió lingüística escolar en català s'ha de protegir.", "Nac", False),
    ("El castellà hauria de tenir molta més presència a les aules catalanes.", "Nac", True),
    ("La sobirania nacional resideix exclusivament en el conjunt del poble espanyol.", "Nac", True),
    ("Catalunya és una comunitat autònoma més d'Espanya, sense drets especials.", "Nac", True),
    ("L'Estat espanyol maltracta sistemàticament Catalunya a nivell econòmic i d'inversions.", "Nac", False),
    ("La monarquia espanyola garanteix l'estabilitat institucional a Catalunya.", "Nac", True),
    ("L'Estat hauria de permetre un referèndum d'independència pactat i vinculant.", "Nac", False),
    ("El procés independentista va ser un cop d'estat a la democràcia.", "Nac", True),
    ("Les seleccions esportives catalanes haurien de competir oficialment a nivell internacional.", "Nac", False),
    ("Cal que les forces i cossos de seguretat de l'Estat espanyol marxin de Catalunya.", "Nac", False),
    ("La Constitució Espanyola de 1978 és intocable.", "Nac", True),
    ("L'1 d'Octubre de 2017 va ser una expressió democràtica legítima.", "Nac", False),
    ("S'ha d'aplicar de nou l'article 155 de forma contundent.", "Nac", True),
    ("La bandera espanyola ha d'onejar a tots els ajuntaments.", "Nac", True),
    ("Catalunya té dret a tenir una hisenda pròpia per recaptar tots els impostos.", "Nac", False),
    ("El nacionalisme català és una ideologia insolidària.", "Nac", True),
    ("Els indults i l'amnistia van ser un error històric.", "Nac", True),
    ("El català hauria de ser l'única llengua oficial i vehicular.", "Nac", False),

    # AUTORITAT
    ("La policia hauria de tenir més autoritat i menys controls.", "Auth", True),
    ("Mantenir l'ordre públic és més important que certes protestes.", "Auth", True),
    ("El dret a vaga en serveis essencials hauria d'estar prohibit.", [("Auth", True), ("Econ", True)], True),
    ("La democràcia representativa s'ha de substituir per assemblees populars.", "Auth", False),
    ("Els 'okupes' han de ser desallotjats per la força de forma immediata.", [("Auth", True), ("Econ", True)], True),
    ("És lícit que el govern controli internet en crisis extremes.", "Auth", True),
    ("Les lleis haurien de castigar els discursos d'odi a les xarxes.", [("Auth", True), ("Cult", False)], True),
    ("La instal·lació de càmeres de reconeixement facial aporta seguretat.", "Auth", True),
    ("Els delictes greus s'haurien de castigar amb la cadena perpètua.", "Auth", True),
    ("Idealment, l'Estat no hauria d'existir.", "Auth", False),
    ("S'han d'il·legalitzar partits que vulguin subvertir la Constitució (de la teva nació).", "Auth", True),
    ("La llibertat d'expressió ha de ser absoluta.", "Auth", False),
    ("El rastreig de comunicacions és justificable per prevenir atemptats.", "Auth", True),
    ("L'obediència i el respecte a la jerarquia són fonamentals.", "Auth", True),
    ("Els mitjans privats haurien d'estar intervinguts per l'Estat.", [("Auth", True), ("Econ", False)], True),
    ("Els cossos d'antiavalots haurien de ser dissolts.", "Auth", False),
    ("Tallar carreteres en protestes ha de comportar presó.", "Auth", True),
    ("La desobediència civil pacífica és un deure moral.", "Auth", False),
    ("Les èpoques difícils demanen líders forts i de mà dura.", "Auth", True),
    ("El servei militar o cívic (per a la teva nació) hauria de ser obligatori.", "Auth", True),
    ("L'Estat ha d'expropiar béns a polítics i banquers corruptes.", [("Auth", True), ("Econ", False)], True),
    ("La prostitució ha de ser eradicada penalitzant els clients.", "Auth", True),
    ("S'haurien de legalitzar totes les drogues.", [("Auth", False), ("Cult", False)], True),
    ("Els jutges han de tenir l'última paraula per damunt dels parlaments.", "Auth", True),
    ("El sistema penitenciari ha de centrar-se només en la reinserció.", "Auth", False),
    ("Tots els policies han de portar càmeres enregistrant les actuacions.", "Auth", False),
    ("L'Estat pot confinar obligatòriament la població en emergències.", "Auth", True),
    ("Cremar banderes (de qualsevol nació) hauria de considerar-se delicte de presó.", "Auth", True),
    ("Cal aplicar lleis antiterroristes a activistes radicals encara que no usin armes.", "Auth", True),

    # CULTURAL
    ("Els ciutadans haurien de poder posseir armes per defensar-se.", [("Auth", True), ("Cult", False)], True),
    ("Les tradicions històriques s'han de preservar per sobre de tot.", "Cult", True),
    ("Els valors cristians són el pilar de la nostra societat.", "Cult", True),
    ("El gènere és un constructe social i l'elecció ha de ser lliure.", "Cult", False),
    ("L’avortament ha de ser legal, lliure i gratuït.", "Cult", False),
    ("La família tradicional és la cèl·lula ideal de la societat.", "Cult", True),
    ("El multiculturalisme és positiu i enriquidor.", "Cult", False),
    ("Cal penalitzar el vehicle privat per motius ecologistes.", [("Auth", True), ("Cult", False), ("Econ", False)], True),
    ("Les renovables han de passar per davant del creixement econòmic.", [("Cult", False), ("Econ", False)], True),
    ("S'ha de defensar la identitat autòctona davant d'influències externes.", "Cult", True),
    ("Totes les cultures són igualment respectables.", "Cult", False),
    ("El moviment feminista actual és imprescindible.", "Cult", False),
    ("La immigració massiva posa en perill la seguretat del país.", [("Auth", True), ("Cult", True)], True),
    ("Cal preservar festes tradicionals amb animals.", "Cult", True),
    ("La religió hauria de tenir pes a l'espai públic.", "Cult", True),
    ("La societat ha de ser estrictament laica.", "Cult", False),
    ("S'ha de poder censurar l'art si ofèn sentiments religiosos.", [("Auth", True), ("Cult", True)], True),
    ("La diversitat racial fa avançar la societat.", "Cult", False),
    ("Els rols de gènere clàssics obeeixen a la naturalesa biològica.", "Cult", True),
    ("La globalització posa en perill els valors locals.", "Cult", True),
    ("Occident ha de defensar els seus valors morals.", "Cult", True),
    ("Les minories necessiten quotes per garantir la igualtat.", "Cult", False),
    ("L'educació sexo-afectiva ha de ser obligatòria.", "Cult", False),
    ("La tauromàquia s'ha de protegir.", "Cult", True),
    ("L'eutanàsia hauria de ser legal i fàcilment accessible.", "Cult", False),
    ("L'excés de correcció política amenaça la llibertat.", "Cult", True),
    ("L'ús del llenguatge inclusiu és una imposició ridícula.", "Cult", True),
    ("Parelles del mateix sexe han de poder adoptar.", "Cult", False),
    ("L'home blanc heterosexual gaudeix de privilegis invisibles.", "Cult", False),
    ("S'han de retirar estàtues lligades al colonialisme.", "Cult", False),
    ("L'Estat ha de deixar de finançar escoles que segreguen per sexe.", [("Cult", False), ("Econ", False)], True),
    ("Cal limitar dràsticament l'arribada d'immigrants.", [("Auth", True), ("Cult", True)], True),
    ("Prioritat als autòctons en ajudes socials i habitatge.", [("Cult", True), ("Econ", False)], True),
    ("Cal facilitar al màxim l'acollida de refugiats.", "Cult", False),
    ("L'islam és incompatible amb els valors europeus.", "Cult", True),
    ("L'arribada d''expats' dilueix la identitat dels barris.", "Cult", True),
]

# ---------------------------
# LOGICA DE TEXTOS DE RESULTAT
# ---------------------------
def label_econ(v):
    if v < -7: return "Esquerra Radical"
    if v < -2: return "Esquerra"
    if v < 2:  return "Centre"
    if v < 7:  return "Dreta"
    return "Dreta Radical"

def label_nac(v):
    if v < -7: return "Nacionalisme Català"
    if v < -3: return "Sobiranisme Català"
    if v < 2:  return "Federalisme / Autonomisme"
    if v < 7:  return "Constitucionalisme Espanyol"
    return "Nacionalisme Espanyol"

def label_auth(v):
    if v < -7: return "Llibertari / Anarquisme"
    if v < -3: return "Anti-autoritari"
    if v < 2:  return "Socioliberalisme"
    if v < 7:  return "Ordre i Autoritat"
    return "Autoritarisme"

def label_cult(v):
    if v < -6: return "Progressisme Radical (Woke)"
    if v < -2: return "Progressisme"
    if v < 2:  return "Moderat / Centrista"
    if v < 6:  return "Conservadorisme"
    return "Tradicionalisme / Reaccionarisme"

# ---------------------------
# UI (Sliders) - Dins d'un Form
# ---------------------------
opcions = [1, 2, 3, 4, 5]
labels_slider = {1: "Molt en contra", 2: "En contra", 3: "Neutral", 4: "A favor", 5: "Molt a favor"}

with st.form(key="formulari_test"):
    respostes = {}
    for i, item in enumerate(preguntes):
        respostes[i] = st.select_slider(
            f"{i+1}. {item[0]}", 
            options=opcions, 
            value=3, 
            format_func=lambda x: labels_slider[x], 
            key=f"p_{i}"
        )
    
    submitted = st.form_submit_button("VEURE RESULTAT")

# ---------------------------
# PROCESSAMENT
# ---------------------------
if submitted:
    puntuacions = {"Econ": 0, "Nac": 0, "Auth": 0, "Cult": 0}
    comptador = {"Econ": 0, "Nac": 0, "Auth": 0, "Cult": 0}

    for i, item in enumerate(preguntes):
        v = respostes[i]
        # Adaptació eixos (si és str o llista de tuples)
        eixos_afectats = [(item[1], item[2])] if isinstance(item[1], str) else item[1]

        for eix, directe in eixos_afectats:
            valor_final = v if directe else (6 - v)
            puntuacions[eix] += valor_final
            comptador[eix] += 1

    r = {}
    for eix in puntuacions:
        min_score = comptador[eix] * 1
        max_score = comptador[eix] * 5
        r[eix] = ((puntuacions[eix] - min_score) / (max_score - min_score)) * 20 - 10

    # DADES IDEOLOGIES (40)
    ideologies = [
        ("Independentisme Identitari", 6, 7, -10, 9, "Independentisme unilateral d'ordre que prioritza la supervivència cultural."),
        ("Independentisme d'Esquerres", -8, -5, -10, -9, "Ruptura unilateral per construir una República Catalana post-capitalista."),
        ("Sobiranisme Progressista", -6, -2, -8, -7, "Dret a l'autodeterminació i sobiranisme social."),
        ("Socialdemocràcia Catalanista", -4, 1, -5, -3, "Defensa de l'autogovern i l'estat del benestar."),
        ("Noucentisme / Post-Convergència", 4, 3, -9, 4, "Liberalisme nacional català pragmàtic."),
        ("Estat Català / Dencasisme", -6, 9, -10, 7, "Nacionalisme català d'acció directa i ordre."),
        ("Carlisme Huguista", -6, -2, -9, 3, "Socialisme autogestionari d'arrel tradicional catalana."),
        ("Nacionalisme de Centre-Dreta", 5, 2, -6, 5, "Catalanisme clàssic de progrés econòmic privat."),
        ("Nacionalisme Espanyol Radical", 8, 9, 10, 10, "Unitarisme espanyol intransigent i conservador."),
        ("Federalisme d'Esquerres", -7, -3, 3, -9, "Transformació republicana d'Espanya plurinacional."),
        ("Socialdemocràcia Constitucionalista", -4, 2, 6, -5, "Reformisme de centre-esquerra basat en la Constitució."),
        ("Aznarisme / Dreta Unificada", 7, 6, 8, 8, "Liberal-conservadorisme centralista."),
        ("Falangisme (Nacional-Sindicalisme)", -5, 10, 10, 9, "Feixisme espanyol clàssic i sindicat vertical."),
        ("Nacional-Sindicalisme (Ledesma Ramos)", -8, 10, 10, 8, "Puresa feixista revolucionària."),
        ("Lerrouxisme", -3, 4, 9, -8, "Populisme espanyolista de base obrera anticlerical."),
        ("Regionalisme No-Nacionalista", 2, 2, 4, 3, "Defensa del que és local dins la unitat d'Espanya."),
        ("Revolucionarisme", -10, 6, -2, -9, "Destrucció de l'estat burgès i acció directa."),
        ("Anarcosindicalisme", -10, -10, -3, -9, "Gestió col·lectiva sense estats ni jerarquies."),
        ("Comunisme Marxista-Leninista", -10, 9, -5, -6, "Economia planificada i avantguarda política."),
        ("Estalinisme", -10, 10, 0, 2, "Model soviètic de control total i industrialització."),
        ("Trotskisme", -10, 4, 0, -10, "Revolució permanent i crítica a la burocràcia."),
        ("Maoisme", -9, 9, 0, -5, "Guerra popular i revolució cultural constant."),
        ("Eco-socialisme", -8, -4, -3, -10, "Síntesi de marxisme i ecologia."),
        ("Mutualisme", -7, -8, 0, -7, "Anarquisme de mercat i cooperatives."),
        ("Anarquisme Individualista", 0, -10, 0, -8, "Sobirania absoluta de l'individu."),
        ("Socialisme de Caviar (Gauche Divine)", -4, -4, 0, -8, "Progressisme de classe alta hedonista."),
        ("Liberalisme Radical (Anarcocapitalisme)", 10, -10, 0, -3, "Lliure mercat absolut sense Estat."),
        ("Minarquisme", 9, -8, 0, -2, "Estat mínim només per a seguretat i propietat."),
        ("Liberal-progressisme", 6, -3, 2, -6, "Capitalisme global i llibertats civils."),
        ("Socioliberalisme", 2, -4, 0, -5, "Mercat lliure amb correccions socials."),
        ("Conservadorisme moderat", 6, 5, 5, 7, "Pragmatisme i preservació institucional."),
        ("Democràcia Cristiana", 3, 4, -4, 7, "Economia social inspirada en l'Església."),
        ("Neoconservadorisme (Bush)", 7, 7, 0, 8, "Intervencionisme militar i moral tradicional."),
        ("Tecnocràcia", 2, 6, 0, -4, "Gestió basada en l'eficiència i els experts."),
        ("Carlisme Tradicionalista", -2, 8, -3, 10, "Déu, Pàtria, Furs i Rei."),
        ("Nacional-Bolxevisme (Nazbol)", -9, 10, 0, 10, "Extrema esquerra econòmica i ultranacionalisme."),
        ("Extrema Dreta Alternativa (Alt-Right)", 8, 8, 8, 10, "Reacció identitària digital contra el multiculturalisme."),
        ("Feixisme Clàssic (Mussolini)", -2, 10, 5, 9, "Tot dins l'Estat, res fora de l'Estat."),
        ("Nacionalsocialisme (Nazi)", 2, 10, 10, 10, "Totalitarisme racial i subordinació de l'economia."),
        ("Ecofeixisme", -2, 9, 0, 8, "Autoritarisme verd per preservar l'ecosistema nacional."),
        ("Distributisme", -3, 3, 0, 8, "Propietat repartida i doctrina social catòlica."),
        ("Populisme de Dretes", 4, 7, 6, 9, "Defensa del poble contra les elits cosmopolites."),
        ("Progressisme Woke", -6, 2, 0, -10, "Justícia social centrada en la deconstrucció de privilegis."),
        ("Centrisme Liberal / Moderat", 2, -2, 0, 0, "Pragmatisme i estabilitat política."),
        ("Anarcoprimitivisme", -10, -10, 0, -5, "Rebuig a la civilització industrial."),
        ("Dreta Il·liberal Identitària", 4, 8, -10, 10, "Nacionalisme català d'ordre identitari."),
        ("Socialisme d'Alliberament Nacional", -9, -3, -10, -3, "Alliberament nacional i social mitjançant la ruptura independentista."),
    ]

    # Guardem les ideologies a la sessió per a la visualització posterior
    st.session_state["ideologies"] = ideologies

    res_afinitat = []
    for nom, e, a, n, c, desc in ideologies:
        dist = np.sqrt((r["Econ"] - e)**2 + (r["Auth"] - a)**2 + (r["Nac"] - n)**2 + (r["Cult"] - c)**2)
        p = max(0, 100 * (1 - dist / 40))
        res_afinitat.append((nom, p, desc))
    
    res_afinitat.sort(key=lambda x: x[1], reverse=True)
    
    st.session_state["resultats"] = r
    st.session_state["resultats_afinitat"] = res_afinitat

# ---------------------------
# DISPLAY DE RESULTATS
# ---------------------------
if st.session_state["resultats"]:
    r = st.session_state["resultats"]
    afinitat = st.session_state["resultats_afinitat"]

    st.header("📊 Resultat")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Econòmic", round(r["Econ"], 1))
        st.info(f"**{label_econ(r['Econ'])}**")
    with col2:
        st.metric("Nacional", round(r["Nac"], 1))
        st.info(f"**{label_nac(r['Nac'])}**")
    with col3:
        st.metric("Autoritat", round(r["Auth"], 1))
        st.info(f"**{label_auth(r['Auth'])}**")
    with col4:
        st.metric("Cultural", round(r["Cult"], 1))
        st.info(f"**{label_cult(r['Cult'])}**")

    # -------------------------------------------------------
    # GRÀFIQUES inicials (matplotlib) AMB EL NOU ESTIL
    # -------------------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(10,5))

    # Econ / Auth
    ax[0].set_xlim(-11, 11)
    ax[0].set_ylim(-11, 11)
    ax[0].axhline(0, color='black')
    ax[0].axvline(0, color='black')
    # Esquerra autoritària (vermell), Dreta autoritària (blau)
    ax[0].add_patch(patches.Rectangle((-11, 0), 11, 11, color='red', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((0, 0), 11, 11, color='blue', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((-11, -11), 11, 11, color='green', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((0, -11), 11, 11, color='yellow', alpha=0.1))
    ax[0].scatter(r['Econ'], r['Auth'], s=200, c='black', zorder=5)
    ax[0].set_title("Econòmic / Autoritat")
    ax[0].set_xlabel("← Esq | Dre →")
    ax[0].set_ylabel("← Lib | Auth →")

    # Nac / Cult
    ax[1].set_xlim(-11, 11)
    ax[1].set_ylim(-11, 11)
    ax[1].axhline(0, color='black')
    ax[1].axvline(0, color='black')
    ax[1].add_patch(patches.Rectangle((-11, -11), 11, 11, color='gold', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((0, -11), 11, 11, color='pink', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((-11, 0), 11, 11, color='purple', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((0, 0), 11, 11, color='orange', alpha=0.1))
    ax[1].scatter(r['Nac'], r['Cult'], s=200, c='black', zorder=5)
    ax[1].set_title("Nacional / Cultural")
    ax[1].set_xlabel("← Cat | Esp →")
    ax[1].set_ylabel("← Prog | Cons →")

    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Afinitat ideològica (Top 10)")
    for nom, p, desc in afinitat[:10]:
        st.write(f"**{nom}**: {round(p,1)}%")
        st.progress(p/100)
        st.markdown("---")

    if st.button("🔍 Veure totes les ideologies"):
        st.session_state["mostrar_totes"] = True

    if st.session_state["mostrar_totes"]:
        st.subheader("Mapa complet d'ideologies")
        for nom, p, desc in afinitat:
            with st.expander(f"{nom} — {round(p,1)}%"):
                st.write(desc)
                st.progress(p/100)

        # ---------------------------------------------------
        # NOUS GRÀFICS INTERACTIUS AMB TOTES LES IDEOLOGIES (quadrats adaptables)
        # ---------------------------------------------------
        st.subheader("📍 Posicionament al mapa ideològic complet")
        ideologies = st.session_state.get("ideologies", [])

        # Dades per al gràfic Econ vs Auth
        x1 = [ideology[1] for ideology in ideologies]
        y1 = [ideology[2] for ideology in ideologies]
        noms1 = [ideology[0] for ideology in ideologies]

        # Dades per al gràfic Nac vs Cult
        x2 = [ideology[3] for ideology in ideologies]
        y2 = [ideology[4] for ideology in ideologies]
        noms2 = noms1  # mateixos noms

        # Creació del gràfic 1 (Econ vs Auth)
        fig_plotly1 = go.Figure()
        fig_plotly1.add_trace(go.Scatter(
            x=x1, y=y1,
            mode='markers',
            marker=dict(color='gray', size=8, opacity=0.6),
            text=noms1,
            hoverinfo='text',
            name='Ideologies'
        ))
        fig_plotly1.add_trace(go.Scatter(
            x=[r['Econ']], y=[r['Auth']],
            mode='markers',
            marker=dict(color='red', size=15, line=dict(color='black', width=2)),
            text=['Tu'],
            hoverinfo='text',
            name='La teva posició'
        ))
        fig_plotly1.update_layout(
            title="Econòmic / Autoritat",
            xaxis=dict(title="← Esq | Dre →", range=[-11, 11], zeroline=True, zerolinecolor='black'),
            yaxis=dict(title="← Lib | Auth →", range=[-11, 11], zeroline=True, zerolinecolor='black',
                       scaleanchor="x", scaleratio=1),
            showlegend=True,
        )
        # Fons de colors
        fig_plotly1.add_shape(type="rect", x0=-11, x1=0, y0=0, y1=11, fillcolor="red", opacity=0.1, line=dict(width=0))
        fig_plotly1.add_shape(type="rect", x0=0, x1=11, y0=0, y1=11, fillcolor="blue", opacity=0.1, line=dict(width=0))
        fig_plotly1.add_shape(type="rect", x0=-11, x1=0, y0=-11, y1=0, fillcolor="green", opacity=0.1, line=dict(width=0))
        fig_plotly1.add_shape(type="rect", x0=0, x1=11, y0=-11, y1=0, fillcolor="yellow", opacity=0.1, line=dict(width=0))

        # Creació del gràfic 2 (Nac vs Cult)
        fig_plotly2 = go.Figure()
        fig_plotly2.add_trace(go.Scatter(
            x=x2, y=y2,
            mode='markers',
            marker=dict(color='gray', size=8, opacity=0.6),
            text=noms2,
            hoverinfo='text',
            name='Ideologies'
        ))
        fig_plotly2.add_trace(go.Scatter(
            x=[r['Nac']], y=[r['Cult']],
            mode='markers',
            marker=dict(color='red', size=15, line=dict(color='black', width=2)),
            text=['Tu'],
            hoverinfo='text',
            name='La teva posició'
        ))
        fig_plotly2.update_layout(
            title="Nacional / Cultural",
            xaxis=dict(title="← Cat | Esp →", range=[-11, 11], zeroline=True, zerolinecolor='black'),
            yaxis=dict(title="← Prog | Cons →", range=[-11, 11], zeroline=True, zerolinecolor='black',
                       scaleanchor="x", scaleratio=1),
            showlegend=True,
        )
        fig_plotly2.add_shape(type="rect", x0=-11, x1=0, y0=-11, y1=0, fillcolor="gold", opacity=0.1, line=dict(width=0))
        fig_plotly2.add_shape(type="rect", x0=0, x1=11, y0=-11, y1=0, fillcolor="pink", opacity=0.1, line=dict(width=0))
        fig_plotly2.add_shape(type="rect", x0=-11, x1=0, y0=0, y1=11, fillcolor="purple", opacity=0.1, line=dict(width=0))
        fig_plotly2.add_shape(type="rect", x0=0, x1=11, y0=0, y1=11, fillcolor="orange", opacity=0.1, line=dict(width=0))

        col_plot1, col_plot2 = st.columns(2)
        with col_plot1:
            st.plotly_chart(fig_plotly1, width='stretch')
        with col_plot2:
            st.plotly_chart(fig_plotly2, width='stretch')
