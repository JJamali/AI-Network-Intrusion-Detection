import csv

# Specify the file path to your CSV file
file_path = 'Train_data.csv'

# Use a set to store unique entries
unique_entries = set()

# Open the CSV file
with open(file_path, mode='r', newline='') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile)
    
    # Loop through each row in the CSV file
    for row in reader:
        # Ensure the row has at least 3 columns
        if len(row) >= 3:
            # Add the entry from the third column to the set
            unique_entries.add(row[2])

# Print each unique entry
for entry in unique_entries:
    print(entry)
