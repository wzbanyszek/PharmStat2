import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Tytuł główny aplikacji
st.title("Wielostronicowa aplikacja w Streamlit z menu bocznym")

# Tworzymy menu w panelu bocznym (sidebar)
page = st.sidebar.selectbox(
    "Wybierz podstronę",
    ["Wprowadzenie", "Wykres punktowy i liniowy", "Regresja liniowa (SciPy)"]
)

# -----------------------------------------------------------------------------
# STRONA 1: Wprowadzenie
# -----------------------------------------------------------------------------
if page == "Wprowadzenie":
    st.header("Wprowadzenie")
    st.write("""
    **Witaj w przykładowej aplikacji Streamlit!**  
    W bocznym menu możesz przełączać się między trzema podstronami:
    1. Wprowadzenie – widzisz ją właśnie teraz.
    2. Wykres punktowy i liniowy – demonstracja losowych danych i wykresów matplotlib.
    3. Regresja liniowa (SciPy) – dopasowanie prostej przy użyciu `scipy.stats.linregress`.

    ---
    **Jak korzystać z aplikacji?**  
    - Wybierz interesującą Cię podstronę z listy w bocznym panelu.  
    - Interakcje z aplikacją (np. generowanie danych, wybór opcji) odbywają się poprzez widżety (suwaki, przyciski itp.).
    - Wyniki, takie jak wykresy i tabele, wyświetlane są w głównym obszarze strony.
    """)
    st.info("Przejdź do kolejnych podstron za pomocą menu w bocznym panelu po lewej stronie.")

# -----------------------------------------------------------------------------
# STRONA 2: Wykres punktowy i liniowy
# -----------------------------------------------------------------------------
elif page == "Wykres punktowy i liniowy":
    st.header("Wykres punktowy i liniowy")
    
    # Wybór liczby wierszy (punktów) przez suwak
    num_rows = st.slider("Ile punktów losowych wygenerować?", 5, 300, 50)
    
    # Generowanie danych: X od 0 do 10 w równych odstępach
    X = np.linspace(0, 10, num_rows)
    noise = np.random.randn(num_rows) * 3  # szum losowy
    # Załóżmy jakiś wzór na Y, np. Y = 2.5 * X + szum
    Y = 2.5 * X + noise
    
    # Tworzymy DataFrame do wglądu
    df = pd.DataFrame({"X": X, "Y": Y})
    st.write("Podgląd danych (pierwsze 5 wierszy):")
    st.dataframe(df.head())
    
    # Selectbox do wyboru typu wykresu (scatter / line)
    chart_type = st.selectbox("Wybierz rodzaj wykresu:", ["Punktowy (scatter)", "Liniowy (line)"])
    
    # Po kliknięciu przycisku rysujemy wykres
    if st.button("Rysuj wykres"):
        fig, ax = plt.subplots()
        
        if chart_type == "Punktowy (scatter)":
            ax.scatter(df["X"], df["Y"], color="blue", alpha=0.7)
            ax.set_title("Wykres punktowy")
        else:
            ax.plot(df["X"], df["Y"], color="red")
            ax.set_title("Wykres liniowy")
        
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        
        st.pyplot(fig)

# -----------------------------------------------------------------------------
# STRONA 3: Regresja liniowa (SciPy)
# -----------------------------------------------------------------------------
elif page == "Regresja liniowa (SciPy)":
    st.header("Regresja Liniowa (SciPy)")
    
    st.write("""
    W tej sekcji losujemy punkty (X, Y) i dopasowujemy do nich linię 
    z wykorzystaniem `scipy.stats.linregress`. 
    """)

    # Slider do wyboru liczby punktów
    num_points = st.slider("Liczba punktów danych:", 10, 300, 50)

    # Generujemy X oraz losowy szum
    X = np.linspace(0, 10, num_points)
    true_a = 3.0
    true_b = 2.0
    noise = np.random.randn(num_points) * 3

    # Wzór: Y = aX + b + szum
    Y = true_a * X + true_b + noise

    df_reg = pd.DataFrame({"X": X, "Y": Y})
    st.write("Podgląd danych (pierwsze 5 wierszy):")
    st.dataframe(df_reg.head())

    # Przycisk: dopasuj regresję i wyświetl wykres
    if st.button("Dopasuj regresję i narysuj wykres"):
        slope, intercept, r_value, p_value, std_err = linregress(X, Y)

        # Przewidywane wartości na podstawie linii regresji
        Y_pred = slope * X + intercept

        # Rysowanie
        fig, ax = plt.subplots()
        ax.scatter(X, Y, label="Dane (punkty)", alpha=0.7)
        ax.plot(X, Y_pred, color="red", label="Linia regresji")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        ax.set_title("Regresja Liniowa: Y = aX + b")

        st.pyplot(fig)

        st.write(f"**Nachylenie (slope)** = {slope:.3f}")
        st.write(f"**Wyraz wolny (intercept)** = {intercept:.3f}")
        st.write(f"**Współczynnik korelacji (r)** = {r_value:.3f}")
        st.write(f"**Wartość p (p-value)** = {p_value:.3e}")
        st.write(f"**Odchylenie standardowe oszacowania (std_err)** = {std_err:.3f}")

        st.info("Za każdym razem dane są generowane z nowym szumem, więc wyniki będą się różnić.")

