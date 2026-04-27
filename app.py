import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(page_title="TEST POLÍTIC-CAT", layout="centered")

st.title("🗳️ Test Política Catalana")
st.write("120 preguntes — 4 eixos: Econòmic, Autoritari, Nacional i Cultural. Respon amb sinceritat.")
st.write("Fet per: @patllaricamps a Twitter (X).")

# ---------------------------
# PREGUNTES (120)
# ---------------------------
preguntes = [
    # ECONÒMIC (30)
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
    ("L'Estat ha d'actuar com a motor econòmic quan el sector privat falla.", "Econ", False),
    ("L'edat de jubilació s'hauria de retardar per garantir les pensions.", "Econ", True),
    ("Els fons voltor que especulen amb l'habitatge han de ser expulsats.", "Econ", False),
    ("El dret a la propietat privada és absolut i intocable.", "Econ", True),
    ("L'acomiadament dels treballadors hauria de ser lliure i gratuït.", "Econ", True),
    ("Cal reduir la jornada laboral a 32 hores setmanals sense reduir el sou.", "Econ", False),
    ("S'hauria d'abolir l'existència de paradisos fiscals a nivell internacional.", "Econ", False),
    ("La desregulació de les criptomonedes és positiva per a l'economia.", "Econ", True),
    ("La creació d'una gran banca pública és innecessària.", "Econ", True),
    ("Els sindicats posen massa traves a la competitivitat de les empreses.", "Econ", True),
    ("Els treballadors haurien de participar en la presa de decisions empresarials.", "Econ", False),

    # NACIONAL (25)
    ("Catalunya ha de ser un Estat independent en forma de República.", "Nac", False),
    ("La unitat d'Espanya és sagrada i indivisible.", "Nac", True),
    ("El conflicte es podria resoldre amb un Estat federal espanyol.", "Nac", True),
    ("L'autodeterminació és un dret legítim que Catalunya pot exercir unilateralment.", "Nac", False),
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
    ("Cal que les forces i cossos de seguretat de l'Estat marxin de Catalunya.", "Nac", False),
    ("La Constitució Espanyola de 1978 és intocable.", "Nac", True),
    ("L'1 d'Octubre de 2017 va ser una expressió democràtica legítima.", "Nac", False),
    ("S'ha d'aplicar de nou l'article 155 de forma contundent.", "Nac", True),
    ("La bandera espanyola ha d'onejar a tots els ajuntaments.", "Nac", True),
    ("Catalunya té dret a tenir una hisenda pròpia per recaptar tots els impostos.", "Nac", False),
    ("El nacionalisme català és una ideologia insolidària.", "Nac", True),
    ("Els indults i l'amnistia van ser un error històric.", "Nac", True),
    ("El català hauria de ser l'única llengua oficial i vehicular.", "Nac", False),

    # AUTORITAT (30)
    ("La policia hauria de tenir més autoritat i menys controls.", "Auth", True),
    ("Mantenir l'ordre públic és més important que certes protestes.", "Auth", True),
    ("El dret a vaga en serveis essencials hauria d'estar prohibit.", "Auth", True),
    ("La democràcia representativa s'ha de substituir per assemblees populars.", "Auth", False),
    ("Els 'okupes' han de ser desallotjats per la força de forma immediata.", "Auth", True),
    ("És lícit que el govern controli internet en crisis extremes.", "Auth", True),
    ("Les lleis haurien de castigar els discursos d'odi a les xarxes.", "Auth", True),
    ("La instal·lació de càmeres de reconeixement facial aporta seguretat.", "Auth", True),
    ("Els delictes greus s'haurien de castigar amb la cadena perpètua.", "Auth", True),
    ("Idealment, l'Estat no hauria d'existir.", "Auth", False),
    ("S'han d'il·legalitzar partits que vulguin subvertir la Constitució.", "Auth", True),
    ("La llibertat d'expressió ha de ser absoluta.", "Auth", False),
    ("El rastreig de comunicacions és justificable per prevenir atemptats.", "Auth", True),
    ("Els ciutadans haurien de poder posseir armes per defensar-se.", "Auth", False),
    ("L'obediència i el respecte a la jerarquia són fonamentals.", "Auth", True),
    ("Els mitjans privats haurien d'estar intervinguts per l'Estat.", "Auth", True),
    ("Els cossos d'antiavalots haurien de ser dissolts.", "Auth", False),
    ("Tallar carreteres en protestes ha de comportar presó.", "Auth", True),
    ("La desobediència civil pacífica és un deure moral.", "Auth", False),
    ("Les èpoques difícils demanen líders forts i de mà dura.", "Auth", True),
    ("El servei militar o cívic hauria de tornar a ser obligatori.", "Auth", True),
    ("L'Estat ha d'expropiar béns a polítics i banquers corruptes.", "Auth", True),
    ("La prostitució ha de ser eradicada penalitzant els clients.", "Auth", True),
    ("S'haurien de legalitzar totes les drogues.", "Auth", False),
    ("Els jutges han de tenir l'última paraula per damunt dels parlaments.", "Auth", True),
    ("El sistema penitenciari ha de centrar-se només en la reinserció.", "Auth", False),
    ("Tots els policies han de portar càmeres enregistrant les actuacions.", "Auth", False),
    ("L'Estat pot confinar obligatòriament la població en emergències.", "Auth", True),
    ("Cremar banderes hauria de considerar-se delicte de presó.", "Auth", True),
    ("Cal aplicar lleis antiterroristes a activistes radicals encara que no usin armes.", "Auth", True),

    # CULTURAL (35)
    ("Les tradicions històriques s'han de preservar per sobre de tot.", "Cult", True),
    ("Els valors cristians són el pilar de la nostra societat.", "Cult", True),
    ("El gènere és un constructe social i l'elecció ha de ser lliure.", "Cult", False),
    ("L’avortament ha de ser legal, lliure i gratuït.", "Cult", False),
    ("La família tradicional és la cèl·lula ideal de la societat.", "Cult", True),
    ("El multiculturalisme és positiu i enriquidor.", "Cult", False),
    ("Cal penalitzar el vehicle privat per motius ecologistes.", "Cult", False),
    ("Les renovables han de passar per davant del creixement econòmic.", "Cult", False),
    ("S'ha de defensar la identitat autòctona davant d'influències externes.", "Cult", True),
    ("Totes les cultures són igualment respectables.", "Cult", False),
    ("El moviment feminista actual és imprescindible.", "Cult", False),
    ("La immigració massiva posa en perill la seguretat del país.", "Cult", True),
    ("Cal preservar festes tradicionals amb animals.", "Cult", True),
    ("La religió hauria de tenir pes a l'espai públic.", "Cult", True),
    ("La societat ha de ser estrictament laica.", "Cult", False),
    ("S'ha de poder censurar l'art si ofèn sentiments religiosos.", "Cult", True),
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
    ("L'Estat ha de deixar de finançar escoles que segreguen per sexe.", "Cult", False),
    ("Cal limitar dràsticament l'arribada d'immigrants.", "Cult", True),
    ("Prioritat als autòctons en ajudes socials i habitatge.", "Cult", True),
    ("Cal facilitar al màxim l'acollida de refugiats.", "Cult", False),
    ("L'islam és incompatible amb els valors europeus.", "Cult", True),
    ("L'arribada d''expats' dilueix la identitat dels barris.", "Cult", True),
]

# ---------------------------
# UI (Sliders)
# ---------------------------
opcions = [1, 2, 3, 4, 5]
labels = {1: "Molt en contra", 2: "En contra", 3: "Neutral", 4: "A favor", 5: "Molt a favor"}

respostes = {}
for i, (text, eix, directe) in enumerate(preguntes):
    respostes[i] = st.select_slider(f"{i+1}. {text}", options=opcions, value=3, format_func=lambda x: labels[x], key=f"p_{i}")

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
# PROCESSAMENT
# ---------------------------
if st.button("VEURE RESULTAT"):
    puntuacions = {"Econ": 0, "Nac": 0, "Auth": 0, "Cult": 0}
    comptador = {"Econ": 0, "Nac": 0, "Auth": 0, "Cult": 0}

    for i, (text, eix, directe) in enumerate(preguntes):
        v = respostes[i]
        if not directe: v = 6 - v
        puntuacions[eix] += v
        comptador[eix] += 1

    r = {}
    for eix in puntuacions:
        min_score = comptador[eix] * 1
        max_score = comptador[eix] * 5
        r[eix] = ((puntuacions[eix] - min_score) / (max_score - min_score)) * 20 - 10

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

    # ---------------------------
    # IDEOLOGIES
    # ---------------------------
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
        ("Eco-socialisme", -8, -4, -3, -10),
        ("Liberal-progressisme", 6, -3, 2, -6),
        ("Conservadorisme moderat", 6, 5, 5, 7),
        ("Democràcia Cristiana", 3, 4, -4, 7),
        ("Comunisme Marxista-Leninista", -10, 9, -5, -6),
        ("Extrema Dreta Alternativa (Alt-Right)", 8, 8, 8, 10),
        ("Socioliberalisme", 2, -4, 0, -5),
        ("Nacionalisme de Centre-Dreta", 5, 2, -6, 5),
        ("Carlisme Tradicionalista", -2, 8, -4, 10),
        ("Falangisme", -5, 10, 10, 9),
        ("Lerrouxisme", -4, 4, 9, -8),
        ("Maoisme", -9, 9, 0, -5),
        ("Estalinisme", -10, 10, 0, 2),
        ("Neoconservadorisme", 7, 7, 0, 8),
        ("Minarquisme", 9, -8, 0, -2),
        ("Feixisme Clàssic", -2, 10, 5, 9),
        ("Populisme de Dretes", 4, 7, 6, 9),
        ("Progressisme Woke", -6, 2, 0, -10)
    ]

    st.subheader("Afinitat ideològica")
    resultats_afinitat = []
    for nom, e, a, n, c in ideologies:
        dist = np.sqrt((r["Econ"] - e)**2 + (r["Auth"] - a)**2 + (r["Nac"] - n)**2 + (r["Cult"] - c)**2)
        p = max(0, 100 - dist * 4)
        resultats_afinitat.append((nom, p))
    
    resultats_afinitat.sort(key=lambda x: x[1], reverse=True)
    for nom, p in resultats_afinitat[:10]: # Mostrem les 10 primeres
        st.write(f"**{nom}**: {round(p,1)}%")
        st.progress(p/100)

    # ---------------------------
    # GRÀFIQUES
    # ---------------------------
    fig, ax = plt.subplots(1, 2, figsize=(10,5))
    ax[0].set_xlim(-11, 11); ax[0].set_ylim(-11, 11)
    ax[0].axhline(0, color='black'); ax[0].axvline(0, color='black')
    ax[0].add_patch(patches.Rectangle((-11, 0), 11, 11, color='blue', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((0, 0), 11, 11, color='red', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((-11, -11), 11, 11, color='green', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((0, -11), 11, 11, color='yellow', alpha=0.1))
    ax[0].scatter(r['Econ'], r['Auth'], s=200, c='black', edgecolors='white')
    ax[0].set_title("Econòmic / Autoritat")
    
    ax[1].set_xlim(-11, 11); ax[1].set_ylim(-11, 11)
    ax[1].axhline(0, color='black'); ax[1].axvline(0, color='black')
    ax[1].add_patch(patches.Rectangle((-11, -11), 11, 11, color='gold', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((0, -11), 11, 11, color='pink', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((-11, 0), 11, 11, color='purple', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((0, 0), 11, 11, color='orange', alpha=0.1))
    ax[1].scatter(r['Nac'], r['Cult'], s=200, c='black', edgecolors='white')
    ax[1].set_title("Nacional / Cultural")

    st.pyplot(fig)
