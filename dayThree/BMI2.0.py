# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
convert_height = float(height)
convert_weight = float(weight)
BMI = convert_weight / convert_height**2
print(int(BMI))

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
elif BMI >= 35:
  print(f"Your BMI is {BMI}, you are clinically obese.")