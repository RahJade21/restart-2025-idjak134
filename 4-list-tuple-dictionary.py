# List, Tuple, and Dictionary are composite data type
# List
# ....
# import json

# myList = ['Jeruk', 'Anggur', 'Apel']
# print(type(myList))
# print(myList)

# # Tuple
# myTuple = ('Jeruk', 'Anggur', 'Apel', 5000)
# print(type(myTuple))
# print(myTuple)
# print(myTuple[1])

# # Dictionary
# myDictionary = {
#     'buah1': 'Jeruk',
#     'buah2': 'Anggur',
#     'buah3': 'Apel',
#     'harga': 50000
# }

# print(type(myDictionary))
# print(myDictionary)
# print(myDictionary['buah2'])
# myDictionary['buah1'] = 'Jeruk Bali'
# print(myDictionary)

# print(json.dumps(myDictionary, indent=2))


# Challange ==========
myProgramming = ['python', 'shell', 'javascript', 'php', 'golang', 'c++']
# print(myProgramming[-2:])
# print(myProgramming[4:])
# print(myProgramming[4:6])

myComplexDict = {
    'name': 'raden kanjeng',
    'alamat': {
        'provinsi': 'jawa tengah',
        'kecamatan': 'laweyan',
        'desa': 'peramban indah',
        'rt': '01',
        'rw': '02',
    },
    'siblings': ['azizah', 'anisa', 'pramudita']
}
