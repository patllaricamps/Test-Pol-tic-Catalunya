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
("Cal reduir impostos a empreses.", "Econ", True),
("El turisme és essencial per l’economia.", "Econ", True),
("Els pisos turístics s’han de restringir.", "Econ", False),
("El transport públic ha de ser gratuït.", "Econ", False),
("Cal privatitzar empreses públiques.", "Econ", True),
("Cal nacionalitzar sectors estratègics.", "Econ", False),
("La competència de mercat és positiva.", "Econ", True),
("Cal posar un salari màxim.", "Econ", False),
("Cal protegir el comerç local.", "Econ", False),
("Cal augmentar impostos als rics.", "Econ", False),
("Cal reduir l’estat del benestar.", "Econ", True),
("La sanitat ha de ser pública.", "Econ", False),
("L’educació ha de ser privada.", "Econ", True),
("Cal regular els preus dels aliments.", "Econ", False),
("Les multinacionals aporten progrés.", "Econ", True),
("Cal fomentar cooperatives.", "Econ", False),
("El mercat laboral ha de ser flexible.", "Econ", True),
("Cal garantir renda bàsica universal.", "Econ", False),
("Cal limitar els beneficis empresarials.", "Econ", False),
("L'edat de jubilació s'hauria de retardar.", "Econ", True),
("Els bancs que van rebre ajudes públiques han de retornar-les íntegrament.", "Econ", False),
("El dret a la propietat privada és absolut i inalienable.", "Econ", True),
("La contractació temporal és necessària per a l'economia.", "Econ", True),
("L'Estat ha d'actuar com a garant d'ocupació pública si el mercat falla.", "Econ", False),
("Cal abolir els paradisos fiscals a nivell internacional.", "Econ", False),
("Les criptomonedes s'han de desregular per atraure capital.", "Econ", True),
("La banca pública és necessària per finançar projectes socials.", "Econ", False),
("Els sindicats tenen massa poder en la negociació col·lectiva.", "Econ", True),
("L'acomiadament hauria de ser lliure i gratuït.", "Econ", True),

# NACIONAL (30)
("Catalunya ha de ser independent.", "Nac", False),
("Catalunya ha de seguir dins Espanya.", "Nac", True),
("Cal més autonomia per Catalunya.", "Nac", False),
("Els Països Catalans són una nació.", "Nac", False),
("La sobirania és del poble espanyol.", "Nac", True),
("Cal protegir la llengua catalana.", "Nac", False),
("Cal un estat federal.", "Nac", False),
("La immigració s’ha de limitar.", "Nac", True),
("Europa ha de tenir més poder.", "Nac", True),
("Cal tancar fronteres en crisis migratòries.", "Nac", True),
("Catalunya ha de tenir exèrcit propi.", "Nac", False),
("Cal eliminar les autonomies.", "Nac", True),
("El català ha de ser obligatori.", "Nac", False),
("La identitat espanyola és prioritària.", "Nac", True),
("Cal cooperació amb Espanya.", "Nac", True),
("La UE limita la sobirania catalana.", "Nac", False),
("Cal acollir refugiats.", "Nac", False),
("La immigració enriqueix la societat.", "Nac", False),
("Cal prioritzar ciutadans locals.", "Nac", True),
("Catalunya ha de liderar Europa.", "Nac", False),
("L'autodeterminació és un dret inalienable dels pobles.", "Nac", False),
("Cal recuperar els símbols nacionals espanyols a les institucions de Catalunya.", "Nac", True),
("El castellà hauria de ser l'única llengua vehicular a les escoles.", "Nac", True),
("L'Estatut vigent ja ofereix suficient autogovern.", "Nac", True),
("S'han de boicotejar els productes d'empreses que van marxar el 2017.", "Nac", False),
("Catalunya té un dèficit fiscal insostenible amb l'Estat.", "Nac", False),
("La monarquia espanyola és un símbol d'unió indispensable.", "Nac", True),
("Espanya és una realitat històrica indivisible.", "Nac", True),
("Cal impulsar l'oficialitat del català a les institucions europees.", "Nac", False),
("La independència perjudicaria greument l'economia catalana.", "Nac", True),

# AUTORITAT (30)
("Cal més presència policial.", "Auth", True),
("L’ordre públic és prioritari.", "Auth", True),
("Cal limitar el dret a vaga.", "Auth", True),
("Les decisions han de ser assembleàries.", "Auth", False),
("Els okupes han de ser desallotjats ràpidament.", "Auth", True),
("El govern ha de controlar internet.", "Auth", True),
("Cal menys intervenció de l’Estat.", "Auth", False),
("Les càmeres de vigilància són positives.", "Auth", True),
("Cal una justícia més dura.", "Auth", True),
("L’Estat no hauria d’existir.", "Auth", False),
("Cal prohibir partits radicals.", "Auth", True),
("La llibertat d’expressió ha de ser total.", "Auth", False),
("Cal vigilància massiva per seguretat.", "Auth", True),
("Els ciutadans han de poder portar armes.", "Auth", False),
("Cal jerarquia forta a la societat.", "Auth", True),
("El govern ha de regular mitjans.", "Auth", True),
("Cal reduir el poder policial.", "Auth", False),
("Les protestes han de ser limitades.", "Auth", True),
("La desobediència civil és legítima.", "Auth", False),
("Cal un líder fort.", "Auth", True),
("El servei militar hauria de tornar a ser obligatori.", "Auth", True),
("Els polítics corruptes haurien de perdre el seu patrimoni personal.", "Auth", True),
("La prostitució hauria de ser abolida per llei.", "Auth", True),
("El consum de drogues s'hauria de despenalitzar totalment.", "Auth", False),
("Els tribunals han de tenir més poder que els polítics escollits.", "Auth", True),
("Cal tancar les presons i apostar per la reinserció comunitària.", "Auth", False),
("Els policies haurien de dur número visible i càmera al pit.", "Auth", False),
("En cas d'emergència nacional, el govern ha de poder suspendre drets civils.", "Auth", True),
("Cal prohibir la crema de banderes en manifestacions.", "Auth", True),
("Les lleis antiterroristes s'utilitzen abusivament contra dissidents.", "Auth", False),

# CULTURAL (30)
("La tradició catalana és important.", "Cult", True),
("El cristianisme és clau a la societat.", "Cult", True),
("El gènere és una elecció personal.", "Cult", False),
("L’avortament és un dret.", "Cult", False),
("La família tradicional és essencial.", "Cult", True),
("El multiculturalisme és positiu.", "Cult", False),
("Cal limitar el cotxe a ciutat.", "Cult", False),
("Les renovables han de ser prioritàries.", "Cult", False),
("Cal defensar la identitat cultural.", "Cult", True),
("Totes les cultures són iguals.", "Cult", False),
("El feminisme és necessari.", "Cult", False),
("La immigració amenaça la cultura.", "Cult", True),
("Cal preservar festes tradicionals.", "Cult", True),
("La religió ha de tenir pes públic.", "Cult", True),
("La societat ha de ser laica.", "Cult", False),
("Cal censurar contingut ofensiu.", "Cult", True),
("La diversitat és un valor central.", "Cult", False),
("Cal mantenir rols de gènere tradicionals.", "Cult", True),
("La globalització cultural és positiva.", "Cult", False),
("Cal protegir valors occidentals.", "Cult", True),
("Les minories ètniques necessiten quotes als llocs de decisió.", "Cult", False),
("L'educació sexual i afectiva ha de ser obligatòria a l'escola.", "Cult", False),
("Cal protegir la tauromàquia com a patrimoni cultural.", "Cult", True),
("L'eutanàsia hauria de ser accessible a tothom que la demani.", "Cult", False),
("Els vegans volen imposar la seva dieta a la resta de la societat.", "Cult", True),
("L'ús de pronoms neutres és una moda passatgera innecessària.", "Cult", True),
("Les adopcions per part de parelles del mateix sexe són igual de vàlides.", "Cult", False),
("La ciència occidental està massa esbiaixada pel masclisme.", "Cult", False),
("S'ha de retirar les estàtues de personatges històrics vinculats a l'esclavisme.", "Cult", False),
("Els missatges religiosos no han de tenir lloc en els debats parlamentaris.", "Cult", False),
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

    # Normalització correcta (Permet arribar exactament a 10 i -10)
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
        # --- NOVES IDEOLOGIES ---
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
