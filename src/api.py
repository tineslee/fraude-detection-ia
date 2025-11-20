from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import joblib
from src.preprocess import preprocess_data, simulate_orders
from src.model import train_model

# Inicializar FastAPI
app = FastAPI(title="Fraud Detection API")

# Carregar modelo treinado ou treinar novo
try:
    model = joblib.load("modelo_fraude.pkl")
    print("Modelo carregado de 'modelo_fraude.pkl'")
except FileNotFoundError:
    print("Modelo não encontrado, treinando novo...")
    model = train_model()

# Definir estrutura de entrada
class Order(BaseModel):
    order_value: float
    payment_method: str
    location: str

@app.post("/predict")
def predict(order: Order):
    """
    Recebe um pedido e retorna se é fraude ou não.
    """
    # Criar DataFrame com os dados recebidos
    df = pd.DataFrame([order.dict()])

    # Pré-processar: normalização usando valores fixos ou salvos do treino
    # Exemplo: média=100, std=50 (ajuste conforme seu treino real)
    mean_order_value = 100
    std_order_value = 50
    df["order_value_norm"] = (df["order_value"] - mean_order_value) / std_order_value

    # One-hot encoding
    df = pd.get_dummies(df, columns=["payment_method", "location"], drop_first=True)

    # Ajustar colunas para bater com treino
    for col in model.feature_names_in_:
        if col not in df.columns:
            df[col] = 0

    # Fazer previsão
    prediction = model.predict(df[model.feature_names_in_])[0]
    result = "Fraude detectada" if prediction == 1 else "Pedido legítimo"

    return {"prediction": int(prediction), "message": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
