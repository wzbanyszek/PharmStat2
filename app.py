import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ---------------------------------------------------------
# Tytuł główny aplikacji
# ---------------------------------------------------------
st.title("Przykładowa wielostronicowa aplikacja w Streamlit")

# ---------------------------------------------------------
# MENU W BOCZNYM PANELU (RADIO BUTTONS)
# ---------------------------------------------------------
page = st.sidebar.radio(
    "Wybierz podstronę:",
    [
        "Wprowadzenie",
        "Wykres punktowy i liniowy",
        "Regresja liniowa (SciPy)",
        "Analiza SPC (Shewhart & Cpk)",
        "Wczytanie pliku Excel"
    ]
)

# ==================================================================
# STRONA 1: Wprowadzenie
# ==================================================================
if page == "Wprowadzenie":
    st.header("Wprowadzenie")
    st.write("""
    **Witaj w przykładowej aplikacji Streamlit!**  
    W bocznym menu możesz przełączać się między kilkoma podstronami:
    
    1. **Wprowadzenie**  
    2. **Wykres punktowy i liniowy**  
    3. **Regresja liniowa (SciPy)**  
    4. **Analiza SPC (Shewhart & Cpk)**  
    5. **Wczytanie pliku Excel**  

    ---
    **Jak korzystać z aplikacji?**  
    - Wybierz interesującą Cię podstronę z listy w bocznym panelu.
    - Interakcja odbywa się przez widżety (suwaki, przyciski, pola do wczytania pliku, itp.).
    - Wyniki (wykresy, tabele, statystyki) pojawiają się w głównym obszarze strony.
    """)
    st.info("Przejdź do kolejnych podstron za pomocą menu w bocznym panelu po lewej stronie.")

# ==================================================================
# STRONA 2: Wykres punktowy i liniowy
# ==================================================================
elif page == "Wykres punktowy i liniowy":
    st.header("Wykres punktowy i liniowy")
    
    # Suwak do wyboru liczby wierszy (punktów)
    num_rows = st.slider("Ile punktów losowych wygenerować?", 5, 300, 50)
    
    # Generowanie danych
    X = np.linspace(0, 10, num_rows)
    noise = np.random.randn(num_rows) * 3  # Szum
    Y = 2.5 * X + noise  # np. Y = 2.5 * X + szum
    
    df = pd.DataFrame({"X": X, "Y": Y})
    st.write("**Podgląd danych (pierwsze 5 wierszy):**")
    st.dataframe(df.head())
    
    # Wybór typu wykresu (scatter / line)
    chart_type = st.selectbox("Wybierz rodzaj wykresu:", ["Punktowy (scatter)", "Liniowy (line)"])
    
    # Przyciskiem rysujemy wykres
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

# ==================================================================
# STRONA 3: Regresja liniowa (SciPy)
# ==================================================================
elif page == "Regresja liniowa (SciPy)":
    st.header("Regresja Liniowa (SciPy)")
    
    st.write("""
    W tej sekcji losujemy punkty (X, Y) i dopasowujemy do nich linię 
    z wykorzystaniem `scipy.stats.linregress`. 
    """)

    # Slider do wyboru liczby punktów
    num_points = st.slider("Liczba punktów danych:", 10, 300, 50)

    # Generowanie X oraz szum
    X = np.linspace(0, 10, num_points)
    true_a = 3.0
    true_b = 2.0
    noise = np.random.randn(num_points) * 3
    Y = true_a * X + true_b + noise

    df_reg = pd.DataFrame({"X": X, "Y": Y})
    st.write("**Podgląd danych (pierwsze 5 wierszy):**")
    st.dataframe(df_reg.head())

    if st.button("Dopasuj regresję i narysuj wykres"):
        slope, intercept, r_value, p_value, std_err = linregress(X, Y)
        Y_pred = slope * X + intercept

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
        st.write(f"**Odchylenie standardowe (std_err)** = {std_err:.3f}")

# ==================================================================
# STRONA 4: Analiza SPC (Shewhart & Cpk)
# ==================================================================
elif page == "Analiza SPC (Shewhart & Cpk)":
    st.header("Analiza SPC (Shewhart & Cpk)")

    st.write("""
    Na tej stronie możesz:
    - Wygenerować losowe dane procesu (np. pomiary).  
    - Obliczyć statystyki procesu (średnia, odchylenie standardowe).  
    - Narysować **wykres Shewharta** (tzw. control chart) z linią centralną (CL) 
      oraz górną/dolną granicą kontrolną (UCL, LCL) na poziomie ±3σ.  
    - Obliczyć **Cpk** (Process Capability Index) na podstawie zadanych wartości 
      LSL (Lower Spec Limit) i USL (Upper Spec Limit).
    """)

    # Wybór liczby próbek
    n_measurements = st.slider("Ile pomiarów chcesz wygenerować?", 10, 300, 50)

    # Wybór średniej i odchylenia standardowego procesu (symulacja)
    mean_process = st.number_input("Średnia procesu (np. 50.0)", value=50.0)
    std_process = st.number_input("Odchylenie standardowe procesu (np. 2.0)", value=2.0, min_value=0.0, step=0.1)

    # Wybór wartości granic specyfikacji (LSL, USL)
    st.write("**Granice specyfikacji (LSL/USL)** – służą do wyliczenia Cpk.")
    lsl = st.number_input("LSL (Lower Spec Limit)", value=45.0)
    usl = st.number_input("USL (Upper Spec Limit)", value=55.0)

    # Przycisk: generuj dane, narysuj wykres, oblicz Cpk
    if st.button("Analizuj proces"):
        # Generowanie losowych pomiarów
        data = mean_process + std_process * np.random.randn(n_measurements)

        # Obliczamy podstawowe statystyki
        x_mean = np.mean(data)
        x_std = np.std(data, ddof=1)  # ddof=1 -> estymator z próby

        st.write(f"**Średnia z próby =** {x_mean:.3f}")
        st.write(f"**Odchylenie standardowe z próby =** {x_std:.3f}")

        # Wyznaczamy granice kontrolne (3-sigma)
        ucl = x_mean + 3 * x_std
        lcl = x_mean - 3 * x_std

        # Rysowanie wykresu Shewharta
        fig, ax = plt.subplots()
        ax.plot(data, marker='o', label='Pomiary')
        
        # Linie poziome: CL, UCL, LCL
        ax.axhline(x_mean, color='green', linestyle='--', label='CL (Center Line)')
        ax.axhline(ucl, color='red', linestyle='--', label='UCL (+3σ)')
        ax.axhline(lcl, color='red', linestyle='--', label='LCL (–3σ)')

        ax.set_title("Wykres Shewharta (X-chart)")
        ax.set_xlabel("Nr pomiaru")
        ax.set_ylabel("Wartość pomiaru")
        ax.legend()

        st.pyplot(fig)

        # Obliczanie Cpk
        if x_std > 0:
            cpk_lower = (x_mean - lsl) / (3 * x_std)
            cpk_upper = (usl - x_mean) / (3 * x_std)
            cpk_value = min(cpk_lower, cpk_upper)
        else:
            cpk_value = np.nan  # brak zmienności w danych

        st.write(f"**Cpk** = {cpk_value:.3f}")

        st.warning("""
        Interpretacja Cpk:
        - Cpk > 1.33 -> proces uznawany za zdolny,
        - 1.0 < Cpk < 1.33 -> może wymagać usprawnień,
        - Cpk < 1.0 -> proces nie spełnia wymagań.
        (Wartości mogą się różnić w zależności od standardów branżowych.)
        """)

        if lsl >= usl:
            st.error("Uwaga: LSL >= USL! Sprawdź poprawność granic specyfikacji.")

# ==================================================================
# STRONA 5: Wczytywanie pliku Excel
# ==================================================================
elif page == "Wczytanie pliku Excel":
    st.header("Wczytywanie pliku Excel")

    st.write("""
    Ta część aplikacji pozwala wgrać własny plik Excel (format `.xlsx` lub `.xls`) 
    i wyświetlić jego zawartość w postaci tabeli.  
    (Następnie możesz dodać własną logikę, np. obliczenia statystyk, wykresy itp.)
    """)

    uploaded_file = st.file_uploader(
        "Wybierz plik Excel (xlsx, xls):",
        type=["xlsx", "xls"]
    )

    if uploaded_file is not None:
        try:
            # Wczytanie danych z Excela do DataFrame
            df_excel = pd.read_excel(uploaded_file)
            st.success("Plik wczytany poprawnie. Oto podgląd danych:")
            st.dataframe(df_excel.head(20))  # pokażmy np. 20 pierwszych wierszy

            # Przykładowa sekcja: obliczenie podstawowych statystyk
            st.subheader("Podstawowe statystyki")
            st.write(df_excel.describe())
            
            # (Możesz tutaj dodać np. wykres, zależny od zawartości pliku)
        except Exception as e:
            st.error(f"Błąd odczytu pliku: {e}")
    else:
        st.info("Najpierw wybierz plik w polu powyżej.")

