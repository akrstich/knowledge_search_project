import os
import requests
import pandas as pd

# Define the URL to the Stack Overflow data dump (adjust this URL as needed)
stack_overflow_url = 'https://archive.org/download/stackexchange/stackoverflow.com-Posts.7z'

# Define the local path where you want to save the data
save_path = 'knowledge_search/data/raw/'

# Create the directory if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Download the data
response = requests.get(stack_overflow_url)

# Check if the download was successful
if response.status_code == 200:
    with open(os.path.join(save_path, 'stackoverflow_data.7z'), 'wb') as file:
        file.write(response.content)
    print("Stack Overflow data downloaded successfully.")
else:
    print("Failed to download Stack Overflow data.")

# Sample a subset of the data (adjust the sample size as needed)
sample_size = 1000  # You can change this to your desired sample size

# Load the downloaded data into a DataFrame
data = pd.read_csv(os.path.join(save_path, 'stackoverflow_data.7z'), compression='7z', encoding='utf-8', nrows=sample_size)

# Save the sampled data as a CSV file
data.to_csv(os.path.join(save_path, 'sampled_stackoverflow_data.csv'), index=False)

print(f"Sampled {sample_size} rows of Stack Overflow data.")