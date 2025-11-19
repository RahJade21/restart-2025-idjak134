import csv
import copy
import os

# make sure the folder exists
result_folder = "result"
if not os.path.exists(result_folder):
    os.makedirs(result_folder)
    print(f'Created folder: {result_folder}')
else:
    print(f'Folder already exists: {result_folder}')

# clean the data from space characters and save it into variable clean
with open('preproinsulin-seq.txt') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=" ")
    for row in csvReader:
        clean = "".join(row)
        print("========cleaning=========")
        print(clean)
        print(f'total line: {len(clean)} \n')
    
    # save into folder result with name file as below 
    with open("result/lsinsulin-seq-clean.txt", "w") as file1:
        file1.write(clean[:24])
        print(clean[:24])
        print(f'total line: {len(clean[:24])} \n')
        
    # save into folder result with name file as below 
    with open("result/binsulin-seq-clean.txt", "w") as file1:
        file1.write(clean[24:54])        
        print(clean[24:54])
        print(f'total line: {len(clean[24:54])} \n')

    # save into folder result with name file as below                 
    with open("result/cinsulin-seq-clean.txt", "w") as file1:
        file1.write(clean[54:89])
        print(clean[54:89])
        print(f'total line: {len(clean[54:89])} \n')
        
    # save into folder result with name file as below         
    with open("result/ainsulin-seq-clean.txt", "w") as file1:
        file1.write(clean[89:110])
        print(clean[89:110])
        print(f'total line: {len(clean[89:110])}')


# print(clean[:24])
# first = clean[:24]
# print(len(clean[:24]))

# print(clean[24:54])
# second = clean[24:54]
# print(len(clean[24:54]))

# print(clean[54:89])
# third = clean[54:89]
# print(len(clean[54:89]))

# print(clean[89:110])
# fourth = clean[89:110]
# print(len(clean[89:110]))

# folder_name = 'result/'
# file_name = 'insulin_sequences.csv'
# file_path = os.path.join(folder_name, file_name)

