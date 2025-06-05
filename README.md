# Portfolio_Returns
Utilize quantitative analysis techniques with Python and Pandas, and you want to determine which portfolio is performing the best across multiple areas: volatility, returns, risk, and Sharpe ratios. 

# Instructions 
1. Prepare the Data
2. Perform Quantitative Analysis
3. Create a Custom Portfolio

## Prepare the Data 
Read in and clean several CSV files for analysis. The CSV files contain data on whale portfolio returns, algorithmic trading portfolio returns, and S&P 500 historical prices.

# Perform Quantitative Analysis 
Analyze the data to determine if any of the portfolios outperform the stock market (that is, the S&P 500). Specifically, you will do a performance analysis and a risk analysis, and then calculate rolling statistics and Sharpe ratios. 

## Performance Analysis 
1. Calculate and plot daily returns of all portfolios.
2. Calculate and plot cumulative returns for all portfolios. Does any portfolio outperform the S&P 500?

## Risk Analysis 
1. Create a box plot for each of the returns.
2. Calculate the standard deviation for each portfolio.
3. Determine which portfolios are riskier than the S&P 500.
4. Calculate the annualized standard deviation.

## Rolling Statistics 
1. Calculate and plot the rolling standard deviation for all portfolios, using a 21-day window.
2. Calculate and plot the correlation between each stock to determine which portfolios mimic the S&P 500.
3. Choose one portfolio, then calculate and plot the 60-day rolling beta between that portfolio and the S&P 500.

## Sharpe Ratios 
Investment managers and their institutional investors look at the return-to-risk ratio, not just the returns. After all, if you have two portfolios that each offer a 10% return, yet one is lower risk, you would invest in the lower-risk portfolio, right? Follow these steps:
1. Using the daily returns, calculate the Sharpe ratios and visualize them in a bar plot.
2. Determine whether the algorithmic strategies outperform both the market (S&P 500) and the whales portfolios.

## Create a Custom Portfolio 
1. Use YFinance to choose 3-5 stocks for your portfolio
2. Calculate the portfolio returns
3. Calculate the weighted returns for your portfolio, assuming equal number of shares per stock
4. Add your portfolio returns to the DataFrame with the other portfolios.
5. Run the following analyses:
   * Calculate the annualized standard deviation
   * Calculate and plot the rolling standard deviation with a 21 day windo
   * Calculate and plot the correlation
   * Calculate and plot beta for your portfolio compared to the S&P 60 TSX
   * Calculate the Sharpe ratios and generate a bar plot
6. Determine how does your custom portfolio perform? 
