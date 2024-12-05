import csv

def read_summary_and_rate(csv_file):
    summaries = []
    rates = []

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            summary = row['Summary']
            rate = row['Rate']
            summaries.append(summary)
            rates.append(rate)

    return summaries, rates

# Replace 'products.csv' with the actual name of your CSV file
csv_file = 'dataset.csv'
summaries, rates = read_summary_and_rate(csv_file)

print("Summaries:")
for summary in summaries:
    print(summary)

print("\nRates:")
for rate in rates:
    print(rate)
