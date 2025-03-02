import streamlit as st
import pandas as pd
import requests

# Funkcja do pobrania tokena OAuth2
def get_oauth_token(env="TEST"):
    auth_urls = {
        "TEST": st.secrets["test_url"],
        "PROD": st.secrets["prod_url"]
    }

    credentials = {
        "TEST": {
            "client_id": st.secrets["test_client_id"],
            "client_secret": st.secrets["test_client_secret"],
            "scope": "api://59b16def-a1cb-4802-a8d5-27cdecaeb07b/.default",
            "grant_type": "client_credentials"
        },
        "PROD": {
            "client_id": st.secrets["prod_client_id"],
            "client_secret": st.secrets["prod_client_secret"],
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
        "TEST": st.secrets["test_subscription_key"],
        "PROD": st.secrets["prod_subscription_key"]
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


def show(language):
    # Interfejs użytkownika Streamlit
    st.header("Pobieranie danych z API - PackingMaterial")
    
    # Wybór środowiska (TEST/PROD)
    env = st.radio("Wybierz środowisko:", ["TEST", "PROD"])
    
    if st.button("Pobierz dane"):
        data = get_packing_materials(env)
        if data:
            df = pd.DataFrame(data)
            st.write("### Dane pobrane z API: ")
            st.dataframe(df)
        else:
            st.error("Nie udało się pobrać danych.")
    
    st.info("Aby pobrać dane, wybierz środowisko i kliknij 'Pobierz dane'.")
