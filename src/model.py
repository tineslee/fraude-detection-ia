import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from src.preprocess import simulate_orders, preprocess_data

def train_model():
    # 1. Simular e pré-processar dados
    df = simulate_orders(n=1000)
    df_clean = preprocess_data(df)

    # 2. Separar features e target
    X = df_clean.drop(columns=["fraud", "order_id", "order_time", "customer_id"])
    y = df_clean["fraud"]

    # 3. Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # 4. Aplicar SMOTE no conjunto de treino
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    # 5. Treinar modelo com balanceamento
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)

    # 6. Avaliar modelo
    y_pred = model.predict(X_test)
    print("Relatório de Classificação:")
    print(classification_report(y_test, y_pred))
    print("\nMatriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    # 7. Salvar modelo treinado
    joblib.dump(model, "modelo_fraude.pkl")
    print("Modelo salvo em 'modelo_fraude.pkl'")

    return model

if __name__ == "__main__":
    model = train_model()
