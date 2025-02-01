import pandas as pd

def calculate_descriptive_stats(df):
    """Oblicza statystyki opisowe dla DataFrame."""
    stats = df.agg(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
    stats.loc['RSD (%)'] = (stats.loc['std'] / stats.loc['mean']) * 100
    return stats.round(2)
