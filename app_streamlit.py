import streamlit as st
import pandas as pd
import joblib

# Carregar modelo treinado
model = joblib.load("modelo_fraude.pkl")

# Parâmetros usados na normalização
mean_order_value = 100
std_order_value = 50

# Título
st.title("🕵️‍♀️ Detecção de Fraude em Pedidos")

# Formulário de entrada
order_value = st.number_input("Valor do Pedido (R$)", min_value=0.0, step=10.0)
payment_method = st.selectbox("Forma de Pagamento", ["credit_card", "debit_card", "pix", "boleto"])
location = st.selectbox("Localização", ["SP", "RJ", "MG", "BA", "RS"])

# Botão de previsão
if st.button("Verificar Pedido"):
    # Criar DataFrame
    df = pd.DataFrame([{
        "order_value": order_value,
        "payment_method": payment_method,
        "location": location
    }])

    # Pré-processar
    df["order_value_norm"] = (df["order_value"] - mean_order_value) / std_order_value
    df = pd.get_dummies(df, columns=["payment_method", "location"], drop_first=True)

    # Ajustar colunas
    for col in model.feature_names_in_:
        if col not in df.columns:
            df[col] = 0

    # Prever
    prediction = model.predict(df[model.feature_names_in_])[0]
    if prediction == 1:
        st.error("🚨 Fraude detectada!")
    else:
        st.success("✅ Pedido legítimo.")
