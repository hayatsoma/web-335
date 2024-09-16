"""
Author: Hayat Soma
Date: 9/01/2024
File Name: Soma_lemonadeStand.py
Description: This program simulates a lemonade stand. It calculates the cost of making lemonade and the profit from selling it.
"""

# Function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    """
    Calculates the total cost of making lemonade.
    
    Parameters:
    lemons_cost (float): The cost of lemons.
    sugar_cost (float): The cost of sugar.
    
    Returns:
    float: The total cost of making lemonade.
    """
    total_cost = lemons_cost + sugar_cost  # Calculating the total cost
    return total_cost  # Returning the total cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    """
    Calculates the profit from selling lemonade.
    
    Parameters:
    lemons_cost (float): The cost of lemons.
    sugar_cost (float): The cost of sugar.
    selling_price (float): The selling price of the lemonade.
    
    Returns:
    float: The profit from selling the lemonade.
    """
    total_cost = calculate_cost(lemons_cost, sugar_cost)  # Using the calculate_cost function to get total cost
    profit = selling_price - total_cost  # Calculating profit
    return profit  # Returning the profit

# Variables to test the functions
lemons_cost = 5.0  # Example cost of lemons
sugar_cost = 3.0   # Example cost of sugar
selling_price = 15.0  # Example selling price of the lemonade

# Testing the calculate_cost function
total_cost = calculate_cost(lemons_cost, sugar_cost)
cost_result = f"Cost of lemons (${lemons_cost}) + Cost of sugar (${sugar_cost}) = Total cost (${total_cost})"
print(cost_result)  # Output the result of the cost calculation

# Testing the calculate_profit function
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)
profit_result = f"Selling price (${selling_price}) - Total cost (${total_cost}) = Profit (${profit})"
print(profit_result)  # Output the result of the profit calculation
