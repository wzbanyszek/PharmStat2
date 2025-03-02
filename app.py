import streamlit as st 
from utils.translations import translations

# Konfiguracja strony
st.set_page_config(page_title="Pharmstat2", layout="wide")

# Wybór języka
language = st.sidebar.selectbox(
    "Wybierz język / Select Language / Выберите язык",
    options=["Polski", "English", "Russian"],
    index=1  # Ustawienie domyślnego języka (0 = Polski, 1 = English, 2 = Русский)
)

# Ustawienie tłumaczeń na podstawie wybranego języka
t = translations[language]

# Menu boczne
st.sidebar.title(t["general"]["menu_title"])
page = st.sidebar.radio(
    t["general"]["choose_page"],
    [
        t["general"]["intro"],
        t["descriptive_statistics"]["descriptive_stats"],
        t["histogram_analysis"]["histograms"],
        t["boxplot_charts"]["boxplot"],
        t["control_charts"]["control_charts"],
        t["process_capability"]["process_capability"],
        t["stability_regression"]["stability_regression"],
        t["temp_humidity_analysis"]["temp_humidity"],
        t["pqr_module"]["title"],
        t["anova_module"]["title"],
        t["dissolution_testing"]["title"],
        #"Get data",
        #"Test",
        t["lab_comparison"]["title"]
    ]
)

# Routing podstron
if page == t["general"]["intro"]:
    from AppPages import Wprowadzenie
    Wprowadzenie.show(language)

elif page == t["descriptive_statistics"]["descriptive_stats"]:
    from AppPages import descriptive_statistics
    descriptive_statistics.show(language)

elif page == t["histogram_analysis"]["histograms"]:
    from AppPages import histogram_analysis
    histogram_analysis.show(language)

elif page == t["boxplot_charts"]["boxplot"]:
    from AppPages import BoxPlot
    BoxPlot.show(language)

elif page == t["control_charts"]["control_charts"]:
    from AppPages import control_charts
    control_charts.show(language)

elif page == t["process_capability"]["process_capability"]:
    from AppPages import process_capability
    process_capability.show(language)

elif page == t["stability_regression"]["stability_regression"]:
    from AppPages import stability_analysis
    stability_analysis.show(language)

elif page == t["temp_humidity_analysis"]["temp_humidity"]:
    from AppPages import Analiza_temperatury_wilgotnosci
    Analiza_temperatury_wilgotnosci.show(language)

elif page == t["pqr_module"]["title"]:  
    from AppPages import pqr
    pqr.show(language)

elif page == t["anova_module"]["title"]:
    from AppPages import anova
    anova.show(language)

elif page == t["dissolution_testing"]["title"]:
    from AppPages import dissolution_testing
    dissolution_testing.show(language)

elif page == "Get data":
    from AppPages import read_data
    read_data.show(language)

elif page == "Test":
    from AppPages import test
    test.show(language)

elif page == t["lab_comparison"]["title"]:
    from AppPages import lab_comparison
    lab_comparison.show(language)
