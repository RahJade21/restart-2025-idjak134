import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# for key, value in myVehicle.items():
#     print("{} : {}".format(key,value))
    
myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1
            
    print(f'Processed {lineCount} lines.')
    
print(myInventoryList)

# [
#     {'vin': 'TMX20122', 'make': 'AnyCompany Motors', 'model': ' Coupe', 'year': ' 2012', 'range': ' 335', 'topSpeed': ' 155', 'zeroSixty': ' 4.1', 'mileage': ' 50000'}, 
#     {'vin': 'TM320163', 'make': 'AnyCompany Motors', 'model': ' Sedan', 'year': ' 2016', 'range': ' 240', 'topSpeed': ' 140', 'zeroSixty': ' 5.2', 'mileage': ' 20000'}, 
#     {'vin': 'TMX20121', 'make': 'AnyCompany Motors', 'model': ' SUV', 'year': ' 2012', 'range': ' 295', 'topSpeed': ' 155', 'zeroSixty': ' 4.7', 'mileage': ' 100000'}, 
#     {'vin': 'TMX20204', 'make': 'AnyCompany Motors', 'model': ' Truck', 'year': ' 2020', 'range': ' 300', 'topSpeed': ' 155', 'zeroSixty': ' 3.5', 'mileage': ' 0'}
# ]

# Column names are: vin, make, model, year, range, topSpeed, zeroSixty, mileage
# vin: TMX20122 make:  AnyCompany Motors, model:  Coupe, year:  2012, range:  335, topSpeed:  155, zeroSixty:  4.1, mileage:  50000
# vin: TM320163 make:  AnyCompany Motors, model:  Sedan, year:  2016, range:  240, topSpeed:  140, zeroSixty:  5.2, mileage:  20000
# vin: TMX20121 make:  AnyCompany Motors, model:  SUV, year:  2012, range:  295, topSpeed:  155, zeroSixty:  4.7, mileage:  100000
# vin: TMX20204 make:  AnyCompany Motors, model:  Truck, year:  2020, range:  300, topSpeed:  155, zeroSixty:  3.5, mileage:  0