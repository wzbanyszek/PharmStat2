import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

st.title("Regresja Liniowa z wykorzystaniem SciPy")

"""
W tej aplikacji generujemy losowe punkty (X, Y) i dopasowujemy do nich linię 
korzystając z `scipy.stats.linregress`, która zwraca m.in. nachylenie, wyraz wolny 
oraz statystyki dotyczące dopasowania.
"""

# Użytkownik wybiera liczbę punktów
num_points = st.slider("Wybierz liczbę punktów danych:", 10, 300, 50)

# Generujemy dane X w równych odstępach, np. w przedziale [0,10]
X = np.linspace(0, 10, num_points)

# Prawdziwe parametry (do testów)
true_a = 3.0
true_b = 2.0

# Szum o rozkładzie normalnym
noise = np.random.randn(num_points) * 3

# Generowanie wartości Y według równania y = a*x + b + szum
Y = true_a * X + true_b + noise

# Tworzymy DataFrame z danymi (opcjonalnie)
df = pd.DataFrame({"X": X, "Y": Y})

st.write("**Podgląd wygenerowanych danych** (pierwsze 5 wierszy):")
st.dataframe(df.head())

# Przycisk, który dopasuje regresję i narysuje wyniki
if st.button("Dopasuj regresję i pokaż wykres"):
    # Dopasowanie liniowe przy pomocy scipy.stats.linregress
    slope, intercept, r_value, p_value, std_err = linregress(X, Y)
    
    # Przewidywane wartości Y z dopasowanej prostej
    Y_pred = slope * X + intercept
    
    # Rysujemy dane oraz linię regresji
    fig, ax = plt.subplots()
    ax.scatter(X, Y, label="Dane (punkty)", alpha=0.7)
    ax.plot(X, Y_pred, color="red", label="Linia regresji")
    ax.set_title("Dopasowanie liniowe: Y = aX + b")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

    st.pyplot(fig)

    # Wyświetlamy oszacowane parametry i statystyki
    st.write(f"**Nachylenie (slope) =** {slope:.3f}")
    st.write(f"**Wyraz wolny (intercept) =** {intercept:.3f}")
    st.write(f"**Współczynnik korelacji (r) =** {r_value:.3f}")
    st.write(f"**Wartość p (p-value) =** {p_value:.3e}")
    st.write(f"**Odchylenie standardowe oszacowania (std_err) =** {std_err:.3f}")

    st.write("""
    Powtórz wywołanie, aby zobaczyć, jak parametry zmieniają się 
    przy nowym losowaniu danych (szum jest generowany za każdym razem).
    """)

