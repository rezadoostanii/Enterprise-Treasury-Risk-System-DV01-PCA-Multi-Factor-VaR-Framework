---

# 🏦 Enterprise Treasury Risk System (IRRBB / ALM / Market Risk Engine)

### DV01 • PCA Yield Curve • Multi-Factor VaR • ALM • Liquidity • Stress Testing

---

## 📌 Repository Name

```
Enterprise-Treasury-Risk-System-DV01-PCA-Multi-Factor-VaR-Framework
```

---

# 📊 1. Overview

This project is a **bank-level Treasury Risk Management and IRRBB analytics engine** designed to replicate institutional risk infrastructure used in:

* 🏦 ALCO (Asset-Liability Management Committee) reporting
* 📉 Market Risk (VaR / Expected Shortfall frameworks)
* 💰 Interest Rate Risk in the Banking Book (IRRBB - Basel III aligned)
* 📊 Fixed Income & Yield Curve Risk Modeling
* 💧 Liquidity Risk monitoring
* 🔴 Scenario-based macro stress testing

It integrates **real U.S. Treasury yield curve data (FRED API)** with **DV01 sensitivity, PCA factor decomposition, Monte Carlo simulation, and regulatory-style risk reporting**.

---

# 📡 2. Sample Model Output (Latest Execution)

> ⚠ These results represent a **single model run snapshot** for demonstration purposes.

---

## 📈 Yield Curve Snapshot (FRED Data)

| Tenor | Yield |
| ----- | ----- |
| 2Y    | 4.00% |
| 5Y    | 4.13% |
| 10Y   | 4.47% |
| 20Y   | 5.01% |
| 30Y   | 5.02% |

---

# 📉 3. Market Risk (VaR / Expected Shortfall)

## 10-Day Risk Estimates

| Method      | VaR (95%) | ES (97.5%) |
| ----------- | --------- | ---------- |
| Historical  | $105,332  | $170,739   |
| Monte Carlo | $135,475  | $202,516   |
| Bootstrap   | $107,839  | $155,986   |

---

## 📌 Model Output (Representative)

* 💰 **VaR (95%)**: $135,475
* 💰 **ES (97.5%)**: $202,516

---

# 💰 4. Interest Rate Risk (DV01 Engine)

## Key Metrics

* DV01: **$-4,229.99 per 1bp**
* DV01 (100bp shock): **$-422,999**

---

## 📊 DV01 vs Market Risk

| Metric                         | Value    |
| ------------------------------ | -------- |
| DV01 VaR (Parallel Shift Only) | $113,990 |
| Full Market VaR (Multi-Factor) | $135,475 |
| Coverage Ratio                 | 84.1%    |

---

## 📌 Interpretation

DV01 captures **linear parallel rate risk only**, while full VaR includes:

* Yield curve shape risk (PCA Slope / Curvature)
* Credit spread risk
* Non-linear convexity effects

---

# 📊 5. PCA Yield Curve Decomposition

| Factor    | Variance Contribution |
| --------- | --------------------- |
| Level     | 86.33%                |
| Slope     | 11.70%                |
| Curvature | 1.29%                 |

---

## 📌 Insight

* Yield curve risk is dominated by **Level factor**
* Slope drives hedging & relative value trades
* Curvature captures butterfly / convexity effects

---

# 📦 6. Risk Decomposition (Euler Allocation)

| Risk Factor   | Contribution |
| ------------- | ------------ |
| Curve Risk    | $84,146      |
| Spread Risk   | $51,724      |
| Parallel Rate | -$395        |

---

## 📌 Insight

* Majority of risk is **non-parallel (curve + spread)**
* DV01 alone significantly underestimates portfolio risk

---

# 📉 7. Stress Testing Scenarios

## 🔴 2008 Financial Crisis

* PnL: **-$3,007,047**

## 🔴 COVID-19 Shock

* PnL: **-$2,555,784**

## 🔴 2022 Rate Hike Cycle

* PnL: **-$1,895,389**

---

# 🏦 8. ALM (Asset-Liability Management)

| Metric                    | Value       |
| ------------------------- | ----------- |
| Duration Gap              | 1.23 years  |
| EVE (100bp shock)         | -$1,225,000 |
| Net Interest Income (NII) | $3,355,000  |
| NII Volatility            | $145,180    |

---

# 💧 9. Liquidity Risk (LCR)

* LCR: **6.83**
* Status: **PASS**

---

# 📊 10. Model Validation (Backtesting)

## Kupiec Test (POF)

* ✅ Passed (p = 0.4363)

## Christoffersen Test (Independence)

* ✅ Passed (p = 1.0000)

---

## 📌 Interpretation

Backtesting results indicate **acceptable model performance under standard VaR validation frameworks**.

---

# 🏛 11. ALCO Governance Dashboard

| Metric       | Value   | Limit   | Status    |
| ------------ | ------- | ------- | --------- |
| VaR (95%)    | 135,475 | 150,000 | ⚠ Warning |
| ES (97.5%)   | 202,516 | 200,000 | 🔴 Breach |
| Duration Gap | 1.23    | 2.0     | OK        |
| LCR          | 6.83    | 1.2     | OK        |

---

## 📌 Overall Status

> ⚠ **Risk Limit Breach Detected (1 metric exceeded threshold)**

---

# 🧠 12. System Architecture

```
DATA LAYER
(FRED Yield Curve Data)
        ↓
DATA ENGINE
(Cleaning + Curve Construction)
        ↓
────────────────────────────────────────
DV01 ENGINE | PCA ENGINE | SPREAD ENGINE
────────────────────────────────────────
        ↓
RISK SIMULATION ENGINE
(Monte Carlo / Bootstrap / Historical)
        ↓
VaR & ES AGGREGATION LAYER
        ↓
────────────────────────────────────────
ALM ENGINE        LIQUIDITY ENGINE
(EVE / NII / DGAP) (LCR / Cashflow Stress)
────────────────────────────────────────
        ↓
GOVERNANCE LAYER
(ALCO Dashboard + Limit Monitoring)
```

---

# 🚀 13. Key Features

* Multi-factor yield curve modeling (PCA-based)
* DV01 + Key Rate Risk engine
* Full VaR decomposition (Euler allocation)
* Credit spread risk modeling
* Scenario-based macro stress testing
* Basel-style backtesting (Kupiec / Christoffersen)
* ALM + IRRBB integration
* Liquidity coverage monitoring
* ALCO governance reporting layer

---

# 🧰 14. Tech Stack

Python | NumPy | Pandas | SciPy | scikit-learn | FRED API | Monte Carlo Simulation | PCA | Financial Risk Modeling

---

# 🏁 15. Final Risk Summary

| Metric       | Value    |
| ------------ | -------- |
| VaR (95%)    | $135,475 |
| ES (97.5%)   | $202,516 |
| DV01 VaR     | $113,990 |
| Spread VaR   | $80,198  |
| Duration Gap | 1.23     |
| LCR          | 6.83     |

---

# 🏦 Conclusion

This system integrates:

> 📉 Market Risk + 🏦 IRRBB / ALM + 💧 Liquidity Risk + 📊 Regulatory Backtesting

into a unified **institutional-grade Treasury Risk Engine** suitable for ALCO reporting, risk management, and fixed income analytics.

---

# 👤 Author

Quantitative Risk & Treasury Analytics Engineer
Focus Areas:

* Market Risk (VaR / ES)
* Interest Rate Risk (DV01 / IRRBB)
* ALM & Balance Sheet Risk
* Fixed Income Risk Modeling
* Factor-Based Risk Decomposition

---

