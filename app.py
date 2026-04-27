import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(page_title="TEST POLITIC-CAT ", layout="centered")

st.title("🗳️ Test Política Catalana")
st.write("80 preguntes — 4 eixos: Econòmic, Autoritari, Nacional i Cultural. Respon amb sinceritat.")
st.write("Fet per: @patllaricamps a Twitter (X).")

# ---------------------------
# PREGUNTES (80)
# ---------------------------
preguntes = [

# ECONÒMIC
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

# NACIONAL
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

# AUTORITAT
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

# CULTURAL
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

    # Normalització correcta
    r = {}
    for eix in puntuacions:
        min_score = comptador[eix] * 1
        max_score = comptador[eix] * 5
        r[eix] = ((puntuacions[eix] - min_score) / (max_score - min_score)) * 20 - 10

    st.header("📊 Resultat")
    st.write(r)

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
    ]

    st.subheader("Afinitat ideològica")

    for nom, e, a, n, c in ideologies:
        dist = np.sqrt(
            (r["Econ"] - e) ** 2 +
            (r["Auth"] - a) ** 2 +
            (r["Nac"] - n) ** 2 +
            (r["Cult"] - c) ** 2
        )
        p = max(0, 100 - dist * 4)
        st.write(f"{nom}: {round(p,1)}%")
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
