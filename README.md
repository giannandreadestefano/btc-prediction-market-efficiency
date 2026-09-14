# Cross-Market Mispricing in Bitcoin Prediction Markets

This repository contains the empirical code, selected outputs, and an illustrative data sample from my MSc thesis in Economics and Finance at LUISS Guido Carli.

## Thesis

**Cross-Market Mispricing in Bitcoin Prediction Markets: Evidence from Polymarket, Kalshi, and Deribit**

The thesis examines whether probabilities observed in Bitcoin-related prediction markets differ systematically from a benchmark derived from Bitcoin spot prices and Deribit's DVOL implied-volatility index.

The empirical analysis focuses on Polymarket and Kalshi and compares observed prediction-market probabilities with a DVOL-based benchmark probability.

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

The sample covers the period from **March 2024 to June 2026**.

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

For terminal events such as \(S_T > K\), the benchmark probability is based on the Black-Scholes terminal distribution:

$$
P(S_T > K) = \Phi(d_2)
$$

where \(d_2\) is computed using the matched Bitcoin spot price, strike, time to maturity, and DVOL-based volatility input.

The benchmark is interpreted as a **risk-neutral-style probability proxy**, rather than as a physical probability forecast.

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
    tables/      Selected descriptive and empirical results

data_sample/
    unified_prediction_market_sample.csv
```

## Notebooks

The empirical workflow is organized sequentially:

1. **01_polymarket_data.ipynb**  
   Collects and prepares Bitcoin-related Polymarket market data.

2. **02_kalshi_data.ipynb**  
   Collects and prepares Kalshi KXBTC contracts and timestamped trade data.

3. **03_deribit_data.ipynb**  
   Collects Bitcoin spot and Deribit DVOL data used to construct the benchmark.

4. **04_dataset_construction.ipynb**  
   Parses contracts, matches market observations with the benchmark inputs, and constructs the empirical samples.

5. **05_descriptive_analysis.ipynb**  
   Produces descriptive statistics, distributions, contract-type comparisons, and monthly figures.

6. **06_empirical_analysis.ipynb**  
   Performs the main statistical tests, bootstrap inference, regressions, and robustness analyses.

## Data Availability

The complete raw, processed, and final research datasets are **not redistributed in this repository**.

A small illustrative sample of the matched dataset is available in:

```text
data_sample/unified_prediction_market_sample.csv
```

This sample is provided to document the structure of the empirical dataset and the main variables used in the analysis.

The complete notebooks are included to document the data-collection, matching, benchmark-construction, descriptive-analysis, and empirical procedures.

Because the full research datasets are not included, the repository should not be interpreted as a one-click reproduction package of the complete thesis dataset.

## Outputs

The `outputs/` directory contains selected empirical results produced by the notebooks, including:

- mispricing distributions
- contract-type comparisons
- monthly pricing-difference figures
- descriptive statistics
- bootstrap confidence intervals
- regression and robustness outputs

## Project Status

**MSc thesis empirical project completed.**

## Author

**Giannandrea De Stefano**  
MSc Economics and Finance  
LUISS Guido Carli

## Disclaimer

This repository is intended exclusively for academic and research purposes.

The benchmark probabilities used in the analysis are model-based proxies and should not be interpreted as investment forecasts or trading recommendations.

Nothing in this repository constitutes investment advice.
