import csv
import os
import random

# Create the dataset directory if it doesn't already exist
directory = "dataset"
if not os.path.exists(directory):
    os.makedirs(directory)

# Function to generate a random number with 'n' digits
def generate_random_number(n):
    return random.randint(10**(n-1), 10**n - 1)

# Generate each CSV file
for i in range(1, 31):  # For files 1.csv to 30.csv
    filename = os.path.join(directory, f"{i}.csv")
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['a', 'b', 'sum'])
        # Write 10 rows with 'a' and 'b' having 'i' digits, and their sum
        for _ in range(10):
            a = generate_random_number(i)
            b = generate_random_number(i)
            writer.writerow([a, b, a + b])