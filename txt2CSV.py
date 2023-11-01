'''==> Convert Entire folders'''

import os
import csv


def combine_text_files(folder_path, output_file):
    files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as txt_file:
                lines = txt_file.readlines()[1:]  # Skip the first row

                for line in lines:
                    columns = line.strip().split()
                    writer.writerow(columns)


folder_path = 'Data'
output_file_path = 'walking.csv'
combine_text_files(folder_path, output_file_path)

# '''==> Convert Saperate File'''
# import csv

# with open('./NEW_txtFiles/Running1.txt', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split(",") for line in stripped if line)
#     with open('running12.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerows(lines)
