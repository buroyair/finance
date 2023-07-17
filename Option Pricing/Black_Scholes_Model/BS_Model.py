import numpy as np
from scipy.stats import norm



# Black-Scholes formula
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    call = (S * norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * norm.cdf(d2, 0.0, 1.0))
    return call, d1, d2, -d1, -d2, norm.cdf(d1, 0.0, 1.0), norm.cdf(-d1, 0.0, 1.0), norm.cdf(d2, 0.0, 1.0), norm.cdf(-d2, 0.0, 1.0)

def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    put = (K * np.exp(-r * T) - S + black_scholes_call(S, K, T, r, sigma)[0])
    return put, d1, d2, -d1, -d2, norm.cdf(d1, 0.0, 1.0), norm.cdf(-d1, 0.0, 1.0), norm.cdf(d2, 0.0, 1.0), norm.cdf(-d2, 0.0, 1.0)

# Parameters
S = 60.0 
K=50 # Current stock price
T = 1.0       # Time until option expiration in years
r = 0.05      # Risk-free interest rate
sigma = 0.1
# Calculate Black-Scholes price for call and put
call_option_price, d1_call, d2_call, minus_d1_call, minus_d2_call, Nd1_call, Nminusd1_call, Nd2_call, Nminusd2_call = black_scholes_call(S, K, T, r, sigma)
put_option_price, d1_put, d2_put, minus_d1_put, minus_d2_put, Nd1_put, Nminusd1_put, Nd2_put, Nminusd2_put = black_scholes_put(S, K, T, r, sigma)

print("Call Option:")
print("The call option price calculated with the Black-Scholes model is: ", call_option_price)
print("d1 for the call option is: ", d1_call)
print("d2 for the call option is: ", d2_call)
print("N(d1) for the call option is: ", Nd1_call)
print("N(d2) for the call option is: ", Nd2_call)
print("\n")


print("Put Option:")
print("The put option price calculated with the Black-Scholes model is: ", put_option_price)
print("-d1 for the put option is: ", minus_d1_put)
print("-d2 for the put option is: ", minus_d2_put)
print("N(-d1) for the put option is: ", Nminusd1_put)
print("N(-d2) for the put option is: ", Nminusd2_put)
