import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="Santo Pharmstat", layout="wide")

# Menu boczne
st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Wybierz podstronę:",
    [
        "Wprowadzenie",
        "Statystyki opisowe",
        "Histogramy",
        "Wykresy pudełkowe BoxPlot",
        "Karty kontrolne ImR",
        "Analiza zdolności procesowej",
        "Regresja dla stabilności",
        "Analiza temperatury i wilgotności"
    ]
)

# Routing podstron
if page == "Wprowadzenie":
    from pages import Wprowadzenie
    Wprowadzenie.show()

elif page == "Statystyki opisowe":
    from pages import descriptive_statistics
    descriptive_statistics.show()

elif page == "Histogramy":
    from pages import histogram_analysis
    histogram_analysis.show()

elif page == "Wykresy pudełkowe BoxPlot":
    from pages import BoxPlot
    BoxPlot.show()

elif page == "Karty kontrolne ImR":
    from pages import control_charts
    control_charts.show()

elif page == "Analiza zdolności procesowej":
    from pages import process_capability
    process_capability.show()

elif page == "Regresja dla stabilności":
    from pages import stability_analysis
    stability_analysis.show()

elif page == "Analiza temperatury i wilgotności":
    from pages import Analiza_temperatury_wilgotnosci
    Analiza_temperatury_wilgotnosci.show()
