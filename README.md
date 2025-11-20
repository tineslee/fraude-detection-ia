## Detecção de Fraude em Pedidos
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-%F0%9F%9A%80-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-app-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-blue)


Este projeto utiliza aprendizado de máquina para identificar possíveis fraudes em pedidos online.

Ele inclui:

 - Simulação de dados de pedidos
 - Pré-processamento com normalização e codificação
 - Treinamento de modelo com Random Forest e SMOTE
 - API com FastAPI para prever fraudes
 - Interface visual com Streamlit para testes interativos.

---

 ## Técnicas e Algoritmos Utilizados

Este projeto utiliza técnicas de Machine Learning supervisionado para classificar pedidos como legítimos ou fraudulentos. Abaixo estão os principais componentes:

 Tipo de Aprendizado:
- Supervisionado: o modelo aprende com exemplos rotulados (fraude ou não fraude).

Algoritmos:
 - Random Forest Classifier: modelo de ensemble baseado em múltiplas árvores de decisão, robusto contra overfitting e eficaz em dados tabulares.
 - SMOTE (Synthetic Minority Over-sampling Technique): técnica para balancear o conjunto de dados gerando exemplos sintéticos da classe minoritária (fraudes).

Pré-processamento:
 - Normalização do valor do pedido (order_value)
 - Codificação One-Hot para variáveis categóricas (payment_method, location)
 - Remoção de colunas irrelevantes como order_id, order_time, customer_id

Avaliação:
- Matriz de Confusão
- Relatório de Classificação com métricas de precisão, recall e F1-score

---

## Como rodar localmente
1. Clone o repositório
   ```bash
   git clone https://github.com/seu-usuario/fraude-detection-ia.git
   cd fraude-detection-ia
   ```
2. Crie e ative o ambiente virtual
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```
3. Instale as dependências
```bash
pip install -r requirements.txt
```
4. Treine o modelo (opcional)
```bash
python src/model.py
```
---

## Testar a API
```bash
uvicorn src.api:app --reload
```
Acesse a documentação interativa em: http://127.0.0.1:8000/docs

---

## Interface com Streamlit
```bash
streamlit run app_streamlit.py
```

## Autora
Projeto desenvolvido por Thais Ines.
Se quiser contribuir, fique à vontade para abrir issues ou pull requests!




