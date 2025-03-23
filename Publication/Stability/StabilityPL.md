#Od teorii do praktyki: wykorzystanie modelu liniowego w PharmStat2 (Python/AI) do analiz stabilności

---

## 1. Ocena stabilności – dlaczego regresja liniowa?

Jednym z kluczowych elementów programu badań stabilności produktu leczniczego jest określenie, jak dany parametr jakościowy (np. zawartość substancji czynnej, poziom zanieczyszczeń) zmienia się w czasie. W praktyce, zgodnie z wytycznymi ICH (m.in. [Q1A(R2)](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-stability-testing-new-drug-substances-products-step-5_en.pdf) i [Q1E](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-e-evaluation-stability-data-step-5_en.pdf)), często wystarcza prosty **model liniowy**, który opisuje relację:

\[
\text{parametr} = a + b \times t
\]

- \( t \) – czas przechowywania (np. w miesiącach),  
- \( a \) (wyraz wolny) – wartość początkowa danego parametru,  
- \( b \) (nachylenie) – tempo zmiany parametru (np. %/miesiąc).

**Dlaczego wystarcza funkcja liniowa?**  
Zgodnie z obserwacjami oraz publikacjami branżowymi (np. „*Handbook of Stability Testing in Pharmaceutical Development: Regulations, Methodologies, and Best Practices*”, ed. K. Huynh-Ba, Springer 2009), gdy degradacja parametru nie przekracza kilkunastu procent w badanym okresie, zmiana bywa w przybliżeniu liniowa. Dzięki temu łatwo przewidzieć punkt, w którym parametry przekroczą specyfikację. Dopiero w skrajnych przypadkach (bardzo duży ubytek, reakcje wieloetapowe) rozważa się wyższe rzędy równań.

---

## 2. Kroki analizy stabilności – od danych źródłowych do interpretacji

Praktyczne wykorzystanie regresji liniowej w ocenie stabilności polega na szeregu kroków:

1. **Wstępne sprawdzenie trendu**  
   Zanim obliczymy regresję, warto ocenić, czy dane faktycznie wskazują na wzrost lub spadek parametru w czasie. Często część serii wykaże istotną zmianę, a inne serie – nie. To sugeruje, że stabilność może zależeć od czynników technologicznych, jakościowych lub warunków przechowywania.

2. **Ocena korelacji**  
   Regresja liniowa zwykle zwraca współczynnik korelacji (r). Jeśli wartość r jest niska (bliska 0) i test istotności sugeruje brak zależności (p-value > 0.05), zmiana parametru może wynikać z szumu pomiarowego. Gdy r jest wysoki (bliski ±1), mamy solidne podstawy, by uznać, że zachodzący proces degradacji (lub inna zmiana) naprawdę zależy od czasu.

3. **Nachylenie i wyraz wolny**  
   - **Nachylenie (slope)** wskazuje, jak szybko parametr zmienia się co miesiąc (np. tempo ubytku w %/mies.). Porównanie nachyleń między różnymi seriami pozwala ocenić wpływ opakowania, warunków przechowywania (np. standardowe 25°C ± 2°C / 60% ± 5% RH lub 30°C ± 2°C / 65% ± 5% RH), technologii wytwarzania czy nawet dostawcy substancji czynnej.  
   - **Wyraz wolny (intercept)** odpowiada wartości początkowej danej cechy jakościowej. Istotne różnice w interceptach mogą świadczyć o zmianach w procesie produkcji albo w jakości surowca.

4. **Łączenie wyników z różnych serii**  
   Wytyczne [Q1E](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-e-evaluation-stability-data-step-5_en.pdf) opisują testy statystyczne (np. analiza ANCOVA) pozwalające sprawdzić, czy wyniki stabilności dla kilku serii można przedstawić wspólnie. Jeżeli w skali statystycznej nie różnią się istotnie nachyleniem i wyrazem wolnym, łączenie danych ułatwia ocenę produktu na poziomie całego procesu.

5. **Prognoza okresu ważności**  
   Mając równanie regresji, wyznaczamy czas, w którym parametr osiągnie limit specyfikacji (np. 1% maksymalnego zanieczyszczenia). Rozwiązujemy \( a + b \times t = \text{limit} \). Należy jednak uwzględnić **przedział ufności** (zwykle 95%), co pozwala oszacować, na ile pewnie predykcja pokrywa się z rzeczywistością. ICH Q1E zaleca podawanie takich przedziałów, aby uniknąć zawyżenia okresu ważności.

---

## 3. Jak wykorzystać do tego Pharmstat2?

### a) Przygotowanie danych

- Pierwszy wiersz w Excelu: nazwa parametru (np. „Zawartość API” lub „Zanieczyszczenie A”).
- Kolumna `Time` – zawierająca czas w miesiącach.
- (Opcjonalnie) Kolumny `Min` i `Max` – jeśli chcemy, by raport pokazywał przecięcie z limitem specyfikacji.
- Kolejne kolumny – wyniki dla każdej serii (np. Seria_1, Seria_2…).

### b) Analiza w Pharmstat2

1. **Wgraj plik** w module dot. stabilności.  
2. **Zaznacz serie** do analizy (możesz wybrać wszystkie lub tylko część).  
3. **Uruchom obliczenia** – narzędzie stworzy wykres rozrzutu z linią regresji i (opcjonalnie) przedziałem ufności 95%.

### c) Interpretacja wyników

- **Wykres**: odczytujemy trend, nachylenie, a także porównujemy różne serie.  
- **Tabela Regression Results**:  
  - *Slope* – tempo zmiany parametru.  
  - *Intercept* – wartość startowa.  
  - *r-value*, *p-value* – siła i istotność korelacji.  
  - *Predicted_time* – przybliżony czas do osiągnięcia górnego limitu specyfikacji (jeśli zdefiniowaliśmy kolumnę `Max`).  
- **Wnioski**: czy tempo degradacji jest niskie/wysokie, czy jedna seria różni się od drugiej, itp.

---

## 4. Dodatkowe uwagi o warunkach stabilności

Zgodnie z [Q1A(R2)](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-stability-testing-new-drug-substances-products-step-5_en.pdf), dobór warunków stabilności obejmuje m.in.:

- **Long-term** (przechowywanie długoterminowe): np. 25°C ± 2°C / 60% ± 5% RH lub 30°C ± 2°C / 65% ± 5% RH,  
- **Accelerated** (przyspieszone): np. 40°C ± 2°C / 75% ± 5% RH,  
- **Intermediate** (pośrednie): np. 30°C ± 2°C / 65% ± 5% RH, stosowane gdy wystąpią „znaczące zmiany” w warunkach przyspieszonych.

Ocena regresji liniowej w tych różnych warunkach pozwala wyciągać wnioski na temat stabilności produktu i ewentualnie ekstrapolować dane na dłuższy okres (zgodnie z zaleceniami Q1E).

---

## Podsumowanie

Analiza stabilności przy użyciu **regresji liniowej** pozostaje fundamentem oceny jakości i bezpieczeństwa produktu leczniczego w czasie. Zrozumienie nachylenia i wyrazu wolnego, korelacji oraz możliwość łączenia wyników z różnych serii (o ile statystyka to dopuszcza) to kluczowe elementy postępowania zalecanego przez wytyczne ICH Q1A(R2) i Q1E.  
**Pharmstat2** (Farmstat2) automatyzuje ten proces – wystarczy odpowiednio przygotowany plik Excel, by w kilka chwil wygenerować wykresy i tabele z istotnymi wskaźnikami (nachyleniem, korelacją, predykcją terminu wygaśnięcia). W efekcie możemy szybko ocenić, czy produkt zachowa wymaganą jakość przez zakładany okres przechowywania.

**Zachęcam do podzielenia się swoimi spostrzeżeniami w komentarzach** – czy w swoich badaniach stabilności też korzystacie z modeli liniowych? A może macie doświadczenia z bardziej rozbudowanymi analizami? Chętnie porozmawiam o praktycznych przykładach!
