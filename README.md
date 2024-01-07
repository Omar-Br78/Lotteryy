# Stock Analysis Script (Lottery)

This Python script analyzes historical stock data stored in a CSV file (`orcl.csv`). It calculates and writes two technical indicators, the 5-day Simple Moving Averages (SMA) and the 14-day Relative Strength Index (RSI), to separate CSV files (`orcl-sma.csv` and `orcl-rsi.csv`).

## Installation

You can install the `lottery_DCL` package using `pip`. Open your terminal or command prompt and run the following command:

```bash
pip install lottery-DCL==0.1.1

```

## Usage

1. **Import the Package**:

In your Python script or interactive session, import the lottery_DCL package

    ```python
    import lottery_DCL
    ```


2. **Load Historical Data:**
   - The script first loads historical stock data from a CSV file (`orcl.csv` in this example). The data is expected to have columns like 'Date', 'Open', 'High', 'Low', 'Close', 'Volume', etc. Make sure to adjust the `csv_file_path` variable with the correct path to your CSV file.

    ```python
    csv_file_path = ' '  # Add orcl.csv file path
    historical_data = load_historical_data(csv_file_path)
    ```

3. **Run the Script:**
   - Execute the script to load the historical data, calculate technical indicators, and write the results to CSV files. Run the following command in the command line:

    ```bash
    python lottery_DCL.py
    ```

## Output Files

Two CSV files (`orcl-sma.csv` and `orcl-rsi.csv`) will be generated with the calculated SMA and RSI values, respectively.

## Functions

- **load_historical_data(file_path):**
  - Loads historical stock data from the specified CSV file into a list of dictionaries.

- **calculate_sma(data, window):**
  - Calculates the 5-day Simple Moving Averages (SMA) for the given historical data.

- **calculate_rsi(data, window):**
  - Calculates the 14-day Relative Strength Index (RSI) for the given historical data using a provided formula.

- **write_to_csv(file_path, header, data):**
  - Writes data to a CSV file with the specified header.

## The Stracture of The File:
The Structure of The File:

my-python-project
│───README.md
│───setup.py
│
│
└───Lottery
│ init.py
│ lottery_dcl_.py



## Example of Usage

```python
csv_file_path = ' '  # Add orcl.csv file path
historical_data = load_historical_data(csv_file_path)

sma_5 = calculate_sma(historical_data, window=5)
rsi_14 = calculate_rsi(historical_data, window=14)

sma_header = ['Date', 'SMA_5']
sma_data = [[row['Date'], sma] for row, sma in zip(historical_data, sma_5)]
write_to_csv('orcl-sma.csv', sma_header, sma_data)

rsi_header = ['Date', 'RSI_14']
rsi_data = [[row['Date'], rsi] for row, rsi in zip(historical_data, rsi_14)]
write_to_csv('orcl-rsi.csv', rsi_header, rsi_data)

print(historical_data[:5])
print("5-day SMA:", sma_5[:5])
print("14-day RSI:", rsi_14[:5])
print("Files 'orcl-sma.csv' and 'orcl-rsi.csv' written successfully.")

