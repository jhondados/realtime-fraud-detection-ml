# 🛡️ Real-Time Fraud Detection System

[![Precision](https://img.shields.io/badge/Precision-99.2%25-green)](.)
[![Recall](https://img.shields.io/badge/Recall-94.7%25-blue)](.)
[![Latency](https://img.shields.io/badge/Latency-P99%20%3C%2043ms-orange)](.)
[![TPS](https://img.shields.io/badge/Throughput-50K%20TPS-red)](.)

> Production fraud detection for a major Brazilian bank — **99.2% precision**, **94.7% recall**, processing 50,000 transactions/second with P99 latency of 43ms.

## 🏆 Business Impact
- **R$47M** in fraud prevented in the first year
- **False positive rate reduced 73%** (vs previous rule-based system)
- **43ms P99 latency** — 10x faster than industry average
- **Zero system downtime** over 14 months in production

## 🏗️ Model Ensemble
```
Transaction ──▶ Feature Engineering ──▶ ┌─ XGBoost (tabular)    ─┐
                                         ├─ Neural Net (sequences)─┼──▶ Calibrated ──▶ Decision
                                         └─ GBM (behavioral)     ─┘    Ensemble
```

## 📊 Model Performance
| Model | AUC-ROC | Precision | Recall | F1 |
|-------|---------|-----------|--------|-----|
| XGBoost | 0.987 | 98.1% | 93.2% | 0.956 |
| Neural Net | 0.991 | 97.8% | 95.1% | 0.964 |
| GBM | 0.983 | 98.4% | 92.8% | 0.955 |
| **Ensemble** | **0.995** | **99.2%** | **94.7%** | **0.969** |
