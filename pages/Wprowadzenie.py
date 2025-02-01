import streamlit as st
from utils.translations import translations


def show(language):
    t = translations[language]

    st.header(t["intro"])
    st.write(f"""
    **{t["intro"]}**  
    Aplikacja umożliwia przeprowadzanie analizy danych statystycznych i jakościowych w prosty i intuicyjny sposób. W bocznym menu znajdziesz moduły, które pomogą Ci w analizie danych z różnych perspektyw.

    **{t["menu_title"]}:**

    1. **{t["intro"]}**  
       {t["intro_desc"]}

    2. **{t["descriptive_stats"]}**  
       {t["descriptive_stats_desc"]}

    3. **{t["histograms"]}**  
       {t["histograms_desc"]}

    4. **{t["boxplot"]}**  
       {t["boxplot_desc"]}

    5. **{t["control_charts"]}**  
       {t["control_charts_desc"]}

    6. **{t["process_capability"]}**  
       {t["process_capability_desc"]}

    7. **{t["stability_regression"]}**  
       {t["stability_regression_desc"]}

    8. **{t["temp_humidity"]}**  
       {t["temp_humidity_desc"]}

    ---
    **{t["how_to_use"]}**  
    - {t["choose_page"]}
    - {t["upload_data"]}
    - {t["view_results"]}
    - {t["customize_view"]}
    """)
