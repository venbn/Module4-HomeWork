The code would initially perform analysis on given portfolios and further understand their market performance by performing some risk analysis, and then the same would be done on the new custom portfolios extracted using GOOGLE Finance sheets, finally extracting the performance data by combining and comparing both the original and the custom portfolios.

Below are the step-by-step details of what code will be doing :

1. Read the below csv files into pandas data frames and convert the date columns into DataTimeIndex format with Date column as the index 
  
   whale_returns.csv
   algo_returns.csv
   sp500_history.csv

2. Display the data from the data frames
3. Drop the Nulls 
4. Combine all the data frames


