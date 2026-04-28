# Yahoo-Finance-API

## Overview
This project analyzes historical closing prices of major technology stocks:

- **AAPL** — Apple  
- **MSFT** — Microsoft  
- **NVDA** — NVIDIA  
- **META** — Meta  
- **ADBE** — Adobe  

The objective is to visualize price movements over time and evaluate the quality of the dataset using simple data reliability indicators.

---

## Analysis Workflow

- Data collection and preprocessing  
- Time series visualization of closing prices  
- Comparative trend observation  
- Data quality evaluation (KPIs)  

---

## Key Observations

- All stocks exhibit natural market volatility  
- **NVDA** shows a strong upward trend toward the end of the period  
- **ADBE** displays a consistent downward movement  
- Other stocks fluctuate within relatively stable ranges  
- No visible gaps or anomalies in the dataset  

---

## Data Quality Summary

| Stock | Completeness | Latency | Accuracy | Consistency |
|------|-------------|--------|----------|------------|
| AAPL | 100% | 0 days | OK | OK |
| MSFT | 100% | 0 days | OK | OK |
| NVDA | 100% | 0 days | OK | OK |
| META | 100% | 0 days | OK | OK |
| ADBE | 100% | 0 days | OK | OK |

✔ The dataset is complete, consistent, and reliable for further analysis.

---

## Visualizations

### Apple (AAPL)
![AAPL](images/aapl.png)

### Microsoft (MSFT)
![MSFT](images/msft.png)

### NVIDIA (NVDA)
![NVDA](images/nvda.png)

### Meta (META)
![META](images/meta.png)

### Adobe (ADBE)
![ADBE](images/adbe.png)

---

## Tools & Technologies

- Python  
- Pandas  
- Matplotlib  

---

## Conclusion

Basic time series visualization already reveals meaningful insights into stock behavior.  
The dataset’s quality makes it a strong foundation for more advanced analysis, such as predictive modeling.

---

## Future Work

- Apply LSTM / GRU models for forecasting  
- Compare model performance across stocks  
- Incorporate additional financial indicators  
