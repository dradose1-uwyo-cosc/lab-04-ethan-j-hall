item_names = [
    "milk", "cheezit", "lemonade", "candy", "gum"
]
item_prices = [
    4.32, 7.11, 3.57, 2.75, 1.52
]
for i in range(len(item_names)): 
    print(f"I bought {item_names[i]} for ${item_prices[i]}")
    
total = 0 
for t in item_prices:
    total = total + t 
print(f"I spent ${total} at Walmart")

leastIndex = item_prices.index(min(item_prices))

print(f"The cheapest item was {item_prices[leastIndex]}.")