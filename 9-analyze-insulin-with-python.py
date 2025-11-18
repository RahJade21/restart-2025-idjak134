import csv
import copy

myInsulin = {
    "insulin": "empty"
}

myInsulinList = []

with open('preproinsulin-seq.txt') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=" ")
    for row in csvReader:
        print(f'insulin: {" ".join(row)}')