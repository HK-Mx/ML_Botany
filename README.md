# 🍅 Predicción Temprana del Éxito en Nuevas Variedades de Tomate

## 🧪 Objetivo de la Tesis

Este proyecto se enmarca en una tesis cuyo objetivo es **desarrollar una nueva variedad de tomate** mediante el cruce de variedades salvajes, con la capacidad de:

- Absorber y aprovechar mejor los **nitratos del suelo**
- Reducir la **contaminación ambiental** por lixiviación de nitratos
- Minimizar los **costes de producción** del cultivo de tomate

El reto: determinar de forma anticipada qué variedades híbridas presentan mayor potencial agronómico y eficiencia nutricional.

---

## 🚜 Contexto Experimental

- Se cultivan **120 variedades híbridas de tomate**, con **6 plantas por variedad**
- A los **2 meses** de cultivo, a la mitad de las plantas se les **reduce al 50% el aporte de nitrógeno**
- A los **2 meses y 20 días**, se realiza el **primer análisis físico-químico y biométrico**
- El experimento continúa durante **6-7 meses** para evaluar desarrollo, producción y comportamiento fisiológico

**Problema**: mantener todas las plantas durante el ciclo completo implica un alto coste en:

- Logística y riego
- Personal capacitado
- Recursos técnicos y espacio

---

## 🤖 Propuesta del Proyecto

Este proyecto propone una **solución basada en machine learning** que permite:

> **Predecir, a partir del primer análisis a los 2 meses y 20 días**, qué plantas tienen alta probabilidad de ser “éxito” y, por tanto, deben continuar en el experimento.

### 🔍 Beneficios

- Eliminar más del **50% de las plantas no prometedoras** tras el primer análisis
- Ahorrar **meses de trabajo y recursos** logísticos
- **Acelerar la toma de decisiones** para futuras campañas de mejora genética

---

## 🧠 Componentes del Sistema

- **Notebook de limpieza y preparación** de datos (variables agronómicas, fotosintéticas y bioquímicas)
- App interactiva en **Streamlit** para simular o introducir datos reales y predecir el éxito
- Módulo de evaluación y comparación de múltiples modelos:
  - Random Forest
  - XGBoost
  - K-Nearest Neighbors
  - GridSearch con optimización de hiperparámetros
- Métrica clave: **F1-Score** (clases desbalanceadas)



