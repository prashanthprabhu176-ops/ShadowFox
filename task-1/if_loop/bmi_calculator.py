height = float(input("Enter height in metres : "))
weight = int(input("Enter weight in kilograms: "))

bmi = weight / (height * height)

if bmi > 30:
    print("Obesity")
elif bmi > 25 and bmi < 29:
    print("Overweight")
elif bmi < 25 and bmi > 18.5:
    print("Normal")
elif bmi < 18.5:
    print("Underweight")
else:
    print("Enter proper values")
# Output :
# Enter height in metres : 1.75
# Enter weight in kilograms: 70
# Normal
