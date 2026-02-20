# ML Fraud Detection System

## Overview
This project implements an AI/ML-based fraud detection prototype for online orders.
The system assigns a fraud risk score to each transaction and recommends a business action:
Approve, Manual Review, or Cancel.

The solution focuses on explainability, business-driven decision-making,
and practical deployment readiness.

---

## Problem Statement
Online transactions are vulnerable to fraud, leading to revenue loss and operational overhead.
Manual fraud review is costly, slow, and not scalable.

The objective is to build an automated, explainable fraud risk scoring system
that assists fraud teams while keeping humans in the loop.

---

## Dataset
- Synthetic dataset simulating real-world e-commerce transactions
- ~300 records with realistic fraud patterns
- Includes:
  - Order amount
  - Payment verification signals (AVS, CVV)
  - Behavioral features (order velocity)
  - Billing vs shipping country
- `chargeback_flag` used as fraud label


---

## Feature Engineering
Key engineered features:
- Log-transformed order amount
- Billing vs shipping country mismatch
- AVS / CVV failure indicators
- Transaction velocity (orders in last 7 days)
- First-time buyer flag

Domain knowledge is encoded into numerical features to improve model performance
and interpretability.

---

## Model Approach
- Algorithm: Logistic Regression
- Reason for selection:
  - Probability-based fraud scoring
  - High interpretability
  - Industry-standard baseline for fraud detection
- Class imbalance handled using `class_weight="balanced"`
- Feature scaling applied using `StandardScaler`

---

## Evaluation Strategy
- ROC-AUC for ranking quality
- Confusion Matrix for error analysis
- Precision & Recall for fraud trade-off analysis
- Accuracy is not treated as the primary metric

---

## Threshold Tuning
Multiple thresholds were evaluated:
- 0.3 → High fraud recall, high manual review load
- 0.5 → Balanced trade-off (selected threshold)
- 0.7 → Fewer false positives, higher fraud miss risk

Threshold selection is based on business cost, not accuracy.

---

## Decision Logic
Fraud Score → Business Action:
- Score > 0.8 → Cancel order
- Score 0.5–0.8 → Manual review / ID verification
- Score < 0.5 → Auto-approve

This ensures human-in-the-loop governance.

---

## Live Demo
A Streamlit-based UI is provided to demonstrate real-time fraud prediction.


The demo allows users to input order details and instantly receive:
- Fraud risk score (0–1)
- Business recommendation

---

## Project Explanation Video
A short (~5 min) walkthrough video is included that explains:
- Problem statement
- Dataset and features
- Model training & evaluation
- Threshold tuning
- Live Streamlit demo

---

## How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt

### 2. Run Notebook

Open and run all cells in:

main.ipynb

### 3. Run Streamlit Demo
streamlit run streamlit_app.py
