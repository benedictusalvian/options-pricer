import math
from scipy.stats import norm
from print_tables import print_tables
from get_global_quote import get_global_quote

index = input("Input Delta One Index ETF: ") # The Delta One Index ETF
S = get_global_quote(index) # Underlying price of Delta One Index ETF
# S = round(float(input("Input price of your chosen index: ")))
K = S # Strike price
T = 0.5 # Time to expiration (in years)
r = 0.0446 # Risk-free rate (U.S. 10 Year Treasury Note, currently 4.46%)
vol = 0.12 # Volatility (Say, 12%)

table_datas = []

for i in range(4):
    T = 0.25 * (i + 1)
    table_data = [[f"{int(T * 12)} months away"], ["Calls", "Strike", "Puts"]]
    step = round(0.01 * S) or 1
    for j in range(S - (10 * step), S + (10 * step) + 1, step):
        K = j
        d1 = (math.log(S / K) + (r + 0.5 * vol ** 2) * T) / (vol * math.sqrt(T))
        d2 = d1 - (vol * math.sqrt(T))
        C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        table_data.append([round(C, 2), K, round(P, 2)])
    table_datas.append(table_data)

print("\nOption Chain for Delta One Index ETF", index, "for underlying market price of", S, "\n")
print_tables(table_datas)
print()