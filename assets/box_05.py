from butils import *
stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
markets = ["US", "EU"]
df = pd.DataFrame({
    "Stock": np.repeat(stocks, 100),
    "Return (%)": np.random.normal(0, 5, 500),
    "Market": np.tile(np.repeat(markets, 50), 5)
})
p = fboxplot_basic(df, "Stock", "Return (%)", 
               title="💹 Stock Return Distribution by Market",
               palette=["#0077FF", "#FFB000"], tth=0, bgc="#f5faff")



save_plot(p, 'output/box_05')