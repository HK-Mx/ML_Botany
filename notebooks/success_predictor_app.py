import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import classification_report
import os

st.set_page_config(page_title="🌿 Tomate Success Predictor", layout="wide")
st.title("🍅 Simulación y Predicción de Éxito en Plantas de Tomate")

# Cargar modelo y scaler
@st.cache_resource
def cargar_modelo():
    modelo = joblib.load("my_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return modelo, scaler

modelo, scaler = cargar_modelo()

# Campos del modelo
campos = [
    "Peso_de_muestra_vegetal_(g)", "Cantidad_de_N_en_muestra_vegetal_(g)", "Cantidad_de_C_en_muestra_vegetal_(g)",
    "Porcentaje_N_de_la_muestra_vegetal", "Porcentaje_C_de_la_muestra_vegetal",
    "Peso_de_muestra_de_fruto_(g)", "Cantidad_de_N_en_muestra_de_fruto_(g)", "Cantidad_de_C_en_muestra_de_fruto_(g)",
    "Porcentaje_N_de_la_muestra_fruto", "Porcentaje_C_de_la_muestra_fruto",
    "Nitrógeno_total_en_planta", "Carbono_total_en_planta", "Nitrógeno_total_en_fruto", "Carbono_total_en_fruto",
    "N1", "N2", "N3", "N4",
    "Primer_peso_fresco_hoja", "Primer_peso_fresco_de_raíz", "Primer_peso_fresco_planta",
    "Primer_peso_seco_hoja", "Primer_peso_seco_de_raíz", "Primer_peso_seco_planta",
    "Harvest_Index_S_(His)", "Root_Index_(Ri)", "CHLOR", "FLV", "ANT", "NBI", "NDVI", "PhipII"
]

st.subheader("🌱 Introduce manualmente los datos de la planta")
valores = {}
with st.form("formulario_manual"):
    for campo in campos:
        valores[campo] = st.number_input(campo, value=0.0, format="%f")
    pred_btn = st.form_submit_button("🔍 Predecir éxito de la planta")

if pred_btn:
    df_manual = pd.DataFrame([valores])
    scaled = scaler.transform(df_manual)
    pred = modelo.predict(scaled)[0]
    st.success("✅ SUCCESS") if pred == 1 else st.error("❌ No será success")
    st.dataframe(df_manual)

st.markdown("---")
st.subheader("🧪 O generar una planta simulada aleatoria")

if st.button("🌿 Simular planta aleatoria"):
    def simular_aleatoria():
        simulada = {}
        for campo in campos:
            media = 0.5 if "porcentaje" in campo.lower() else 1.0
            simulada[campo] = round(np.random.normal(loc=media, scale=0.3), 4)
            simulada[campo] = max(simulada[campo], 0)
        return simulada

    planta_simulada = simular_aleatoria()

    # Forzar 50% success / 50% no success
    forzar = np.random.choice([0, 1])
    intento = 0
    while True:
        df_simulada = pd.DataFrame([planta_simulada])
        scaled = scaler.transform(df_simulada)
        pred = modelo.predict(scaled)[0]
        if pred == forzar or intento > 10:
            break
        planta_simulada = simular_aleatoria()
        intento += 1

    st.subheader("📊 Planta generada")
    st.dataframe(pd.DataFrame([planta_simulada]))
    st.success("✅ Éxito! Esta planta es apta (simulada)") if pred == 1 else st.error("❌ Esta planta no es apta (simulada)")
