import streamlit as st
import pandas as pd
import requests

# Funkcja do pobrania tokena OAuth2
def get_oauth_token(env="TEST"):
    auth_urls = {
        "TEST": "https://login.microsoftonline.com/edf3cfc4-ee60-4b92-a2cb-da2c123fc895/oauth2/v2.0/token",
        "PROD": "https://login.microsoftonline.com/edf3cfc4-ee60-4b92-a2cb-da2c123fc895/oauth2/v2.0/token"
    }

    credentials = {
        "TEST": {
            "client_id": "a2cf6053-8fcb-4132-a725-0ca7e46bce17",
            "client_secret": "c7.8Q~cf3sJpPg4yCQ1slBdiTXcXz6oe9CljCcIw",
            "scope": "api://59b16def-a1cb-4802-a8d5-27cdecaeb07b/.default",
            "grant_type": "client_credentials"
        },
        "PROD": {
            "client_id": "cef38701-1021-4a78-a0c5-4b5f35b1a024",
            "client_secret": "3qL8Q~hwsFtoSi4IDR0d65oDBlAhpPORra7IGc14",
            "scope": "api://4611a98a-c4b4-4951-9f88-11d2d43443c8/.default",
            "grant_type": "client_credentials"
        }
    }

    response = requests.post(auth_urls[env], data=credentials[env])

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        st.error(f"Błąd pobierania tokena ({env}): {response.status_code} {response.text}")
        return None

# Funkcja do pobrania danych z API
def get_packing_materials(env="TEST"):
    api_urls = {
        "TEST": "https://apimgmtdev.polpharma.net/external/Santo/packingMaterial",
        "PROD": "https://apimgmt.polpharma.net/external/Santo/packingMaterial"
    }

    subscription_keys = {
        "TEST": "44c58909c0484c3487082eb3ef9b30b7",
        "PROD": "c16c25a654364fa2b295419dd6c36902"
    }

    token = get_oauth_token(env)
    if not token:
        return None

    headers = {
        "Authorization": f"Bearer {token}",
        "Ocp-Apim-Subscription-Key": subscription_keys[env]
    }

    response = requests.get(api_urls[env], headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Błąd pobierania danych ({env}): {response.status_code} {response.text}")
        return None

# Interfejs użytkownika Streamlit
st.header("Pobieranie danych z API - PackingMaterial")

# Wybór środowiska (TEST/PROD)
env = st.radio("Wybierz środowisko:", ["TEST", "PROD"])

if st.button("Pobierz dane"):
    data = get_packing_materials(env)
    if data:
        df = pd.DataFrame(data)
        st.write("### Dane pobrane z API:")
        st.dataframe(df)
    else:
        st.error("Nie udało się pobrać danych.")

st.info("Aby pobrać dane, wybierz środowisko i kliknij 'Pobierz dane'.")
