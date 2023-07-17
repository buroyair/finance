import numpy as np

def option_pricing(binomial_tree, K, r, T, call=True):
    """
    Function to calculate the price of an option using a provided binomial tree.
    
    Parameters:
    binomial_tree: A 2D list representing the binomial tree.
    K: The strike price.
    r: The risk-free rate.
    T: The time to expiration of the option.
    call: A boolean to specify whether the option is a call or put.
    """

    # Create a similar structure for the option prices.
    option_prices = [[] for _ in range(len(binomial_tree))]
    
    # The last row of the option prices array is max(S-K, 0) for call options
    # and max(K-S, 0) for put options.
    if call:
        option_prices[-1] = list(np.maximum(np.array(binomial_tree[-1]) - K, 0))
    else:
        option_prices[-1] = list(np.maximum(K - np.array(binomial_tree[-1]), 0))
    
    # Print the initial option prices at expiry
    print(f"Option prices at T = {T}: {np.round(option_prices[-1], 4)}")

    # Iterate backwards through the tree
    for i in range(len(binomial_tree) - 2, -1, -1):
        for j in range(len(binomial_tree[i])):
            # Calculate the up and down factors
            d = binomial_tree[i + 1][j] / binomial_tree[i][j]
            u = binomial_tree[i + 1][j + 1] / binomial_tree[i][j]
            
            # Calculate the risk-neutral probabilities
            p = (np.exp(-r) - d) / (u - d)
            q = 1 - p
            
            # The price now is the discounted expected future price, using the risk-neutral probabilities
            option_price = np.exp(-r) * (q * option_prices[i + 1][j + 1] + p * option_prices[i + 1][j])
            option_prices[i].append(option_price)
            
            # Print the calculated option price at this step
            print(f"Step: {i}, Node: {j}, Down Factor: {round(d, 4)}, Up Factor: {round(u, 4)}, Down-move Probability: {round(q, 4)}, Up-move Probability: {round(p, 4)}, Calculation: e^(-{r})*({round(p, 4)}*{round(option_prices[i + 1][j + 1], 4)} + {round(q, 4)}*{round(option_prices[i + 1][j], 4)}) = {round(option_price, 4)}")
    
    # Return the current price of the option
    return round(option_prices[0][0], 4)

# Example usage:

# The price tree as a 2D list
binomial_tree = [
    [100],
    [90, 110],
    [80, 100, 120],
    [70, 90, 110, 130]
]

K = 95  # Strike price
r = 0.02  # Risk-free rate
T = 1  # Time to expiration

# Calculate and print the option prices
print("Call Option Price: ", option_pricing(binomial_tree, K, r, T, call=True))
print("\n---------------------\n")
print("Put Option Price: ", option_pricing(binomial_tree, K, r, T, call=False))
