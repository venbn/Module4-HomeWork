# Initial imports
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path

%matplotlib inline

# Reading whale returns

wr_csv=Path('whale_returns.csv')
wr_df=pd.read_csv(wr_csv, index_col='Date', parse_dates=True, infer_datetime_format=True)
wr_df.index=pd.DatetimeIndex(wr_df.index)
wr_df.head()

# Count nulls
wr_df.isnull().sum()

# Drop nulls

wr_dn=wr_df.dropna()
wr_dn.head()

# Reading algorithmic returns

ar_csv=Path('algo_returns.csv')
ar_df=pd.read_csv(ar_csv, index_col="Date", parse_dates=True, infer_datetime_format=True)
ar_df.index=pd.DatetimeIndex(ar_df.index)
ar_df.head()

# Count nulls

ar_df.isnull().sum()

# Drop nulls

ar_dn=ar_df.dropna()
ar_dn.head()

# Reading S&P 500 Closing Prices

sph_csv=Path('sp500_history.csv')
sph_df=pd.read_csv(sph_csv, index_col="Date", parse_dates=True, infer_datetime_format=True)
sph_df.index=pd.DatetimeIndex(sph_df.index)
sph_df.head()

# Check Data Types

sph_df.dtypes

# Calculate Daily Returns

sph_dl=sph_df.pct_change()
sph_dl.head()

# Drop nulls

sph_dl=sph_dl.dropna()
sph_dl.head()

# Rename `Close` Column to be specific to this portfolio.

sph_dl.columns=['SP500DR']
sph_dfr=sph_dl.head()
sph_dfr.head()

# Join Whale Returns, Algorithmic Returns, and the S&P 500 Returns into a single DataFrame with columns for each portfolio's returns.

merge_df=pd.concat([wr_dn,ar_dn,sph_dfr], axis="columns", join="inner")
merge_df.columns=["SFM","PC","TGM","BH","A1","A2","SP500"]
merge_df.head()

# Plot daily returns of all portfolios

combined_dr=merge_df.pct_change()
combined_dr.plot(figsize=(20, 10), title="Daily Returns of all Portfolios")

# Calculate cumulative returns of all portfolios

combined_cumr = (1 + combined_dr).cumprod() - 1
combined_cumr.head()

# Plot cumulative returns

combined_cumr.plot(figsize=(20, 10), title="Cumulative Returns of all Portfolios")

# Box plot to visually show risk

merge_df.plot.box(figsize=(20, 10), title="Portfolio Risk")

# Calculate the daily standard deviations of all portfolios

daily_std=merge_df.std()
daily_std.sort_values()

# Calculate  the daily standard deviation of S&P 500

sp500_daily_std=merge_df['SP500'].std()
sp500_daily_std

# Determine which portfolios are riskier than the S&P 500

var=merge_df.var()
sort_var=var.sort_values(ascending=True)

print(f"Variances of all the portfolios : \n")
print(f"{sort_var}\n")

sort_var.plot.bar(figsize=(20, 10), title="Portfolio Risk")

print(f" Higher the Variance of a portfolio, higher the volatility = higher the risk")
print(f" \n BERKSHIRE HATHAWAY INC and ALGO-1 are riskier portfolios than SP500 because they have an higher variances")

# Calculate the annualized standard deviation (252 trading days)

annual_std=merge_df*np.sqrt(252)
annual_std.head()

# Calculate the rolling standard deviation for all portfolios using a 21-day window

merge_std=merge_df.rolling('21d').std()

# Plot the rolling standard deviation

merge_std.plot(figsize=(20, 10), title="21 days Rolling Standard Deviation")

# Calculate the correlation

import seaborn as sns
correlation=merge_df.corr()

# Display de correlation matrix

correlation

# Calculate covariance of a single portfolio

pc_cov=np.cov(merge_df['A1'])
print(f"Covariance of Algo 1 : {pc_cov}\n")

# Calculate variance of S&P 500

sp_var=merge_df['SP500'].var()
print(f"Variance of SP500 is : {sp_var}")

# 30 day rolling variance

rolling_var_sp500=merge_df['SP500'].rolling('30d').var()

# Computing beta

rolling_cov_sp500=merge_df['SP500'].rolling('30d').cov(merge_df['SP500'])
rolling_cov_sp500

rolling_cov_asp=merge_df['A1'].rolling('30d').cov(merge_df['SP500'])

rolling_beta=rolling_cov_asp / rolling_var

rolling_beta.plot(figsize=(20, 10), title="Beta trend of ALGO 1 against SP500")

# Use `ewm` to calculate the rolling window

merge_ewm=merge_df.ewm(halflife='21 days',times=pd.DatetimeIndex(merge_df.index)).std()
merge_ewm.plot(figsize=(20, 10), title="Exponential Weighted Moving Average with a 21-day half life")

# Annualized Sharpe Ratios

sharpes_ratios = (merge_df.mean() * 252) / (merge_df.std() * np.sqrt(252))
sharpes_ratios

# Visualize the sharpe ratios as a bar plot

sharpes_ratios.plot.bar()

# Reading data from 1st stock

goog_csv=Path('goog.csv')
goog_df=pd.read_csv(goog_csv, index_col='Date', parse_dates=True, infer_datetime_format=True)
goog_df.index=pd.DatetimeIndex(goog_df.index)
goog_df.head()

# Reading data from 2nd stock

twtr_csv=Path('twtr.csv')
twtr_df=pd.read_csv(twtr_csv, index_col='Date', parse_dates=True, infer_datetime_format=True)
twtr_df.index=pd.DatetimeIndex(twtr_df.index)
twtr_df.head()

# Reading data from 3rd stock

nyse_csv=Path('nyse.csv')
nyse_df=pd.read_csv(nyse_csv, index_col='Date', parse_dates=True, infer_datetime_format=True)
nyse_df.index=pd.DatetimeIndex(nyse_df.index)
nyse_df.head()

# Combine all stocks in a single DataFrame

combined_df=pd.concat([goog_df,twtr_df,nyse_df], axis="columns", join="inner")
combined_df.head()

# Reset Date index

combined_df.reset_index(inplace=False)
combined_df.head()

# Reorganize portfolio data by having a column per symbol

combined_df.columns=['GOOG','TWTR','NYSE']
combined_df.head()

# Calculate daily returns

combined_daily_returns=combined_df.pct_change()
combined_daily_returns

# Drop NAs

combined_dn=combined_daily_returns.dropna()

# Display sample data

combined_dn

# Set weights

weights = [1/3, 1/3, 1/3]

# Calculate portfolio return

portfolio_returns=combined_dn.dot(weights)

# Display sample data

portfolio_returns.head(10)

# Join your returns DataFrame to the original returns DataFrame

all_portfolios=pd.concat([merge_df,combined_dn],axis="columns",join="inner")
all_portfolios.head()

# Only compare dates where return data exists for all the stocks (drop NaNs)

all_portfolios.dropna()
all_portfolios.head()

# Calculate the annualized `std`

all_portfolios_std=all_portfolios.std()*np.sqrt(252)
all_portfolios_std.head()

# Calculate rolling standard deviation

all_portfolios_std=all_portfolios.rolling('21d').std()

# Plot rolling standard deviation

all_portfolios_std.plot(figsize=(20, 10), title="21 days Rolling Standard Deviation of all portfolios")

# Calculate and plot the correlation

import seaborn as sns
correlation_all_portfolios=all_portfolios.corr()

# Display de correlation matrix

correlation_all_portfolios

# Calculate and plot Beta

## 60 day rolling variance of SP500

rolling_var60_sp500=all_portfolios['SP500'].rolling('60d').var()

## 60 day rolling covarience of GOOGLE 

rolling_goog_cov60_sp500=all_portfolios['GOOG'].rolling('60d').cov(all_portfolios['SP500'])

## Calculating beta for GOOGLE vs SP500

beta=rolling_goog_cov60_sp500 / rolling_var60_sp500

## Plotting the beta trend

beta.plot(figsize=(20, 10), title="Beta trend of GOOGLE vs SP500")

# Calculate Annualized Sharpe Ratios

sharpes_ratios_all = (all_portfolios.mean() * 252) / (all_portfolios.std() * np.sqrt(252))
sharpes_ratios_all

# Visualize the sharpe ratios as a bar plot
sharpes_ratios_all.plot.bar()

print(f"\nSharpe ratio of my portfolio is trending upwards compared to the original portfolio which means, the investment performance is good. The original portfolio's sharpe ratio is less than 1 which is not a good investment performance.\n")
