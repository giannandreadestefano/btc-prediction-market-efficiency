# Cross-Market Mispricing in Bitcoin Prediction Markets

This repository contains the empirical code and selected outputs from my MSc thesis in Economics and Finance at LUISS Guido Carli.

## Thesis

**Cross-Market Mispricing in Bitcoin Prediction Markets: Evidence from Polymarket, Kalshi, and Deribit**

The thesis studies whether probabilities observed in Bitcoin-related prediction markets differ systematically from a benchmark derived from Bitcoin spot prices and Deribit's DVOL implied-volatility index.

The analysis focuses on Polymarket and Kalshi and compares observed prediction-market probabilities with a DVOL-based Deribit-implied probability proxy.

## Research Question

Do Bitcoin prediction-market prices on Polymarket and Kalshi differ systematically from a DVOL-based Deribit-implied probability benchmark?

## Data

The empirical analysis combines:

- Polymarket Bitcoin-related prediction markets
- Kalshi KXBTC event contracts
- Bitcoin spot prices
- Deribit DVOL implied-volatility data

The final matched dataset contains:

- **19,649** Polymarket terminal-contract observations
- **10,323** Polymarket path-dependent observations
- **3,135** Kalshi contracts using the first timestamped trade within 30 minutes of market opening
- **33,107** observations in the unified dataset
- **6,566** unique contracts

The sample covers the period from March 2024 to June 2026.

## Methodology

The empirical pipeline includes:

- API-based prediction-market data collection
- Contract parsing and classification
- Timestamp and maturity matching
- Bitcoin spot and DVOL matching
- Construction of a Black-Scholes-style probability benchmark
- Signed and absolute pricing-difference measures
- Descriptive analysis
- Bootstrap inference
- OLS regressions with robust and clustered standard errors
- Monthly and horizon-based robustness checks

For terminal events such as \(S_T > K\), the benchmark probability is constructed using the Black-Scholes terminal distribution:

\[
P(S_T > K) = \Phi(d_2)
\]

The benchmark should be interpreted as a risk-neutral-style probability proxy rather than a physical probability forecast.

## Repository Structure

```text
config.py        Project configuration

notebook/
    01_polymarket_data.ipynb
    02_kalshi_data.ipynb
    03_deribit_data.ipynb
    04_dataset_construction.ipynb
    05_descriptive_analysis.ipynb
    06_empirical_analysis.ipynb

outputs/
    figures/     Selected figures from the empirical analysis
    tables/      Selected summary and regression outputs

data_sample/
    Small illustrative sample of the final matched dataset
