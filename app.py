import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tytuł aplikacji
st.title("Aplikacja z wyborem typu wykresu (matplotlib + Streamlit)")

# Ustawienie liczby losowych wierszy
num_rows = st.slider("Liczba wierszy danych:", 5, 100, 20)

a = st.sidebar.radio("Select one:", [1, 2])
import reglin
