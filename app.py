import streamlit as st
from utils.translations import translations

# Konfiguracja strony
st.set_page_config(page_title="Santo Pharmstat", layout="wide")

# Wybór języka
language = st.sidebar.selectbox(
    "Wybierz język / Select Language / Выберите язык",
    options=["Polski", "English", "Русский"],
    index=0  # Ustawienie domyślnego języka (0 = Polski, 1 = English, 2 = Русский)
)

# Ustawienie tłumaczeń na podstawie wybranego języka
t = translations[language]

# Menu boczne
st.sidebar.title(t["menu_title"])
page = st.sidebar.radio(
    t["choose_page"],
    [
        t["intro"],
        t["descriptive_stats"],
        t["histograms"],
        t["boxplot"],
        t["control_charts"],
        t["process_capability"],
        t["stability_regression"],
        t["temp_humidity"]
    ]
)

# Routing podstron
if page == t["intro"]:
    from pages import Wprowadzenie
    Wprowadzenie.show(language)

elif page == t["descriptive_stats"]:
    from pages import descriptive_statistics
    descriptive_statistics.show(language)

elif page == t["histograms"]:
    from pages import histogram_analysis
    histogram_analysis.show(language)

elif page == t["boxplot"]:
    from pages import BoxPlot
    BoxPlot.show(language)

elif page == t["control_charts"]:
    from pages import control_charts
    control_charts.show(language)

elif page == t["process_capability"]:
    from pages import process_capability
    process_capability.show(language)

elif page == t["stability_regression"]:
    from pages import stability_analysis
    stability_analysis.show(language)

elif page == t["temp_humidity"]:
    from pages import Analiza_temperatury_wilgotnosci
    Analiza_temperatury_wilgotnosci.show(language)
