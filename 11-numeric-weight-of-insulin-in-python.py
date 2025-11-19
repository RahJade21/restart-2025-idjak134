# Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# lsinsulin = "malwmrllpllallalwgpdpaaa"
# binsulin = "fvnqhlcgshlvealylvcgergffytpkt"
# ainsulin = "giveqcctsicslyqlenycn"
# cinsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

with open("result/lsinsulin-seq-clean.txt", "r") as file1:
    lsinsulin = file1.read()
    print(lsinsulin)
with open("result/binsulin-seq-clean.txt", "r") as file1:
    binsulin = file1.read()
    print(binsulin)
with open("result/ainsulin-seq-clean.txt", "r") as file1:
    ainsulin = file1.read()
    print(ainsulin)
with open("result/cinsulin-seq-clean.txt", "r") as file1:
    cinsulin = file1.read()
    print(cinsulin)

insulin = binsulin + ainsulin
print("")
print(insulin)


# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))