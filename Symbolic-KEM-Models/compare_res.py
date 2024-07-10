import os
import csv

def read_csv(file_path):
    data = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        for row in reader:
            if row:  # Skip empty rows
                data[row[0]] = row[1]
    return data

def compare_csv_files(folder1, folder2):
    # Iterate over the folders in folder1
    for subdir1, _, files1 in os.walk(folder1):
        for file1 in files1:
            if file1.endswith('.csv'):
                # Construct the full path for the CSV file in folder1
                file1_path = os.path.join(subdir1, file1)
                
                # Determine the corresponding subfolder and file path in folder2
                subfolder_name = os.path.relpath(subdir1, folder1)
                file2_path = os.path.join(folder2, subfolder_name, file1)
                
                # Check if the corresponding file exists in folder2
                if os.path.exists(file2_path):
                    # Read both CSV files
                    data1 = read_csv(file1_path)
                    data2 = read_csv(file2_path)
                    
                    # Find differences
                    differences = []
                    for key in data1:
                        if key in data2 and data1[key] != data2[key]:
                            differences.append((key, data1[key], data2[key]))
                    
                    if differences:
                        print(f"Differences found in {subfolder_name}/{file1}:")
                        for diff in differences:
                            print(f"Name: {diff[0]} - New: {diff[1]}, Precomputed: {diff[2]}")

folder1 = 'RES'
folder2 = 'precomputed_RES'
compare_csv_files(folder1, folder2)
