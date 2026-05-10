# BTC Prediction Market Efficiency

This repository documents my MSc thesis project on pricing efficiency in binary prediction markets, with a focus on Bitcoin-related event contracts.

## Thesis Topic

**Pricing Efficiency in Binary Prediction Markets — Evidence from BTC Derivatives**

The project investigates whether event probabilities observed on prediction markets such as Polymarket and Kalshi are consistent with derivatives-implied benchmarks from Bitcoin options and volatility markets.

## Research Objective

The main objective is to compare binary prediction-market probabilities with benchmarks derived from BTC derivatives markets, in order to identify pricing deviations, probability miscalibration and potential cross-market inefficiencies.

## Data Sources

The empirical analysis is expected to use:

- Polymarket binary prediction market data
- Kalshi event probability data
- Deribit BTC derivatives data
- BTC spot and futures market data

## Methodology

The empirical pipeline includes:

- Prediction-market data collection through APIs
- Market and maturity matching
- Probability extraction from binary contracts
- Derivatives-implied benchmark construction
- Mispricing measurement
- Probability calibration analysis
- OLS and predictive regressions

## Current Status

Work in progress — MSc thesis project.

The repository currently documents the research design and methodology. Code, figures and empirical outputs will be added progressively as the thesis develops.

## Planned Repository Structure

```text
src/          Python scripts for data collection, matching and regressions
notebooks/    Exploratory analysis and empirical checks
figures/      Output charts and diagnostics
data_sample/  Small illustrative data samples only
paper/        Thesis-related documents, if publicly shareable
```

## Disclaimer

This repository is intended for academic and research purposes only. It does not constitute investment advice.
