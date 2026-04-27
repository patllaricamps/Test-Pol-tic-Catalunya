import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(page_title="TEST POLITIC-CAT ", layout="centered")

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
("S'han de prohibir o restringir dràsticament els pisos turístics.", "Econ", False),
("El transport públic hauria de ser gratuït o quasi gratuït.", "Econ", False),
("Cal privatitzar les empreses públiques deficitàries.", "Econ", True),
("Els sectors estratègics (energia, aigua) han de ser nacionals i públics.", "Econ", False),
("La lliure competència és la millor garantia de prosperitat.", "Econ", True),
("S'hauria d'establir un salari màxim per llei.", "Econ", False),
("Cal protegir el petit comerç local enfront de grans superfícies.", "Econ", False),
("Els grans patrimonis i les herències s'han de gravar amb impostos elevats.", "Econ", False),
("El mercat s'autoregula millor sense la intervenció de l'Estat.", "Econ", True),
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

# NACIONAL - Estrictament Catalunya vs Espanya (25)
("Catalunya ha de ser un Estat independent en forma de República.", "Nac", False),
("La unitat d'Espanya és sagrada i indivisible.", "Nac", True),
("El conflicte es podria resoldre amb un Estat federal espanyol.", "Nac", False),
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
("Cal que les forces i cossos de seguretat de l'Estat (Policia Nacional, Guàrdia Civil) marxin de Catalunya.", "Nac", False),
("La Constitució Espanyola de 1978 és intocable per a l'organització territorial.", "Nac", True),
("L'1 d'Octubre de 2017 va ser una expressió democràtica completament legítima.", "Nac", False),
("S'ha d'aplicar de nou l'article 155 de forma contundent si hi ha indicis de desobediència.", "Nac", True),
("La bandera espanyola ha d'onejar obligatòriament a tots els ajuntaments de Catalunya.", "Nac", True),
("Catalunya té dret a tenir una hisenda pròpia per recaptar absolutament tots els impostos.", "Nac", False),
("El nacionalisme català és una ideologia intrínsecament insolidària.", "Nac", True),
("Els indults i l'amnistia als líders independentistes van ser un error històric.", "Nac", True),
("El català hauria de ser l'única llengua oficial i vehicular a Catalunya.", "Nac", False),

# AUTORITAT (30)
("La policia hauria de tenir més autoritat i menys controls burocràtics.", "Auth", True),
("Mantenir l'ordre públic és més important que permetre certes protestes.", "Auth", True),
("El dret a vaga en serveis essencials hauria d'estar totalment prohibit.", "Auth", True),
("La democràcia representativa actual s'ha de substituir per assemblees populars.", "Auth", False),
("Els anomenats 'okupes' han de ser desallotjats per la força de forma immediata.", "Auth", True),
("És lícit que el govern controli o censuri internet en situacions de crisi extrema.", "Auth", True),
("Les lleis haurien de castigar durament els discursos d'odi a les xarxes socials.", "Auth", True),
("La instal·lació de càmeres de reconeixement facial als carrers aporta seguretat.", "Auth", True),
("Els delictes greus s'haurien de castigar amb la cadena perpètua.", "Auth", True),
("Idealment, l'Estat com a aparell repressor i institucional no hauria d'existir.", "Auth", False),
("S'han d'il·legalitzar els partits polítics que vulguin subvertir l'ordre constitucional.", "Auth", True),
("La llibertat d'expressió ha de ser absoluta, fins i tot per a les idees més aberrants.", "Auth", False),
("El rastreig massiu de comunicacions ciutadanes és justificable per prevenir atemptats.", "Auth", True),
("Els ciutadans haurien de tenir el dret legal a posseir armes de foc per defensar-se.", "Auth", False),
("L'obediència i el respecte a la jerarquia són virtuts fonamentals a la societat.", "Auth", True),
("Els mitjans de comunicació privats haurien d'estar fortament intervinguts per l'Estat.", "Auth", True),
("Els cossos d'antiavalots (com la BRIMO dels Mossos) haurien de ser dissolts.", "Auth", False),
("Manifestar-se tallant carreteres o infraestructures clau ha de comportar penes de presó.", "Auth", True),
("La desobediència civil pacífica i massiva contra lleis injustes és un deure moral.", "Auth", False),
("Les èpoques difícils demanen líders forts i de mà dura, no parlaments lents i dividits.", "Auth", True),
("El servei militar o cívic hauria de tornar a ser obligatori per a tota la joventut.", "Auth", True),
("L'Estat ha d'expropiar ràpidament els béns a polítics i banquers condemnats per corrupció.", "Auth", True),
("La prostitució ha de ser eradicada penalitzant severament els clients.", "Auth", True),
("S'haurien de legalitzar i regular totes les drogues per acabar amb el narcotràfic.", "Auth", False),
("Els jutges i magistrats han de tenir l'última paraula per damunt dels parlaments electes.", "Auth", True),
("El sistema penitenciari hauria de centrar-se només en la reinserció, eliminant el concepte de càstig.", "Auth", False),
("Tots els policies haurien de portar obligatòriament càmeres al pit enregistrant les seves actuacions.", "Auth", False),
("Durant una emergència nacional, l'Estat pot confinar obligatòriament la població als seus domicilis.", "Auth", True),
("Cremar banderes o fotos de caps d'Estat hauria de considerar-se un delicte de presó.", "Auth", True),
("Cal aplicar la legislació antiterrorista a grups d'activistes radicals encara que no usin violència armada.", "Auth", True),

# CULTURAL I SOCIAL (35)
("Les tradicions culturals històriques d'un territori s'han de preservar per sobre de tot.", "Cult", True),
("Els valors de base cristiana són el pilar fonamental de la nostra societat.", "Cult", True),
("El gènere és un constructe social i l'elecció d'identitat ha de ser totalment lliure.", "Cult", False),
("L’avortament hauria de ser legal, lliure i gratuït en qualsevol circumstància.", "Cult", False),
("La família tradicional (pare, mare i fills) és la cèl·lula bàsica i ideal de la societat.", "Cult", True),
("El multiculturalisme i la convivència de diverses ètnies als carrers és positiu i enriquidor.", "Cult", False),
("Cal penalitzar l'ús del vehicle privat contaminant per motius ecologistes.", "Cult", False),
("La transició energètica i les renovables han de passar per davant del creixement econòmic.", "Cult", False),
("S'ha de defensar aferrissadament la identitat cultural autòctona davant d'influències externes.", "Cult", True),
("Totes les cultures i costums del món són igualment respectables i vàlids.", "Cult", False),
("El moviment feminista actual és imprescindible per assolir la igualtat real.", "Cult", False),
("La immigració massiva posa en greu perill la seguretat i la cohesió cultural del país.", "Cult", True),
("Cal preservar festes tradicionals encara que incloguin la utilització d'animals.", "Cult", True),
("La religió i l'espiritualitat haurien de tenir presència i pes a l'espai públic i educatiu.", "Cult", True),
("La societat i totes les institucions públiques han de ser estrictament laiques.", "Cult", False),
("S'hauria de poder censurar l'art o la cultura si ofèn profundament els sentiments religiosos.", "Cult", True),
("La diversitat racial és un valor que fa avançar les societats modernes.", "Cult", False),
("Els rols de gènere clàssics (masculí i femení) obeeixen a la naturalesa biològica humana.", "Cult", True),
("La globalització posa en perill els valors tradicionals de les comunitats locals.", "Cult", True),
("Occident ha de defensar els seus valors morals tradicionals davant del relativisme.", "Cult", True),
("Les minories històricament marginades necessiten quotes a les empreses per garantir la igualtat.", "Cult", False),
("L'educació sexo-afectiva i la perspectiva de gènere ha de ser obligatòria a totes les escoles.", "Cult", False),
("La tauromàquia (curses de braus) és un art tradicional que s'ha de protegir.", "Cult", True),
("L'eutanàsia o dret a una mort digna hauria de ser legal i fàcilment accessible a qui ho demani.", "Cult", False),
("L'excés de correcció política actual és una amenaça real per a la llibertat de pensament.", "Cult", True),
("L'ús de pronoms neutres o el llenguatge inclusiu és una imposició innecessària i ridícula.", "Cult", True),
("Les parelles del mateix sexe haurien de tenir exactament els mateixos drets per adoptar menors.", "Cult", False),
("L'anomenat 'home blanc heterosexual' gaudeix de privilegis invisibles en la nostra societat.", "Cult", False),
("S'han de retirar de l'espai públic les estàtues de personatges històrics lligats al colonialisme.", "Cult", False),
("L'Estat ha de deixar de finançar les escoles concertades que segreguen per sexe o religió.", "Cult", False),
("Cal limitar dràsticament i controlar estrictament l'arribada d'immigrants estrangers.", "Cult", True),
("S'ha de donar prioritat als ciutadans autòctons a l'hora d'accedir a ajudes socials i habitatge.", "Cult", True),
("Cal obrir les portes i facilitar al màxim l'acollida de refugiats que fugen de zones en conflicte.", "Cult", False),
("La religió islàmica és culturalment incompatible amb els valors europeus de tolerància i llibertat.", "Cult", True),
("L'arribada massiva d''expats' i nòmades digitals estrangers empitjora i dilueix la identitat dels barris.", "Cult", True),
]

# ---------------------------
# UI (slider amb text)
# ---------------------------
opcions = [1, 2, 3, 4, 5]
labels = {
    1: "Molt en contra",
    2: "En contra",
    3: "Neutral",
    4: "A favor",
    5: "Molt a favor"
}

respostes = {}
for i, (text, eix, directe) in enumerate(preguntes):
    respostes[i] = st.select_slider(
        f"{i+1}. {text}",
        options=opcions,
        value=3,
        format_func=lambda x: labels[x],
        key=f"p_{i}"
    )

# ---------------------------
# RESULTATS
# ---------------------------
if st.button("VEURE RESULTAT"):

    puntuacions = {"Econ": 0, "Nac": 0, "Auth": 0, "Cult": 0}
    comptador = {"Econ": 0, "Nac": 0, "Auth": 0, "Cult": 0}

    for i, (text, eix, directe) in enumerate(preguntes):
        v = respostes[i]
        if not directe:
            v = 6 - v
        puntuacions[eix] += v
        comptador[eix] += 1

    # Normalització correcta (Permet arribar exactament a 10 i -10 adaptant-se als diferents totals de preguntes per eix)
    r = {}
    for eix in puntuacions:
        min_score = comptador[eix] * 1
        max_score = comptador[eix] * 5
        r[eix] = ((puntuacions[eix] - min_score) / (max_score - min_score)) * 20 - 10

    st.header("📊 Resultat")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Econòmic", round(r["Econ"], 1))
    col2.metric("Nacional", round(r["Nac"], 1))
    col3.metric("Autoritat", round(r["Auth"], 1))
    col4.metric("Cultural", round(r["Cult"], 1))

    # ---------------------------
    # IDEOLOGIES
    # ---------------------------
    ideologies = [
        ("Independentisme Identitari", 6, 7, -10, 9),
        ("Revolucionarisme / Comunisme Cat", -10, 6, -8, -9),
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
    ]

    st.subheader("Afinitat ideològica")

    # Guardem els resultats en una llista per poder-los ordenar
    resultats_afinitat = []
    
    for nom, e, a, n, c in ideologies:
        dist = np.sqrt(
            (r["Econ"] - e) ** 2 +
            (r["Auth"] - a) ** 2 +
            (r["Nac"] - n) ** 2 +
            (r["Cult"] - c) ** 2
        )
        p = max(0, 100 - dist * 4)
        resultats_afinitat.append((nom, p))

    # Ordenem de més semblança a menys
    resultats_afinitat.sort(key=lambda x: x[1], reverse=True)

    # Imprimim a la pantalla
    for nom, p in resultats_afinitat:
        st.write(f"**{nom}**: {round(p,1)}%")
        st.progress(p/100)

    # ---------------------------
    # GRÀFIQUES
    # ---------------------------
    fig, ax = plt.subplots(1, 2, figsize=(10,5))

    # Econ/Auth
    ax[0].set_xlim(-11, 11); ax[0].set_ylim(-11, 11)
    ax[0].axhline(0, color='black'); ax[0].axvline(0, color='black')
    ax[0].add_patch(patches.Rectangle((-11, 0), 11, 11, color='blue', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((0, 0), 11, 11, color='red', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((-11, -11), 11, 11, color='green', alpha=0.1))
    ax[0].add_patch(patches.Rectangle((0, -11), 11, 11, color='yellow', alpha=0.1))
    ax[0].scatter(r['Econ'], r['Auth'], s=200, c='black')
    ax[0].set_title("Econòmic / Autoritat")
    ax[0].set_xlabel("← Esq | Dre →")
    ax[0].set_ylabel("← Lib | Auth →")

    # Nac/Cult
    ax[1].set_xlim(-11, 11); ax[1].set_ylim(-11, 11)
    ax[1].axhline(0, color='black'); ax[1].axvline(0, color='black')
    ax[1].add_patch(patches.Rectangle((-11, -11), 11, 11, color='gold', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((0, -11), 11, 11, color='pink', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((-11, 0), 11, 11, color='purple', alpha=0.1))
    ax[1].add_patch(patches.Rectangle((0, 0), 11, 11, color='orange', alpha=0.1))
    ax[1].scatter(r['Nac'], r['Cult'], s=200, c='black')
    ax[1].set_title("Nacional / Cultural")
    ax[1].set_xlabel("← Cat | Esp →")
    ax[1].set_ylabel("← Prog | Cons →")

    plt.tight_layout()
    st.pyplot(fig)
