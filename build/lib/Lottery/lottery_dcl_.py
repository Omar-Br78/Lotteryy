# import the csv module to open .csv files
import csv

def load_historical_data(file_path):
    """Create a Function to Load the Historical Data from the file orcl.csv into a list of dictionaries"""

    data = [] # Initialize an empty list
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            data.append(row)
    return data


def calculate_sma(data, window):
    """Create a Function to calculate the Simple Moving Averages for a 5-day window"""

    sma = []  # Initialize an empty list

    """Use List comprehension"""

    close_prices = [float(row['Close']) for row in data]

    for i in range(len(close_prices)):
        if i < window - 1:
            sma.append(None)
        else:
            sma.append(sum(close_prices[i - window + 1:i + 1]) / window)

    return sma

def calculate_rsi(data, window):
    """Create a Function to calculate the Relative Strength Index (RSI) for a 14-day window"""

    rsi = [] # Initialize an empty list

    """Use List comprehension"""

    close_prices = [float(row['Close']) for row in data]

    gain = [max(0, close_prices[i] - close_prices[i - 1]) for i in range(1, len(close_prices))]
    loss = [max(0, close_prices[i - 1] - close_prices[i]) for i in range(1, len(close_prices))]

    avg_gain = sum(gain[:window]) / window
    avg_loss = sum(loss[:window]) / window

    for i in range(len(close_prices)):
        if i < window - 1:
            rsi.append(None)
        else:
            avg_gain = ((avg_gain * (window - 1)) + gain[i - 1]) / window
            avg_loss = ((avg_loss * (window - 1)) + loss[i - 1]) / window

            if avg_loss == 0:
                rsi.append(100)
            else:
                rs = avg_gain / avg_loss
                rsi.append(100 - (100 / (1 + rs)))

    return rsi


def write_to_csv(file_path, header, data):
    """Write data to a CSV file"""

    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)

# Add orcl.csv file path
csv_file_path = '  '

# Call the function to load historical data
historical_data = load_historical_data(csv_file_path)

# Calculate 5-day Simple Moving Averages (SMA)
sma_5 = calculate_sma(historical_data, window=5)

# Calculate 14-day Relative Strength Index (RSI) using the provided formula
rsi_14 = calculate_rsi(historical_data, window=14)

# Write SMA to CSV
sma_header = ['Date', 'SMA_5']
sma_data = [[row['Date'], sma] for row, sma in zip(historical_data, sma_5)] # Use the zip function to combine historical_data, sma_5
write_to_csv('orcl-sma.csv', sma_header, sma_data)

# Write RSI to CSV
rsi_header = ['Date', 'RSI_14']
rsi_data = [[row['Date'], rsi] for row, rsi in zip(historical_data, rsi_14)] # Use the zip function to combine historical_data, rsi_14
write_to_csv('orcl-rsi.csv', rsi_header, rsi_data)

# Print the desired output
print(historical_data[:5])
print("5-day SMA:", sma_5[:5])
print("14-day RSI:", rsi_14[:5])
print("Files 'orcl-sma.csv' and 'orcl-rsi.csv' written successfully.")


