import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data = {
    "AAPL": yf.download("AAPL", period="3mo"),
    "MSFT": yf.download("MSFT", period="5mo"),
    "NVDA": yf.download("NVDA", period="7mo"),
    "META": yf.download("META", period="9mo"),
    "ADBE": yf.download("ADBE", period="11mo"),
}

report = {}

for ticker, df in data.items():
    print(f"\nProcessing {ticker}...")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    completeness = df.notnull().mean().mean() * 100

    last_date = df.index[-1]
    latency = (datetime.datetime.now() - last_date.to_pydatetime()).days

    accuracy = bool((df['High'] >= df['Low']).all())
    consistency = bool((df['Volume'] >= 0).all())

    report[ticker] = {
        "Completeness (%)": round(completeness, 2),
        "Latency (days)": latency,
        "Accuracy": "OK" if accuracy else "Issue",
        "Consistency": "OK" if consistency else "Issue"
    }

    df['Close'].plot(title=f"{ticker} Closing Price")
    plt.show()

kpi_df = pd.DataFrame(report).T

print("\n=== KPI SUMMARY ===")
print(kpi_df)
