# lists
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# var for total price
total_price = 0

for price in prices:
    total_price += price

# getting average price
average_price = total_price / 8
print("Average Haircut Price: " + str(average_price))

# new prices and print
new_prices = [price - 5 for price in prices]
print(new_prices)

# getting revenue
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue = prices[i] + last_week[i]

print(total_revenue)

# getting daily average revenue
average_daily_revenue = total_revenue / 7

# defining all cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)
