import random

systemNumber = random.randint(1, 10)
print(f'contekan: {systemNumber}')
while True:
    guessNumber = input("Tebak angka 1-10: ")
    
    if (systemNumber) == int(guessNumber):
        print("You are win bro!")
        break
    else:
        print("Ulangi lagi deh, salah nih")

# print("====")
# # Refactoring kode dengan loop for
# for i in range(2, 6):
#     print(f'angka {i}')
    
# print("===range variation===")
# myList = list(range(6))
# print(myList)
# myList = list(range(1, 6))
# print(myList)
# myList = list(range(1, 6, 2))
# print(myList)

# for i, z in enumerate(myList):
#     print(f'Nilai my list index ke {i} adalah {z}')
    
# # study case
# namaSiswa = ['pritvi', 'ginda', 'abdul', 'christoper']
# for nm in namaSiswa:
#     print(f'{nm} hadir')
    
# listNumbers = [1, 2, 4, 100]
# tempSum = 0
# for ln in listNumbers:
#     tempSum = tempSum + ln
    
# print(tempSum)