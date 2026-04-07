print("tell me your height and weight and i will tell you your BMI rating.")
height =float(input("tell me how tall you are in metres"))
weight =float(input("tell me your weight in kilograms"))
BMI =weight / height ** 2
print("your BMI is",BMI)
if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <=34.9:
    print("you are obese")
else:
    print("you are severely obese")
