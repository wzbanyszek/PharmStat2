# From Theory to Practice: Using a Linear Model in PharmStat2 (Python/AI) for Stability Analyses

In this continuation of our series on employing modern tools for statistical analysis in the pharmaceutical field, we demonstrate how a linear model, implemented in the PharmStat2 tool (based on Python/AI), provides a straightforward way to assess stability and predict the shelf life of medicinal products. You will learn how to prepare data in Excel, perform key calculations in line with ICH guidelines (Q1A(R2), Q1E), and evaluate as well as forecast product stability.

---

## 1. Stability Assessment – Why Linear Regression?

A core aspect of a medicinal product’s stability program is determining how a given quality parameter (e.g., active substance content, impurity levels) changes over time. In practice, according to ICH guidelines (including [Q1A(R2)](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-stability-testing-new-drug-substances-products-step-5_en.pdf) and [Q1E](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-e-evaluation-stability-data-step-5_en.pdf)), a **simple linear model** often suffices to describe the relationship:

result = a + b * t

- \( t \) – storage time (e.g., in months),  
- \( a \) (intercept) – the initial value of the parameter,  
- \( b \) (slope) – the rate of change (e.g., %/month).

**Why is a linear function sufficient?**  
According to observations and industry publications (e.g., “*Handbook of Stability Testing in Pharmaceutical Development: Regulations, Methodologies, and Best Practices*,” ed. K. Huynh-Ba, Springer 2009), when the parameter’s degradation does not exceed about a dozen percentage points over the study period, the change is approximately linear. As a result, it becomes easy to predict when the parameter will surpass its specification limit. Only in extreme cases (very high depletion, multi-stage reactions) are higher-order equations generally considered.

---

## 2. Steps in Stability Analysis – From Raw Data to Interpretation

Practical use of linear regression for stability assessment consists of several steps:

1. **Preliminary Trend Check**  
   Before running a regression, it is advisable to determine whether the data genuinely show an increase or decrease in the parameter over time. Frequently, some batches exhibit a significant change, while others do not—suggesting that stability may hinge on technological factors, quality variables, or storage conditions.

2. **Correlation Assessment**  
   The strength of the relationship between variables is given by the correlation coefficient (r). If r is low (close to 0) and statistical testing indicates no relationship (p-value > 0.05), any parameter change could be due to measurement noise. When r is high (close to ±1), we have solid grounds to conclude that the ongoing degradation process (or other change) truly depends on time.

3. **Slope and Intercept**  
   - **Slope (b)** indicates how quickly the parameter changes over time (e.g., a depletion rate in %/month). Comparing slopes across different batches reveals the impact of packaging, storage conditions (e.g., the standard 25°C ± 2°C / 60% ± 5% RH or 30°C ± 2°C / 65% ± 5% RH), manufacturing technology, or active-substance suppliers.  
   - **Intercept (a)** is the initial value of the quality attribute. Significant differences in intercept among various batches can point to changes in the production process or raw material quality.

4. **Combining Results from Different Batches**  
   Guideline [Q1E](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-e-evaluation-stability-data-step-5_en.pdf) describes statistical tests (e.g., ANCOVA) to determine whether stability results for multiple batches can be presented jointly. If, statistically, there is no significant difference in slope and intercept, combining data simplifies the product evaluation and enhances the statistical power of the findings.

5. **Forecasting Shelf Life**  
   Once the regression equation is set, we find the time at which the parameter reaches the specification limit (e.g., 1% maximum impurity) by solving \( a + b \times t = \text{limit} \). However, we must consider the **confidence interval** (usually 95%), which estimates how closely the prediction matches reality. ICH Q1E recommends reporting such intervals to avoid overstating shelf life.

---

## 3. How to Use PharmStat2 for This?

PharmStat2 (online tool) – [https://pharmstat2.streamlit.app/](https://pharmstat2.streamlit.app/) – is a Python/AI-based platform enabling automated stability data analysis:

### a) Preparing the Data

- First row in Excel: parameter name (e.g., “API Content” or “Impurity A”).  
- **`Time`** column – containing time in months.  
- *(Optional)* **`Min` and `Max`** columns – if you want the report to indicate when a spec limit is reached.  
- Additional columns – results for each batch (e.g., Batch_1, Batch_2…).

Sample Excel file (download link):
[https://docs.google.com/spreadsheets/d/1tMSGOBJkq9zxpLugE51UZUjVWGpji8dK/edit?usp=sharing&ouid=118120522004481145097&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1tMSGOBJkq9zxpLugE51UZUjVWGpji8dK/edit?usp=sharing&ouid=118120522004481145097&rtpof=true&sd=true)

### b) Analysis in PharmStat2

1. **Upload the file** in the Stability module.  
2. **Select batches** for analysis (all or just some).  
3. **Run the calculations** – the tool generates a scatter plot with a regression line and (optionally) a 95% confidence interval.

### c) Interpreting the Results

- **Plot**: observe the trend, slope, and compare different batches.  
- **Regression Results table**:  
  - *Slope* – the parameter’s rate of change,  
  - *Intercept* – the starting value,  
  - *r-value*, *p-value* – correlation strength and statistical significance,  
  - *Predicted_time* – approximate time to reach the spec limit (if `Max` or `Min` were defined).  
- **Conclusions**: whether the degradation rate is high/low, and if one batch differs from another, etc.

---

## 4. Additional Remarks on Stability Conditions

Per [Q1A(R2)](https://www.ema.europa.eu/en/documents/scientific-guideline/ich-q-1-stability-testing-new-drug-substances-products-step-5_en.pdf), selecting stability conditions typically covers:

- **Long-term**: e.g., 25°C ± 2°C / 60% ± 5% RH or 30°C ± 2°C / 65% ± 5% RH,  
- **Accelerated**: e.g., 40°C ± 2°C / 75% ± 5% RH,  
- **Intermediate**: e.g., 30°C ± 2°C / 65% ± 5% RH, used if “significant changes” appear under accelerated conditions.

Linear regression under these varying conditions allows us to draw conclusions on product stability and potentially extrapolate the data over a longer period (consistent with Q1E guidelines).

---

## Summary

Stability analysis using **linear regression** remains fundamental for assessing a medicinal product’s quality and safety throughout its shelf life. Proper interpretation of slope and intercept, correlation, and the ability to merge results from different batches (where statistics permit) form the key elements recommended by ICH Q1A(R2) and Q1E.  
**Pharmstat2** (Farmstat2) automates this approach—just prepare an Excel file appropriately, and in a matter of moments, you’ll have plots and tables featuring critical indicators (slope, correlation, predicted expiry). As a result, you can swiftly determine whether the product maintains the required quality over the intended storage period.

**We encourage you to share your insights in the comments**—do you also use linear models for stability research? Or do you have experience with more advanced analyses? I’d be delighted to discuss practical examples!
