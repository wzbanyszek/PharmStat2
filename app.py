import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="Santo Pharmstat", layout="wide")

# Menu boczne
st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Wybierz podstronę:",
    [
        "Wprowadzenie",
        "Wykres punktowy i liniowy",
        "Regresja liniowa (SciPy)",
        "Wczytanie pliku Excel",
        "Analiza temperatury i wilgotności",
        "Karta kontrolna Shewharta (X-bar / R)",
        "Wykresy BoxPlot"  # Nowa opcja
    ]
)

# Routing podstron
if page == "Wprowadzenie":
    from pages import Wprowadzenie
    Wprowadzenie.show()

elif page == "Wykres punktowy i liniowy":
    #from pages import Wykres_punktowy_i_liniowy
    #Wykres_punktowy_i_liniowy.show()

elif page == "Regresja liniowa (SciPy)":
    #from pages import Regresja_liniowa
    #Regresja_liniowa.show()

elif page == "Wczytanie pliku Excel":
    #from pages import Wczytanie_Excel
    #Wczytanie_Excel.show()

elif page == "Analiza temperatury i wilgotności":
    #from pages import Analiza_temperatury_wilgotnosci
    #Analiza_temperatury_wilgotnosci.show()

elif page == "Karta kontrolna Shewharta (X-bar / R)":
    #from pages import Karta_kontrolna_Shewharta
    #Karta_kontrolna_Shewharta.show()

elif page == "Wykresy BoxPlot":
    #from pages import BoxPlot
    #BoxPlot.show()
