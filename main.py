height=float(input('enter height in meters\n'))
weight=int(input('enter weight in kgs\n'))

bmi= float(weight/(height**2))
print (f"your BMI is {bmi}")

if bmi <= 15.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 31.9:
    print("You are over weight.")
elif bmi <= 40.9:
    print("You are severely over weight.")
elif bmi <= 48.9:
    print("You are obese.")
else:
    print("You are severely obese.")