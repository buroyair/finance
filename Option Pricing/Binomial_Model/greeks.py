import numpy as np
from scipy.stats import norm
import pandas as pd
from IPython.display import display, Markdown

# parameters
S = 100      # underlying price
K = 100      # strike price
T = 20/52   # time to maturity in years
r = 0.05    # risk-free rate
σ =  0.3   # volatility

# calculations
d1 = (np.log(S/K) + (r + 0.5 * σ**2) * T) / (σ * np.sqrt(T))
d2 = d1 - σ * np.sqrt(T)

# Delta:
# Measures the rate of change of option value with 
# respect to changes in the underlying asset price
Delta_Call = norm.cdf(d1)  

# Gamma: 
# Measures the rate of change in the delta with 
# respect to changes in the underlying price
Gamma_Call = norm.pdf(d1) / (S * σ * np.sqrt(T))  

# Vega: 
# Measures sensitivity to volatility
Vega_Call = S * np.sqrt(T) * norm.pdf(d1)

# Theta: 
# Measures the sensitivity of the value of the 
# derivative to the passage of time (the "time decay")
Theta_Call = -(S * norm.pdf(d1) * σ / (2 * np.sqrt(T))) - r * K * np.exp(-r * T) * norm.cdf(d2)  

# Rho: 
# Measures sensitivity to the interest rate
Rho_Call = K * T * np.exp(-r * T) * norm.cdf(d2)  

# Delta for Put Option
Delta_Put = Delta_Call - 1

# Theta for Put Option
Theta_Put = Theta_Call + r * K * np.exp(-r * T)

# Rho for Put Option
Rho_Put = -K * T * np.exp(-r * T) * norm.sf(d2)  # norm.sf is survival function, which is 1 - cdf

# Store Greeks in a dataframe for comparison
greek_data = {'Call': [Delta_Call, Gamma_Call, Vega_Call, Theta_Call, Rho_Call], 
              'Put': [Delta_Put, Gamma_Call, Vega_Call, Theta_Put, Rho_Put]}

df = pd.DataFrame(greek_data, index=['Delta', 'Gamma', 'Vega', 'Theta', 'Rho'])

df
