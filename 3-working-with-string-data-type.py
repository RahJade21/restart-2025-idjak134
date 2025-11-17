# String variable
print("=== String (Alphabetical) ===")
myString = "Zauvik"
print(myString)
print(type(myString))
 
# Int variable
print("=== Integer (Bilangan bulat) ===")
myInt = 19
print(myInt)
print(type(myInt))
 
# Float variable
print("=== Float (Desimal) ===")
myFloat = 19.5
print(myFloat)
print(type(myFloat))
 
# Boolean variable
print("=== Boolean (Binary/True False) ===")
myBool = True
print(myBool)
print(type(myBool))
 
# Complex variable
print("=== Complex (Imaginer number) ===")
myImagine = 1j
print(myImagine)
print(type(myImagine))
 
 
# Math operations
print("=== Math operations ===")
num1 = 10
num2 = 5
 
# Variable type conversion. From integer to string
strNum1 = str(num1)
strNum2 = str(num2) + " ="
 
print(strNum1 + " + " + strNum2, num1 + num2)
print(strNum1 + " - " + strNum2, num1 - num2)
print(strNum1 + " * " + strNum2, num1 * num2)
print(strNum1 + " / " + strNum2, num1 / num2)
print(strNum1 + " % " + strNum2, num1 % num2) # Sisa bagi
 
 
print("Converting num1 from "+ str(type(num1)) + " to "+ str(type(strNum1)))
 
# Refactoring the code
typeNum1 = str(type(num1))
typeStrNum1 = str(type(strNum1))
print(f"Converting num1 from {typeNum1} to {typeStrNum1}")
 