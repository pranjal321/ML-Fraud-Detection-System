# ML Fraud Detection System

An end-to-end **AI/ML-based Fraud Detection Prototype** that assigns a fraud risk score to online orders and recommends business actions such as **Approve**, **Manual Review**, or **Cancel**.

This project demonstrates applied machine learning, business-driven decision logic, explainability, and deployment readiness.

---

##  Project Overview

Online transactions are highly vulnerable to fraud, leading to revenue loss and increased operational costs.  
Manual fraud review is expensive, slow, and not scalable.

This project builds an **automated, explainable fraud risk scoring system** that:
- Predicts fraud probability (0–1)
- Balances fraud detection with customer experience
- Keeps humans in the loop for critical decisions

---

## Key Features

- Synthetic but realistic fraud dataset
- Domain-driven feature engineering
- Interpretable ML model (Logistic Regression)
- Threshold tuning based on business cost
- Interactive **Streamlit demo**
- Executive + technical presentation
- Short project walkthrough video

---

## Dataset

- **Type:** Synthetic (for demo & learning purposes)
- **Size:** ~300 transactions
- **Label:** `chargeback_flag` (1 = fraud, 0 = legitimate)

### Key Columns
- `amount`
- `billing_country`, `shipping_country`
- `payment_avs_result`, `payment_cvv_result`
- `num_orders_last_7_days`
- `is_first_time_buyer`
- `chargeback_flag`

File:


---

##  Feature Engineering

Business logic is converted into numerical features:

- Log-transformed order amount
- Billing vs shipping country mismatch
- AVS / CVV failure indicators
- Transaction velocity (orders in last 7 days)
- First-time buyer flag
- High velocity indicator (derived)

This improves both **model performance** and **explainability**.

---

##  Model Approach

- **Algorithm:** Logistic Regression  
- **Why Logistic Regression?**
  - Probability-based risk scoring
  - High interpretability
  - Industry-standard baseline for fraud detection

### Training Details
- Train-test split with stratification
- Feature scaling using `StandardScaler`
- Class imbalance handled with `class_weight="balanced"`
- Regularization to prevent overfitting

---

## 📈 Evaluation Strategy

Metrics used:
- ROC-AUC (ranking quality)
- Confusion Matrix
- Precision & Recall (fraud-focused metrics)

> Accuracy is **not** treated as the primary metric due to class imbalance.

---

## Threshold Tuning

Different thresholds were evaluated:

| Threshold | Behavior |
|---------|----------|
| 0.3 | High fraud recall, high manual review load |
| 0.5 | Balanced trade-off (**selected**) |
| 0.7 | Fewer false positives, higher fraud miss risk |

Threshold selection is based on **business cost**, not accuracy.

---

## Decision Logic

| Fraud Score | Action |
|-----------|--------|
| > 0.8 | Cancel Order |
| 0.5 – 0.8 | Manual Review / ID Verification |
| < 0.5 | Auto Approve |

This ensures **human-in-the-loop governance**.

---

## Live Demo (Streamlit)

A Streamlit-based UI allows real-time fraud prediction.

Users can input:
- Order amount
- Payment verification results
- Behavioral signals

Outputs:
- Fraud risk score (0–1)
- Business recommendation
  
- <img width="1910" height="1012" alt="20 02 2026_11 03 00_REC" src="https://github.com/user-attachments/assets/0a0e1ef7-0598-4f5d-98a7-a9c8d5433b43" />








