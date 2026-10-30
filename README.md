# Cross-Market Mispricing in Bitcoin Prediction Markets

This repository contains the empirical code, selected outputs, an illustrative data sample, and the full PDF of my MSc thesis in Economics and Finance at Luiss Guido Carli University.

The project examines pricing efficiency in prediction markets, using Bitcoin-linked contracts as an empirical setting.

## Thesis

**Cross-Market Mispricing in Bitcoin Prediction Markets: Evidence from Polymarket, Kalshi, and Deribit**

[**Read the full thesis (PDF)**](thesis/Giannandrea_De_Stefano_Thesis.pdf)

The thesis examines whether prices observed in Bitcoin-related prediction markets differ systematically from a model-based probability benchmark constructed using Bitcoin spot prices and Deribit's DVOL implied-volatility index.

The empirical analysis focuses on Polymarket and Kalshi. Observed prediction-market prices are interpreted as event probabilities subject to market frictions and compared with the DVOL-based benchmark.

## Research Question

Do prices in Bitcoin-related prediction markets on Polymarket and Kalshi differ systematically from a model-based probability benchmark constructed using Bitcoin spot prices and Deribit DVOL?

## Data

The empirical analysis combines:

- Polymarket Bitcoin-related prediction markets.
- Kalshi KXBTC event contracts.
- Bitcoin spot prices from Binance.
- Deribit DVOL implied-volatility data.

The final matched dataset contains:

- **19,649** Polymarket terminal-contract observations.
- **10,323** Polymarket path-dependent observations.
- **3,135** Kalshi contracts, sampled using the first timestamped trade within 30 minutes of market opening.
- **33,107** observations in the unified dataset.
- **6,566** unique contracts.

Sample coverage extends from **March 2024 to June 2026**, with coverage varying across platforms and contract types.

## Methodology

The empirical pipeline includes:

- API-based prediction-market data collection.
- Contract parsing and classification.
- Timestamp and maturity matching.
- Matching of Bitcoin spot prices and DVOL inputs according to information availability.
- Construction of a lognormal, Black–Scholes-style probability benchmark.
- Signed and absolute pricing-difference measures.
- Descriptive analysis.
- Bootstrap inference.
- OLS regressions with heteroskedasticity-robust and clustered standard errors.
- Monthly and horizon-based robustness checks.

### Probability Benchmark

For terminal events such as $S_T > K$, the benchmark probability is based on a lognormal terminal-price distribution:

$$
p_{\text{benchmark}} = \Phi(d_2)
$$

Here, $\Phi$ denotes the standard normal cumulative distribution function. The value of $d_2$ is computed using the matched Bitcoin spot price, strike, time to maturity, and DVOL-based volatility input under the assumptions described in the thesis.

The benchmark is interpreted as a **risk-neutral-style probability proxy**, rather than as a physical probability forecast. It does not represent a direct extraction of strike-specific probabilities from the full option surface.

### Pricing Differences

Signed pricing differences are defined as:

$$
\Delta p = p_{\text{market}} - p_{\text{benchmark}}
$$

A positive value indicates that the observed prediction-market price exceeds the model-based benchmark probability.

The term **mispricing** refers to these measured differences. A deviation from the benchmark does not, by itself, establish that the market price is incorrect.

### Information Availability and Contract Comparability

Benchmark inputs are matched according to when the underlying information would have been available at each observation timestamp, to avoid look-ahead bias.

Terminal and path-dependent contracts are analysed separately because their payoff structures differ. A terminal-price benchmark does not fully represent the probability of an event occurring at any point before maturity.

## Key Findings

The principal result concerns the **Polymarket terminal-contract sample**, comprising **19,649 observations across 2,847 markets**.

- The market-level mean signed pricing difference is **0.007496**, equivalent to approximately **0.75 percentage points**.
- The **95% bootstrap confidence interval** is **[0.006709, 0.008285]**, equivalent to approximately **[0.67, 0.83] percentage points**.
- The estimate remains positive under monthly aggregation and is almost unchanged under a seven-day maturity restriction. The latter removes only 33 observations, providing a limited additional robustness check.

Larger average differences are observed for Kalshi and Polymarket path-dependent contracts. These estimates are interpreted separately because of differences in contract design, sampling, trading environment, and comparability with the terminal benchmark.

The findings document systematic pricing differences relative to the chosen benchmark. They **do not establish forecasting errors, causal relationships, or executable arbitrage opportunities**.

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

thesis/
    Giannandrea_De_Stefano_Thesis.pdf
```
## Notebooks

The empirical workflow is organised sequentially:

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

## Data Availability and Reproducibility

The complete raw, processed, and final research datasets are **not redistributed in this repository**.

A small illustrative sample of the matched dataset is available at:

```text
data_sample/unified_prediction_market_sample.csv
```

This sample documents the structure of the empirical dataset and the main variables used in the analysis. It is not intended to reproduce the complete empirical results.

The notebooks document the data-collection, matching, benchmark-construction, descriptive-analysis, and empirical procedures.

Because the full research datasets are not included, the repository is **not a one-click reproduction package**. Running the complete workflow requires the relevant input data and environment configuration. Recollection from external APIs may also be affected by changes in data availability or API behaviour.

## Outputs

The `outputs/` directory contains selected empirical results produced by the notebooks, including:

- Pricing-difference distributions.
- Contract-type comparisons.
- Monthly pricing-difference figures.
- Descriptive statistics.
- Bootstrap confidence intervals.
- Regression and robustness results.

The thesis provides the full discussion of these results and their interpretation.

## Main Limitations

The analysis is subject to several limitations:

- **Benchmark specification:** probabilities depend on the lognormal model and the use of DVOL as a volatility proxy.
- **Option-surface information:** a single volatility index does not capture the full strike- and maturity-specific implied-volatility surface.
- **Payoff comparability:** path-dependent events are not fully represented by a terminal-price benchmark.
- **Sampling differences:** Polymarket and Kalshi use different observation-selection procedures, limiting direct comparisons.
- **Market frictions:** fees, bid–ask spreads, liquidity, execution constraints, and settlement rules affect the economic interpretation of observed differences.
- **Probability interpretation:** prediction-market prices and risk-neutral-style benchmark probabilities need not coincide with physical event probabilities.

These limitations are considered when interpreting the empirical evidence.

## Project Status

**Completed MSc thesis research project.**

## Author

**Giannandrea De Stefano**  
MSc Economics and Finance — Major in Finance  
Luiss Guido Carli University

**Supervisor:** Professor Nicola Borri  
**Co-supervisor:** Professor Emilio Barone  
**Academic year:** 2025/2026

## Disclaimer

This repository is intended for academic and research purposes.

The benchmark probabilities are model-based proxies and should not be interpreted as investment forecasts or trading recommendations. Observed pricing differences do not, by themselves, imply executable trading opportunities.

Nothing in this repository constitutes investment advice.
