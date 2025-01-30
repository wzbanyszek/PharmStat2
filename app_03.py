import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dane
t = np.array([0, 3, 6, 9, 12, 18, 24])  # Punkty czasowe w miesiącach
y_test = np.array([0.18, 0.35, 0.38, 0.52, 0.58, 0.65, 0.71])  # Poziomy zanieczyszczeń w %

# Regresja liniowa
slope, intercept, r_value, p_value, std_err = linregress(t, y_test)
y_pred = intercept + slope * t

# Obliczanie przedziału ufności
residuals = y_test - y_pred
std_resid = np.std(residuals, ddof=2)

# Linie dla regresji
t_line = np.linspace(0, 24, 100)
y_line = intercept + slope * t_line

# Górny i dolny limit przedziału ufności
n = len(t)
mean_x = np.mean(t)
conf_interval = 1.96 * std_resid * np.sqrt(1/n + (t_line - mean_x)**2 / np.sum((t - mean_x)**2))

y_upper = y_line + conf_interval
y_lower = y_line - conf_interval

# Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.plot(t, y_test, 'o', label='Zaobserwowane dane', color='blue')
plt.plot(t_line, y_line, '-', label='Linia regresji', color='red')
plt.fill_between(t_line, y_lower, y_upper, color='gray', alpha=0.3, label='95% Przedział ufności')

# Linia specyfikacji
plt.axhline(y=1.0, color='green', linestyle='--', label='Limit specyfikacji (1%)')

# Adnotacje i legenda
plt.xlabel('Czas (miesiące)')
plt.ylabel('Poziom zanieczyszczeń (%)')
plt.title('Analiza regresji z przedziałem ufności')
plt.legend()

# Wyświetlanie równania regresji
equation = f"y = {intercept:.2f} + {slope:.2f}x"
plt.text(1, 0.8, equation, fontsize=12, color='red')

plt.grid(True)
plt.show()
