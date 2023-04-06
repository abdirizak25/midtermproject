import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Step 1: Reading CSV File
with open('data.csv') as csvfile:
    data = [row for row in csv.reader(csvfile)]

# Step 2: Total Sale
total_sales = [sum([int(x) for x in row[1:] if x.isnumeric()]) for row in data][1:]

with open('stats.txt', 'w') as outfile:
    for year, sales in enumerate(total_sales, start=2012):
        outfile.write(f"Total sales in {year}: {sales}\n")

# Step 3: Bar Plot

plt.bar(range(2012, 2023), total_sales)
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Sales per Year')
plt.show()

# Step 4: Sale Estimation
sales_2021 = [int(x) for x in data[-2][1:]]
sales_2022 = [int(x) for x in data[-1][1:6]]

a = sum(sales_2022)
b = sum(sales_2021[:6])
sgr = (a - b) / b

with open('stats.txt', 'a') as outfile:
    outfile.write(f"\nSales growth rate for first 6 months of 2022: {sgr:.2f}\n")

    estimated_sales_2022 = [int(x) + int(x) * sgr for x in sales_2021[-6:]]
    for month, sales in zip(['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], estimated_sales_2022):
        outfile.write(f"Estimated sales in {month} of 2022: {sales:.0f}\n")

# Step 5: Horizontal Bar Plot
plt.barh(range(6), estimated_sales_2022)
plt.yticks(range(6), ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.xlabel('Estimated Sales')
plt.ylabel('Month')
plt.title('Estimated Sales for Last Six Months of 2022')
plt.show()
