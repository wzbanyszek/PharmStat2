# From Theory to Practice: Using a Linear Model in PharmStat2 (Python/AI) for Stability Analyses

In this continuation of our series on modern statistical methods in pharmacy, we show how a linear model, implemented in the **PharmStat2** tool (based on Python/AI), offers a straightforward way to evaluate stability and forecast the shelf life of medicinal products. You’ll learn how to prepare data in Excel, perform key calculations in line with ICH guidelines (Q1A(R2), Q1E), and conduct analyses in seconds to assess and predict product stability.

---

## 1. Stability Assessment – Why Linear Regression?

A pivotal aspect of a medicinal product’s stability study is determining how a specific quality parameter (e.g., active substance content, impurity levels) changes over time. In practice, according to ICH guidelines ([Q1A(R2)](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-stability-testing-new-drug-substances-products-step-5_en.pdf), [Q1E](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-e-evaluation-stability-data-step-5_en.pdf)), a **simple linear model** often suffices to depict the relationship:

result = a + b * t

- \( t \) – storage time (e.g., in months),  
- \( a \) (intercept) – the initial value of the parameter,  
- \( b \) (slope) – the rate of change (e.g., %/month).

**Why is a linear function sufficient?**  
According to industry observations and publications (e.g., “*Handbook of Stability Testing in Pharmaceutical Development: Regulations, Methodologies, and Best Practices*,” ed. K. Huynh-Ba, Springer 2009), when a parameter’s degradation does not exceed about a dozen percentage points in the studied period, the change is approximately linear. As a result, it becomes straightforward to predict the point at which the parameter crosses its specification limit. Only in extreme cases (very high depletion or multi-stage reactions) might higher-order equations be considered.

---

## 2. Steps for Stability Analysis – From Source Data to Interpretation

Practical application of linear regression in stability assessment involves several steps:

1. **Preliminary Trend Check**  
   Before running a regression, it’s worth evaluating whether the data genuinely show an increase or decrease in the parameter over time. Often, some series exhibit a significant change, while others do not—suggesting stability depends on technological or quality factors, or storage conditions.

2. **Correlation Assessment**  
   Linear regression usually reports a correlation coefficient (r). If r is low (near 0) and the significance test indicates no relationship (p-value > 0.05), the parameter’s change may simply be measurement noise. Where r is high (close to ±1), there is solid evidence that the degradation process (or another change) truly depends on time.

3. **Slope and Intercept**  
   - **Slope (b)** shows how quickly the parameter changes each month (e.g., percentage loss per month). Comparing slopes among different series can reveal the impact of packaging, storage conditions (e.g., standard 25°C ± 2°C / 60% ± 5% RH or 30°C ± 2°C / 65% ± 5% RH), manufacturing technology, or even the active substance supplier.  
   - **Intercept (a)** corresponds to the initial value of the quality attribute. Significant differences in intercepts may indicate variations in the production process or raw material quality.

4. **Combining Results from Different Series**  
   Guideline [Q1E](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-e-evaluation-stability-data-step-5_en.pdf) describes statistical tests (e.g., ANCOVA) to check whether the stability results for several series can be presented together. If, statistically, their slopes and intercepts do not differ significantly, combining data simplifies evaluating the product at the overall process level.

5. **Forecasting Shelf Life**  
   Using the regression equation, we determine when the parameter hits the specification limit (e.g., 1% maximum impurity) by solving \( a + b \times t = \text{limit} \). Yet we must account for the **confidence interval** (usually 95%) to estimate how accurately the prediction aligns with reality. ICH Q1E recommends providing such intervals to avoid inflating the predicted shelf life.

---

## 3. How to Use PharmStat2 for This?

**PharmStat2 (online tool)** – [https://pharmstat2.streamlit.app/](https://pharmstat2.streamlit.app/) – is a Python/AI-based platform that automates stability data analysis:

### a) Preparing the Data

- **First row in Excel**: parameter name (e.g. “API Content” or “Impurity A”).  
- **`Time` column** – containing storage time in months.  
- *(Optional)* **`Min` and `Max` columns** – if you want the report to show when a limit is reached.  
- **Subsequent columns** – results for each series (e.g., Series_1, Series_2…).

Sample Excel file (download link):  
[https://docs.google.com/spreadsheets/d/1tMSGOBJkq9zxpLugE51UZUjVWGpji8dK/edit?usp=sharing&ouid=118120522004481145097&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1tMSGOBJkq9zxpLugE51UZUjVWGpji8dK/edit?usp=sharing&ouid=118120522004481145097&rtpof=true&sd=true)

### b) Analysis in PharmStat2

1. **Upload your file** in the Stability module.  
2. **Select the series** you want to analyze (all or just some).  
3. **Run the calculations** – the tool creates a scatter plot with a regression line and, optionally, a 95% confidence interval.

### c) Interpreting the Results

- **Graph**: check the trend, slope, and compare different series.  
- **Regression Results table**:  
  - *Slope* – the parameter’s rate of change,  
  - *Intercept* – the starting value,  
  - *r-value, p-value* – correlation strength and statistical significance,  
  - *Predicted_time* – the approximate time to reach the upper spec limit (if you defined `Max`).  
- **Conclusions**: whether degradation is slow/fast, or if there’s a difference between series, etc.

---

## 4. Further Notes on Stability Conditions

According to [Q1A(R2)](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-stability-testing-new-drug-substances-products-step-5_en.pdf), choosing stability conditions involves, e.g.:

- **Long-term**: 25°C ± 2°C / 60% ± 5% RH or 30°C ± 2°C / 65% ± 5% RH,  
- **Accelerated**: 40°C ± 2°C / 75% ± 5% RH,  
- **Intermediate**: 30°C ± 2°C / 65% ± 5% RH, used if “significant changes” occur under accelerated conditions.

Evaluating linear regression under these various conditions facilitates conclusions on product stability and possible extrapolation over a longer timeframe (consistent with Q1E recommendations).

---

## Conclusion

**Linear regression** remains central to assessing a medicinal product’s quality and safety over time. Proper interpretation of slope and intercept, correlation, and the ability to combine results from multiple series (as statistically warranted) form key elements of the approach recommended by ICH Q1A(R2) and Q1E.  
**PharmStat2** (Farmstat2) automates this process—simply provide a properly prepared Excel file, and within moments, you’ll have plots and tables showing pivotal indicators (slope, correlation, predicted shelf life). Consequently, you can swiftly determine whether the product retains the required quality throughout the intended storage period.

**We’d love to hear your thoughts**: do you use linear models in your stability research? Or do you have experience with more complex methods? Feel free to share practical examples!
