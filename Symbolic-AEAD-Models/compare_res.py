import os
import csv

def read_csv(file_path):
    data = set()
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip empty rows
                if row[1] in {"False","True"}:
                    data.add((row[1],row[3]))
    return data

def compare_csv_files(folder1, folder2):
    # List all CSV files in folder1
    files1 = [f for f in os.listdir(folder1) if f.endswith('.csv')]

    
    for file1 in files1:
        # Construct the full path for the CSV file in folder1
        file1_path = os.path.join(folder1, file1)
        
        # Determine the corresponding file path in folder2
        file2_path = os.path.join(folder2, file1)
        
        print(file1)
        # Check if the corresponding file exists in folder2
        if os.path.exists(file2_path):
            # Read both CSV files
            data1 = read_csv(file1_path)
            data2 = read_csv(file2_path)
            #print(data2)
            #print(data1)
            
            # Find differences
            differences = data2.symmetric_difference(data1)
            #print(differences)
            
            if differences:
                print(f"Differences found in {file1}:")
                for diff in differences:
                    print(f" New: {diff[0]}, Precomputed: {diff[1]}")
        
        

# Example usage:
folder1 = 'results'
folder2 = 'results_precomputed'
compare_csv_files(folder1, folder2)
