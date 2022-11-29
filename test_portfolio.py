import portfolio
import pandas as pd

df = pd.read_csv("df_moving_averages.csv").drop("Unnamed: 0", axis=1)
p = portfolio.Portfolio(df)

p.buy(4, 10)
p.sell(4, 9.9)
print(p.evaluate())