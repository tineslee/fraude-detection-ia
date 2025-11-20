import pandas as pd
import numpy as np

def simulate_orders(n=1000, seed=42):
    """
    Simula um dataset de pedidos com possíveis fraudes.
    """
    np.random.seed(seed)

    # Simulação de dados
    order_id = np.arange(1, n+1)
    customer_id = np.random.randint(1, 200, n)
    order_value = np.random.exponential(scale=100, size=n).round(2)
    payment_method = np.random.choice(["credit_card", "debit_card", "pix", "boleto"], n)
    order_time = pd.date_range("2025-01-01", periods=n, freq="h")
    location = np.random.choice(["SP", "RJ", "MG", "RS", "BA"], n)

    # Label de fraude (simulação simples)
    fraud = np.random.choice([0, 1], n, p=[0.9, 0.1])

    # Criação do DataFrame
    df = pd.DataFrame({
        "order_id": order_id,
        "customer_id": customer_id,
        "order_value": order_value,
        "payment_method": payment_method,
        "order_time": order_time,
        "location": location,
        "fraud": fraud
    })

    return df


def preprocess_data(df):
    """
    Limpeza e preparação dos dados.
    """
    # Remover valores nulos (se houver)
    df = df.dropna()

    # Normalizar valores numéricos
    df["order_value_norm"] = (df["order_value"] - df["order_value"].mean()) / df["order_value"].std()

    # Codificação de variáveis categóricas
    df = pd.get_dummies(df, columns=["payment_method", "location"], drop_first=True)

    return df


if __name__ == "__main__":
    # Simular dataset
    df = simulate_orders(n=500)
    print("Dataset simulado:")
    print(df.head())

    # Pré-processar
    df_clean = preprocess_data(df)
    print("\nDataset após pré-processamento:")
    print(df_clean.head())
