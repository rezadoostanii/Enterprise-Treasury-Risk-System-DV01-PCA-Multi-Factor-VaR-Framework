# ============================================================
# ENTERPRISE TREASURY RISK SYSTEM (DEMO SHOWCASE ONLY)
# ============================================================
# ⚠ This code is for demonstration purposes only.
# ⚠ Not designed for production reuse or integration.
# ============================================================

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# CONFIG (SAFE - NO REAL KEY EXPOSURE)
# ============================================================

API_KEY = "FRED_API_KEY_HIDDEN_FOR_SECURITY"
PORTFOLIO_VALUE = 5_000_000

np.random.seed(42)

# ============================================================
# SIMPLE DEMO ENGINE (REDUCED COMPLEXITY)
# ============================================================

class DemoRiskEngine:
    def __init__(self, portfolio_value):
        self.portfolio_value = portfolio_value

    def simulate_returns(self, n=1000):
        return np.random.normal(0, 0.01, n)

    def calculate_var(self, returns, alpha=0.05):
        return -np.percentile(returns, alpha * 100) * self.portfolio_value

    def calculate_es(self, returns, alpha=0.05):
        var_threshold = np.percentile(returns, alpha * 100)
        tail = returns[returns <= var_threshold]
        return -np.mean(tail) * self.portfolio_value

# ============================================================
# DV01 SIMULATION (SIMPLIFIED)
# ============================================================

def dv01_demo(portfolio_value):
    shock_bp = 1
    dv01 = portfolio_value * 0.0001 * 5.2  # synthetic duration
    return dv01

# ============================================================
# MAIN SHOWCASE RUN
# ============================================================

def run_demo():

    print("\n======================================================")
    print("🏦 ENTERPRISE TREASURY RISK SYSTEM - DEMO RUN")
    print("======================================================\n")

    engine = DemoRiskEngine(PORTFOLIO_VALUE)

    returns = engine.simulate_returns(2000)

    var = engine.calculate_var(returns)
    es = engine.calculate_es(returns)
    dv01 = dv01_demo(PORTFOLIO_VALUE)

    print("📊 RISK METRICS (SIMULATED)")
    print("--------------------------------")
    print(f"VaR (95%):        ${var:,.2f}")
    print(f"Expected Shortfall:${es:,.2f}")
    print(f"DV01 (approx):    ${dv01:,.2f} per 1bp")

    print("\n📌 NOTE:")
    print("This is a simplified demonstration model.")
    print("Full implementation contains PCA, ALM, Liquidity, and Monte Carlo engines.")

    print("\n======================================================")
    print("END OF DEMO")
    print("======================================================\n")

# ============================================================
# ENTRY POINT (SAFE)
# ============================================================

if __name__ == "__main__":
    run_demo()