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
        "Karta kontrolna Shewharta (X-bar / R)"
    ]
)

# Routing podstron
if page == "Wprowadzenie":
    from pages import Wprowadzenie
    Wprowadzenie.show()


elif page == "Karta kontrolna Shewharta (X-bar / R)":
    from pages import Karta_kontrolna_Shewharta
    Karta_kontrolna_Shewharta.show()
