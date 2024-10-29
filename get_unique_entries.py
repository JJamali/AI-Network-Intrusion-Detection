import csv

# Specify the file paths
file_path = 'Train_data.csv'
output_path = 'unique_entries.md'

# Function to check if all elements are numbers
def is_numeric(entries):
    try:
        # Try converting all entries to float
        [float(entry) for entry in entries]
        return True
    except ValueError:
        return False

# Dictionary to store unique entries for each column (with column index as key)
unique_entries_by_column = {}

# Open the CSV file
with open(file_path, mode='r', newline='') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile)
    
    # Skip the first row (header)
    headers = next(reader)
    
    # Process each row
    for row in reader:
        # Process each column in the row
        for i, value in enumerate(row):
            # Initialize a set for each column if not already initialized
            if i not in unique_entries_by_column:
                unique_entries_by_column[i] = set()
            # Add the value to the set for the column
            unique_entries_by_column[i].add(value)
            
# Filter columns to only include those with 6+ unique non-numeric entries
filtered_columns = {i: entries for i, entries in unique_entries_by_column.items() 
                    if len(entries) >= 6 and not is_numeric(entries)}

# Write the unique entries to a Markdown file
with open(output_path, mode='w') as mdfile:
    # Loop over filtered columns
    for col_index, entries in filtered_columns.items():
        # Write column title and entries
        mdfile.write(f"## Unique entries in column {col_index + 1} ({headers[col_index]})\n\n")
        for entry in entries:
            mdfile.write(f"{entry}\n")
        mdfile.write("\n")

print(f"Unique entries have been written to '{output_path}'.")
